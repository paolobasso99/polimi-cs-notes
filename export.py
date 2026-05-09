"""Export a BookStack instance to a local markdown tree.

Layout produced under ./content/:

    content/
      books/
        <book-slug>/
          _book.md                       (book description + frontmatter)
          <page-slug>.md                 (pages directly under the book)
          <chapter-slug>/
            _chapter.md                  (chapter description + frontmatter)
            <page-slug>.md
      images/
        <hash>_<original-name>           (deduplicated by URL hash)

Image references inside each page's markdown are rewritten to relative
paths so the markdown stays portable and editable. Re-running the script
is idempotent: existing images are reused, pages are overwritten.
"""

from __future__ import annotations

import hashlib
import os
import re
import sys
import time
import unicodedata
from collections.abc import Iterable
from pathlib import Path
from typing import Any, cast
from urllib.parse import unquote, urlparse

import frontmatter  # type: ignore[import-untyped]
import requests
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
CONTENT_DIR = ROOT / "content"
BOOKS_DIR = CONTENT_DIR / "books"
IMAGES_DIR = CONTENT_DIR / "images"

load_dotenv(ROOT / ".env")

BASE_URL = os.environ.get("BOOKSTACK_BASE_URL", "").rstrip("/")
TOKEN_ID = os.environ.get("BOOKSTACK_TOKEN_ID", "")
TOKEN_SECRET = os.environ.get("BOOKSTACK_TOKEN_SECRET", "")

if not (BASE_URL and TOKEN_ID and TOKEN_SECRET):
    sys.exit(
        "Missing BOOKSTACK_BASE_URL / BOOKSTACK_TOKEN_ID / BOOKSTACK_TOKEN_SECRET. "
        "Copy .env.example to .env and fill it in."
    )

session = requests.Session()
session.headers.update(
    {
        "Authorization": f"Token {TOKEN_ID}:{TOKEN_SECRET}",
        "Accept": "application/json",
        "User-Agent": "bookstack-export/1.0",
    }
)


# ---------- API helpers ---------------------------------------------------- #

def api_get(path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
    url = f"{BASE_URL}{path}"
    for _attempt in range(3):
        r = session.get(url, params=params, timeout=30)
        if r.status_code == 429:
            wait = int(r.headers.get("Retry-After", "2"))
            time.sleep(wait)
            continue
        r.raise_for_status()
        return cast(dict[str, Any], r.json())
    r.raise_for_status()
    return {}


def api_paginated(path: str) -> Iterable[dict[str, Any]]:
    offset = 0
    page_size = 200
    while True:
        data = api_get(path, params={"count": page_size, "offset": offset})
        items = data.get("data", [])
        if not items:
            return
        yield from items
        offset += len(items)
        if offset >= data.get("total", 0):
            return


def fetch_page_markdown(page_id: int) -> str:
    url = f"{BASE_URL}/api/pages/{page_id}/export/markdown"
    r = session.get(url, timeout=60)
    r.raise_for_status()
    return r.text


# ---------- filesystem helpers --------------------------------------------- #

def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text or "")
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    text = re.sub(r"[-\s_]+", "-", text)
    return text or "untitled"


def write_markdown(path: Path, body: str, meta: dict[str, Any]) -> None:
    post = frontmatter.Post(body, **meta)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as f:
        frontmatter.dump(post, f)


# ---------- image localization --------------------------------------------- #

# Matches markdown images: ![alt](url "optional title")
IMAGE_RE = re.compile(r"!\[(?P<alt>[^\]]*)\]\((?P<url>\S+?)(?P<title>\s+\"[^\"]*\")?\)")

# Matches HTML <img ... src="url" ...> tags (used by BookStack for draw.io diagrams)
HTML_IMG_RE = re.compile(r"""(<img\b[^>]*?\bsrc=)(["'])([^"']+)\2""", re.IGNORECASE)

# Matches the BookStack pattern of an image wrapped in a click-through link to
# the full-size original: [![alt](inner_url)](outer_url). After image localization,
# the outer URL is rewritten to match the (now-local) inner URL.
WRAPPING_IMG_RE = re.compile(
    r"\[(?P<inner>!\[[^\]]*\]\((?P<inner_url>\S+?)(?:\s+\"[^\"]*\")?\))\]"
    r"\((?P<outer_url>\S+?)(?:\s+\"[^\"]*\")?\)"
)


def _is_local_url(url: str) -> bool:
    if url.startswith("/"):
        return True
    parsed = urlparse(url)
    base_host = urlparse(BASE_URL).netloc
    return parsed.netloc == base_host


def _download_image(url: str) -> Path | None:
    full_url = url if url.startswith("http") else f"{BASE_URL}{url}"
    parsed = urlparse(full_url)
    raw_name = unquote(os.path.basename(parsed.path)) or "image"
    raw_name = re.sub(r"[^A-Za-z0-9._-]", "_", raw_name)
    digest = hashlib.sha1(full_url.encode("utf-8")).hexdigest()[:10]
    local_path = IMAGES_DIR / f"{digest}_{raw_name}"

    if local_path.exists():
        return local_path

    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    try:
        r = session.get(full_url, timeout=60, stream=True)
        r.raise_for_status()
        with open(local_path, "wb") as f:
            for chunk in r.iter_content(8192):
                f.write(chunk)
        return local_path
    except Exception as exc:
        print(f"    ! image download failed for {full_url}: {exc}")
        if local_path.exists():
            local_path.unlink(missing_ok=True)
        return None


def localize_images(md_text: str, md_path: Path) -> str:
    def repl_md(match: re.Match[str]) -> str:
        url = match.group("url")
        if not _is_local_url(url):
            return match.group(0)
        local = _download_image(url)
        if not local:
            return match.group(0)
        rel = os.path.relpath(local, md_path.parent)
        title = match.group("title") or ""
        return f'![{match.group("alt")}]({rel}{title})'

    def repl_html(match: re.Match[str]) -> str:
        url = match.group(3)
        if not _is_local_url(url):
            return match.group(0)
        local = _download_image(url)
        if not local:
            return match.group(0)
        rel = os.path.relpath(local, md_path.parent)
        return f"{match.group(1)}{match.group(2)}{rel}{match.group(2)}"

    def repl_wrap(match: re.Match[str]) -> str:
        outer = match.group("outer_url")
        if not _is_local_url(outer):
            return match.group(0)
        inner = match.group("inner_url")
        return f"[{match.group('inner')}]({inner})"

    md_text = IMAGE_RE.sub(repl_md, md_text)
    md_text = HTML_IMG_RE.sub(repl_html, md_text)
    md_text = WRAPPING_IMG_RE.sub(repl_wrap, md_text)
    return md_text


def fix_text_artifacts(text: str) -> str:
    """Repair encoding/keyboard artifacts in BookStack-exported markdown.
    U+00A5 (¥) appears where backslashes were intended (Japanese-locale
    keyboard or Shift-JIS round-trip), breaking LaTeX commands like
    `¥begin{align*}` and `¥lambda`."""
    return text.replace("¥", "\\")


# ---------- export passes -------------------------------------------------- #

def export_page(
    page_summary: dict[str, Any],
    parent_dir: Path,
    book: dict[str, Any],
    chapter: dict[str, Any] | None,
) -> None:
    if page_summary.get("draft"):
        return
    page_id = page_summary["id"]
    page_slug = page_summary.get("slug") or slugify(page_summary["name"])
    md_path = parent_dir / f"{page_slug}.md"

    label = "    " if chapter else "  "
    print(f"{label}page: {page_summary['name']}")

    try:
        md_text = fetch_page_markdown(page_id)
    except Exception as exc:
        print(f"{label}! failed to export page {page_id}: {exc}")
        return

    md_text = fix_text_artifacts(md_text)
    md_text = localize_images(md_text, md_path)

    meta: dict[str, Any] = {
        "title": page_summary["name"],
        "type": "page",
        "id": page_id,
        "slug": page_slug,
        "priority": page_summary.get("priority", 0),
        "book_slug": book["slug"],
        "book_title": book["name"],
    }
    if chapter:
        meta["chapter_slug"] = chapter["slug"]
        meta["chapter_title"] = chapter["name"]
    if page_summary.get("updated_at"):
        meta["updated_at"] = page_summary["updated_at"]
    if page_summary.get("created_at"):
        meta["created_at"] = page_summary["created_at"]

    write_markdown(md_path, md_text, meta)


def export_chapter(chapter_summary: dict[str, Any], book_dir: Path, book: dict[str, Any]) -> None:
    chapter = api_get(f"/api/chapters/{chapter_summary['id']}")
    chapter_slug = chapter.get("slug") or slugify(chapter["name"])
    chapter_dir = book_dir / chapter_slug
    chapter_dir.mkdir(parents=True, exist_ok=True)

    print(f"  chapter: {chapter['name']}")

    chapter_meta_path = chapter_dir / "_chapter.md"
    description = chapter.get("description") or ""
    description = fix_text_artifacts(description)
    description = localize_images(description, chapter_meta_path)
    write_markdown(
        chapter_meta_path,
        description,
        {
            "title": chapter["name"],
            "type": "chapter",
            "id": chapter["id"],
            "slug": chapter_slug,
            "priority": chapter_summary.get("priority", chapter.get("priority", 0)),
            "book_slug": book["slug"],
            "book_title": book["name"],
        },
    )

    chapter_short = {"slug": chapter_slug, "name": chapter["name"], "id": chapter["id"]}
    for page in chapter.get("pages", []):
        export_page(page, chapter_dir, book, chapter_short)


def export_book(book_summary: dict[str, Any]) -> None:
    book = api_get(f"/api/books/{book_summary['id']}")
    book_slug = book.get("slug") or slugify(book["name"])
    book_dir = BOOKS_DIR / book_slug
    book_dir.mkdir(parents=True, exist_ok=True)

    print(f"\nbook: {book['name']}")

    book_meta_path = book_dir / "_book.md"
    description = book.get("description") or ""
    description = fix_text_artifacts(description)
    description = localize_images(description, book_meta_path)
    write_markdown(
        book_meta_path,
        description,
        {
            "title": book["name"],
            "type": "book",
            "id": book["id"],
            "slug": book_slug,
            "priority": book_summary.get("priority", 0),
        },
    )

    book_short = {"slug": book_slug, "name": book["name"], "id": book["id"]}
    for item in book.get("contents", []):
        if item.get("type") == "chapter":
            export_chapter(item, book_dir, book_short)
        elif item.get("type") == "page":
            export_page(item, book_dir, book_short, chapter=None)


def main() -> None:
    BOOKS_DIR.mkdir(parents=True, exist_ok=True)
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    books = list(api_paginated("/api/books"))
    print(f"found {len(books)} books")

    for book in books:
        try:
            export_book(book)
        except Exception as exc:
            print(f"! failed to export book {book.get('name', book.get('id'))}: {exc}")

    print("\nexport complete.")


if __name__ == "__main__":
    main()
