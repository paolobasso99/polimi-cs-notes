"""Build a static HTML site from the markdown tree under ./content/.

Output goes to ./site/, mirroring the book/chapter/page hierarchy and
suitable for GitHub Pages. Styling is BookStack-like: white content card,
left sidebar with the book tree, primary blue (#206ea7), and Tailwind's
typography plugin for prose. Tailwind is loaded via the Play CDN so the
output is purely static HTML — no build step.

Run after editing markdown to regenerate the site.
"""

from __future__ import annotations

import html
import json
import os
import re
import shutil
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, cast

import frontmatter  # type: ignore[import-untyped]
import markdown
from dotenv import load_dotenv
from pygments.formatters import HtmlFormatter

ROOT = Path(__file__).resolve().parent
CONTENT_DIR = ROOT / "content"
BOOKS_DIR = CONTENT_DIR / "books"
IMAGES_DIR = CONTENT_DIR / "images"
SITE_DIR = ROOT / "site"
VENDOR_DIR = ROOT / "assets" / "vendor"
ICONS_DIR = VENDOR_DIR / "icons"

load_dotenv(ROOT / ".env")
SITE_TITLE = os.environ.get("SITE_TITLE", "Documentation")
SITE_BASE_PATH = os.environ.get("SITE_BASE_PATH", "").rstrip("/")
SITE_URL = os.environ.get("SITE_URL", "").rstrip("/")
SITE_DESCRIPTION = os.environ.get(
    "SITE_DESCRIPTION",
    "Notes from the Computer Science and Engineering Master's at Politecnico di Milano (2021-2023).",
)


# ---------- data model ----------------------------------------------------- #


@dataclass
class Page:
    title: str
    slug: str
    priority: int
    body: str
    meta: dict[str, Any]
    md_path: Path
    url: str  # site-root-relative, e.g. "books/foo/bar.html"


@dataclass
class Chapter:
    title: str
    slug: str
    priority: int
    description_body: str
    description_meta: dict[str, Any]
    pages: list[Page] = field(default_factory=list)
    url: str = ""


BookItem = Chapter | Page


@dataclass
class Book:
    title: str
    slug: str
    priority: int
    description_body: str
    description_meta: dict[str, Any]
    items: list[BookItem] = field(default_factory=list)
    url: str = ""


# ---------- loading -------------------------------------------------------- #


def _load_md(path: Path) -> tuple[str, dict[str, Any]]:
    with open(path, encoding="utf-8") as f:
        post = frontmatter.load(f)
    return cast(str, post.content), dict(post.metadata)


def _load_book(book_dir: Path) -> Book:
    book_slug = book_dir.name
    book_md = book_dir / "_book.md"
    if book_md.exists():
        body, meta = _load_md(book_md)
    else:
        body, meta = "", {"title": book_slug.replace("-", " ").title()}

    book = Book(
        title=meta.get("title", book_slug),
        slug=book_slug,
        priority=int(meta.get("priority", 0) or 0),
        description_body=body,
        description_meta=meta,
        url=f"books/{book_slug}/index.html",
    )

    raw_items: list[BookItem] = []
    for entry in sorted(book_dir.iterdir()):
        if entry.name.startswith("_") or entry.name.startswith("."):
            continue
        if entry.is_dir():
            raw_items.append(_load_chapter(entry, book_slug))
        elif entry.suffix == ".md":
            raw_items.append(_load_page(entry, book_slug, chapter_slug=None))

    raw_items.sort(key=lambda it: (it.priority, it.title.lower()))
    book.items = raw_items
    return book


def _load_chapter(chapter_dir: Path, book_slug: str) -> Chapter:
    chapter_slug = chapter_dir.name
    chapter_md = chapter_dir / "_chapter.md"
    if chapter_md.exists():
        body, meta = _load_md(chapter_md)
    else:
        body, meta = "", {"title": chapter_slug.replace("-", " ").title()}

    chapter = Chapter(
        title=meta.get("title", chapter_slug),
        slug=chapter_slug,
        priority=int(meta.get("priority", 0) or 0),
        description_body=body,
        description_meta=meta,
        url=f"books/{book_slug}/{chapter_slug}/index.html",
    )

    pages = []
    for entry in sorted(chapter_dir.iterdir()):
        if entry.name.startswith("_") or entry.name.startswith("."):
            continue
        if entry.suffix == ".md":
            pages.append(_load_page(entry, book_slug, chapter_slug=chapter_slug))
    pages.sort(key=lambda p: (p.priority, p.title.lower()))
    chapter.pages = pages
    return chapter


def _load_page(md_path: Path, book_slug: str, chapter_slug: str | None) -> Page:
    body, meta = _load_md(md_path)
    slug = md_path.stem
    url = f"books/{book_slug}/{chapter_slug}/{slug}.html" if chapter_slug else f"books/{book_slug}/{slug}.html"
    return Page(
        title=meta.get("title", slug.replace("-", " ").title()),
        slug=slug,
        priority=int(meta.get("priority", 0) or 0),
        body=body,
        meta=meta,
        md_path=md_path,
        url=url,
    )


def load_books() -> list[Book]:
    if not BOOKS_DIR.exists():
        return []
    books = []
    for book_dir in sorted(BOOKS_DIR.iterdir()):
        if book_dir.is_dir():
            books.append(_load_book(book_dir))
    books.sort(key=lambda b: (b.priority, b.title.lower()))
    return books


# ---------- markdown rendering --------------------------------------------- #

MD_EXTENSIONS = [
    "fenced_code",
    "codehilite",
    "tables",
    "toc",
    "sane_lists",
    "attr_list",
    "def_list",
    "footnotes",
    "md_in_html",
]
MD_CONFIG = {
    "codehilite": {"css_class": "highlight", "guess_lang": False},
    "toc": {"permalink": False},
}


def _md() -> markdown.Markdown:
    return markdown.Markdown(extensions=MD_EXTENSIONS, extension_configs=cast(Any, MD_CONFIG))


def _rewrite_md_links(md_text: str, page_url: str) -> str:
    """Rewrite internal links from `something.md` to `something.html`.

    Image and asset paths are left as-is — they are already relative paths
    in the markdown tree, and we mirror that tree into the site/ output.
    """
    link_re = re.compile(r"(\]\()([^)\s]+?)(\.md)((?:#[^)]*)?)\)")
    return link_re.sub(lambda m: f"{m.group(1)}{m.group(2)}.html{m.group(4)})", md_text)


_LIST_LINE = re.compile(r"^([-*+]|\d+\.)\s\S")

_PAREN_OL_RE = re.compile(r"^(\s*)(\d+)\)(\s)", re.MULTILINE)


def _normalize_paren_ordered_lists(text: str) -> str:
    """Rewrite `1) ...` line starts to `1. ...` so Python-Markdown's sane_lists
    recognizes them as ordered list items."""
    return _PAREN_OL_RE.sub(r"\1\2.\3", text)


def _strip_leading_h1(text: str) -> str:
    """Drop a leading H1 line. BookStack exports repeat the title as the first
    H1, but the layout already renders it as a heading."""
    lines = text.split("\n")
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines) and re.match(r"^#\s+\S", lines[i]):
        del lines[i]
        while i < len(lines) and not lines[i].strip():
            del lines[i]
    return "\n".join(lines)


def _normalize_lists(text: str) -> str:
    """Insert a blank line before a top-level list when it follows a paragraph.

    BookStack exports lists without a separating blank line; Python-Markdown
    then renders them inline with the paragraph. We only touch column-0 list
    items whose previous line is a non-empty, non-indented, non-list line —
    leaves nested lists, code blocks, and existing properly-spaced lists alone.
    """
    lines = text.split("\n")
    out: list[str] = []
    in_fence = False
    for i, line in enumerate(lines):
        if line.startswith("```") or line.startswith("~~~"):
            in_fence = not in_fence
            out.append(line)
            continue
        if not in_fence and i > 0 and _LIST_LINE.match(line):
            prev = lines[i - 1]
            if prev.strip() and not prev.startswith((" ", "\t")) and not _LIST_LINE.match(prev):
                out.append("")
        out.append(line)
    return "\n".join(out)


_TABLE_RE = re.compile(r"(<table\b[^>]*>[\s\S]*?</table>)", re.IGNORECASE)


_DISPLAY_MATH_RE = re.compile(r"\$\$[\s\S]+?\$\$")
_INLINE_MATH_RE = re.compile(r"(?<!\$)\$(?!\$)[^\n$]+?(?<!\$)\$(?!\$)")


def _protect_math(text: str) -> tuple[str, list[str]]:
    """Replace $$…$$ and $…$ with opaque placeholders so Markdown leaves them
    alone. Without this, characters like `*` (e.g. `\\begin{align*}`) get
    interpreted as emphasis and KaTeX can no longer parse the block."""
    blocks: list[str] = []

    def take(match: re.Match[str]) -> str:
        blocks.append(match.group(0))
        return f"MATHBLOCK{len(blocks) - 1}MATHEND"

    text = _DISPLAY_MATH_RE.sub(take, text)
    text = _INLINE_MATH_RE.sub(take, text)
    return text, blocks


def _restore_math(html_out: str, blocks: list[str]) -> str:
    for i, content in enumerate(blocks):
        html_out = html_out.replace(f"MATHBLOCK{i}MATHEND", html.escape(content))
    return html_out


_DETAILS_RE = re.compile(r"<details(?![^>]*\bmarkdown=)([^>]*)>", re.IGNORECASE)


def _enable_md_in_details(text: str) -> str:
    """Add markdown="1" to <details> tags so md_in_html processes their bodies.
    BookStack exports collapsible solutions as <details>...<summary>...</summary>
    markdown body</details>; without the attribute, the inner lists render raw."""
    return _DETAILS_RE.sub(r'<details markdown="1"\1>', text)


def _wrap_tables(html_out: str) -> str:
    """Wrap each <table> in a scrollable container so wide tables don't
    overflow the article column on narrow viewports."""
    return _TABLE_RE.sub(r'<div class="table-wrap">\1</div>', html_out)


def render_markdown(body: str, page_url: str) -> str:
    body = _strip_leading_h1(body)
    body = _enable_md_in_details(body)
    body, math_blocks = _protect_math(body)
    body = _rewrite_md_links(body, page_url)
    body = _normalize_paren_ordered_lists(body)
    body = _normalize_lists(body)
    if not body.strip():
        return ""
    html_out = _wrap_tables(_md().convert(body))
    return _restore_math(html_out, math_blocks)


# ---------- url helpers ---------------------------------------------------- #


def root_prefix(page_url: str) -> str:
    """Relative path from this page back to site root."""
    depth = page_url.count("/")
    return "../" * depth if depth else ""


def link(target_url: str, from_url: str) -> str:
    """Compute href for `target_url` from a page at `from_url`."""
    return root_prefix(from_url) + target_url


# ---------- templates ------------------------------------------------------ #


def _esc(s: str) -> str:
    return html.escape(s, quote=True)


def _sidebar_link(href: str, kind: str, label: str, active: bool, base_cls: str) -> str:
    cls = (
        f"{base_cls} active text-primary-700 font-semibold"
        if active
        else f"{base_cls} text-gray-700 hover:text-primary-600"
    )
    return f'<a href="{_esc(href)}" class="{cls}">{_ion(kind, "icn")}<span class="label label-{kind}">{_esc(label)}</span></a>'


def render_sidebar(books: list[Book], current: dict[str, Any], from_url: str) -> str:
    """Sidebar with all books listed; the current book is expanded.

    `current` keys: book_slug, chapter_slug (optional), page_url (optional).
    """
    out = [
        '<nav class="sidebar bg-white rounded-md border border-gray-200 shadow-sm p-4 sticky top-4 max-h-[calc(100vh-2rem)] overflow-y-auto text-[0.95rem]">'
    ]
    out.append('<div class="text-[11px] uppercase tracking-wider text-gray-500 mb-3 font-semibold">Books</div>')
    out.append('<ul class="space-y-0.5">')

    for book in books:
        is_current_book = current.get("book_slug") == book.slug
        href = link(book.url, from_url)
        has_items = bool(book.items)
        book_open_cls = " open" if is_current_book else ""
        out.append(f'<li class="tree-node{book_open_cls}">')
        out.append('<div class="tree-row">')
        if has_items:
            out.append(
                f'<button type="button" class="chev" aria-label="Toggle book">{_ion("chevron", "chev-icn")}</button>'
            )
        else:
            out.append('<span class="chev-spacer"></span>')
        out.append(_sidebar_link(href, "book", book.title, is_current_book, "py-1 flex-1"))
        out.append("</div>")

        if has_items:
            out.append('<ul class="children mt-1 ml-2 space-y-0.5 border-l border-gray-200 pl-2">')
            for item in book.items:
                if isinstance(item, Chapter):
                    is_current_chap = current.get("chapter_slug") == item.slug
                    chap_href = link(item.url, from_url)
                    has_pages = bool(item.pages)
                    chap_open_cls = " open" if is_current_chap else ""
                    out.append(f'<li class="tree-node{chap_open_cls}">')
                    out.append('<div class="tree-row">')
                    if has_pages:
                        out.append(
                            f'<button type="button" class="chev" aria-label="Toggle pages">{_ion("chevron", "chev-icn")}</button>'
                        )
                    else:
                        out.append('<span class="chev-spacer"></span>')
                    out.append(_sidebar_link(chap_href, "chapter", item.title, is_current_chap, "py-1 flex-1"))
                    out.append("</div>")
                    if has_pages:
                        out.append('<ul class="children mt-0.5 ml-5 space-y-0.5 border-l border-gray-200 pl-2">')
                        for page in item.pages:
                            page_href = link(page.url, from_url)
                            is_current_page = current.get("page_url") == page.url
                            out.append("<li>")
                            out.append(_sidebar_link(page_href, "page", page.title, is_current_page, "py-0.5"))
                            out.append("</li>")
                        out.append("</ul>")
                    out.append("</li>")
                else:
                    page = item
                    page_href = link(page.url, from_url)
                    is_current_page = current.get("page_url") == page.url and current.get("chapter_slug") is None
                    out.append("<li>")
                    out.append(_sidebar_link(page_href, "page", page.title, is_current_page, "py-0.5"))
                    out.append("</li>")
            out.append("</ul>")
        out.append("</li>")
    out.append("</ul></nav>")
    return "\n".join(out)


def render_breadcrumbs(crumbs: list[tuple[str, str | None]]) -> str:
    """`crumbs` is a list of (label, href-or-None) from root to current."""
    parts = [
        '<nav class="text-sm text-gray-500 mb-4 flex flex-wrap items-center gap-x-1 gap-y-1" aria-label="Breadcrumb"><ol class="flex flex-wrap items-center gap-x-1">'
    ]
    for i, (label, href) in enumerate(crumbs):
        is_last = i == len(crumbs) - 1
        if i > 0:
            parts.append('<li class="text-gray-300 px-1">/</li>')
        if href and not is_last:
            parts.append(f'<li><a href="{_esc(href)}" class="hover:text-primary-600">{_esc(label)}</a></li>')
        else:
            parts.append(f'<li class="text-gray-700 font-medium" aria-current="page">{_esc(label)}</li>')
    parts.append("</ol></nav>")
    return "".join(parts)


LAYOUT = """<!doctype html>
<html lang="en" data-root="{root}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{site_title}">
{canonical_meta}
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{og_title}">
<meta name="twitter:description" content="{description}">
<script src="{root}assets/vendor/tailwind.js"></script>
<script>
tailwind.config = {{
  theme: {{
    extend: {{
      fontFamily: {{
        sans: ['Inter', 'ui-sans-serif', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'Helvetica Neue', 'Arial', 'sans-serif'],
        mono: ['"JetBrains Mono"', 'ui-monospace', 'SFMono-Regular', 'Menlo', 'Monaco', 'Consolas', 'monospace']
      }},
      colors: {{
        primary: {{
          50:  '#eff6fb',
          100: '#d6e8f3',
          200: '#aed1e7',
          300: '#7fb4d6',
          400: '#4f97c4',
          500: '#206ea7',
          600: '#1a5b8b',
          700: '#15496f',
          800: '#103857',
          900: '#0a273e'
        }}
      }}
    }}
  }}
}}
</script>
<link rel="stylesheet" href="{root}assets/vendor/fonts.css">
<link rel="stylesheet" href="{root}assets/highlight.css">
<link rel="stylesheet" href="{root}assets/vendor/katex/katex.min.css">
<script defer src="{root}assets/vendor/katex/katex.min.js"></script>
<script defer src="{root}assets/vendor/katex/auto-render.min.js"
  onload="renderMathInElement(document.body, {{
    delimiters: [
      {{left: '<math>', right: '</math>', display: false}},
      {{left: '$$', right: '$$', display: true}},
      {{left: '$', right: '$', display: false}},
      {{left: '\\\\(', right: '\\\\)', display: false}},
      {{left: '\\\\[', right: '\\\\]', display: true}},
      {{left: '\\\\begin{{equation}}', right: '\\\\end{{equation}}', display: true}},
      {{left: '\\\\begin{{align}}', right: '\\\\end{{align}}', display: true}},
      {{left: '\\\\begin{{align*}}', right: '\\\\end{{align*}}', display: true}},
      {{left: '\\\\begin{{alignat}}', right: '\\\\end{{alignat}}', display: true}},
      {{left: '\\\\begin{{gather}}', right: '\\\\end{{gather}}', display: true}},
      {{left: '\\\\begin{{split}}', right: '\\\\end{{split}}', display: true}}
    ],
    throwOnError: false
  }})"></script>
<style>
  :root {{ --primary: #206ea7; --primary-dark: #15496f; --chapter: #3b7a3a; --chapter-dark: #265120; }}
  html {{ font-size: 16px; }}
  body {{ background: #f2f2f3; }}

  /* Topbar */
  .topbar {{ background: var(--primary); color: #fff; box-shadow: 0 1px 2px rgba(0,0,0,0.1); }}
  .topbar a {{ color: #fff; }}
  .topbar a:hover {{ color: #d6e8f3; }}
  .topbar svg {{ font-size: 22px; }}

  /* Entity cards (used on book/chapter index pages) */
  .entity-card {{ display: flex; background: #fff; border-radius: 4px; border: 1px solid #e5e7eb; overflow: hidden; transition: box-shadow .15s ease, transform .15s ease; text-decoration: none; }}
  .entity-card:hover {{ box-shadow: 0 4px 12px rgba(0,0,0,0.08); transform: translateY(-1px); }}
  .entity-card .cover {{ flex: 0 0 72px; display: flex; align-items: center; justify-content: center; color: #fff; }}
  .entity-card .cover svg {{ font-size: 28px; }}
  .entity-card .cover.book {{ background: linear-gradient(135deg, #206ea7 0%, #15496f 100%); }}
  .entity-card .cover.chapter {{ background: linear-gradient(135deg, var(--chapter) 0%, var(--chapter-dark) 100%); }}
  .entity-card .cover.page {{ background: linear-gradient(135deg, #4f97c4 0%, #206ea7 100%); }}
  .entity-card .body {{ flex: 1 1 auto; padding: .9rem 1.1rem; min-width: 0; }}
  .entity-card .body .title {{ color: var(--primary-dark); font-weight: 600; font-size: 1.05rem; line-height: 1.3; }}
  .entity-card .body .desc {{ color: #6b7280; font-size: .9rem; margin-top: .2rem; line-height: 1.45; overflow: hidden; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; }}

  /* Sidebar */
  .sidebar a {{ display: flex; align-items: center; gap: .45rem; text-decoration: none; }}
  .sidebar .icn {{ flex: 0 0 16px; font-size: 16px; opacity: .6; }}
  .sidebar a.active .icn,
  .sidebar a:hover .icn {{ opacity: 1; }}
  .sidebar a.active svg[data-name="folder-outline"] {{ color: var(--chapter); }}
  .sidebar a.active svg[data-name="library-outline"],
  .sidebar a.active svg[data-name="document-text-outline"] {{ color: var(--primary); }}
  .sidebar .label {{ overflow: hidden; text-overflow: ellipsis; white-space: nowrap; min-width: 0; flex: 1 1 auto; }}
  .sidebar .label-book {{ white-space: normal; text-overflow: clip; overflow: visible; line-height: 1.25; }}
  .sidebar .tree-row > a {{ min-width: 0; }}

  /* Sidebar tree toggles (books and chapters) */
  .sidebar .tree-row {{ display: flex; align-items: center; gap: .25rem; }}
  .sidebar .chev {{ flex: 0 0 18px; width: 18px; height: 18px; display: flex; align-items: center; justify-content: center; color: #9ca3af; background: transparent; border: 0; padding: 0; cursor: pointer; border-radius: 3px; }}
  .sidebar .chev:hover {{ color: #4b5563; background: #f3f4f6; }}
  .sidebar .chev-icn {{ font-size: 14px; transition: transform .15s ease; }}
  .sidebar .tree-node.open > .tree-row .chev-icn {{ transform: rotate(90deg); }}
  .sidebar .chev-spacer {{ flex: 0 0 18px; width: 18px; }}
  .sidebar .tree-node > .children {{ display: none; }}
  .sidebar .tree-node.open > .children {{ display: block; }}

  /* Prose tweaks */
  .prose a {{ color: var(--primary); text-decoration: none; }}
  .prose a:hover {{ text-decoration: underline; }}
  .prose img {{ border-radius: 4px; border: 1px solid #e5e7eb; }}
  .prose code {{ background: #f4f4f5; padding: 0.1rem 0.35rem; border-radius: 3px; font-size: 0.9em; font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace; font-weight: 400; }}
  .prose code::before, .prose code::after {{ content: ''; }}
  .prose pre {{ background: #f8fafc; border: 1px solid #e5e7eb; color: #1f2937; }}
  .prose pre code {{ background: transparent; padding: 0; font-size: 0.9rem; }}
  .prose h1, .prose h2, .prose h3, .prose h4 {{ color: var(--primary-dark); }}
  .prose h2 {{ border-bottom: 1px solid #e5e7eb; padding-bottom: .25em; }}
  .prose blockquote {{ border-left-color: var(--primary); color: #4b5563; }}
  .prose table {{ font-size: 0.95em; }}
  .prose .table-wrap {{ overflow-x: auto; max-width: 100%; }}
  .prose .table-wrap > table {{ margin: 0; }}
  .prose th {{ background: #f8fafc; }}
  .prose hr {{ border-color: #e5e7eb; }}

  /* Collapsible details / solution boxes */
  .prose details {{ border: 1px solid #e5e7eb; border-left: 3px solid var(--primary); border-radius: 4px; background: #f8fafc; padding: .75rem .9rem; margin: 1.25em 0; }}
  .prose details > summary {{ list-style: none; cursor: pointer; margin: -.75rem -.9rem; padding: .65rem .9rem; font-weight: 600; color: var(--primary-dark); user-select: none; display: flex; align-items: center; gap: .5rem; }}
  .prose details > summary::-webkit-details-marker {{ display: none; }}
  .prose details > summary::before {{ content: "▶"; font-size: .7em; color: #9ca3af; transition: transform .15s ease; flex: 0 0 auto; }}
  .prose details[open] > summary::before {{ transform: rotate(90deg); }}
  .prose details[open] > summary {{ border-bottom: 1px solid #e5e7eb; margin-bottom: .75rem; }}
  .prose details > *:not(summary):first-of-type {{ margin-top: 0; }}
  .prose details > *:not(summary):last-child {{ margin-bottom: 0; }}

  /* KaTeX: keep wide formulas within the column on mobile */
  .katex-display {{ overflow-x: auto; overflow-y: hidden; padding: .25rem 0; max-width: 100%; }}
  .katex-display > .katex {{ white-space: nowrap; }}
  .prose .katex {{ max-width: 100%; }}

  /* Page heading */
  .page-heading {{ display: flex; align-items: center; gap: .7rem; }}
  .page-heading .heading-icon {{ flex: 0 0 36px; width: 36px; height: 36px; border-radius: 4px; display: flex; align-items: center; justify-content: center; color: #fff; }}
  .page-heading .heading-icon svg {{ font-size: 22px; }}

  /* Container width */
  .page-shell {{ max-width: 1440px; }}

  /* Search */
  .search-wrap {{ position: relative; flex: 1 1 auto; max-width: 480px; }}
  .search-wrap .search-icn {{ position: absolute; left: .65rem; top: 50%; transform: translateY(-50%); color: rgba(255,255,255,.7); display: flex; font-size: 18px; pointer-events: none; }}
  #search-input {{ width: 100%; height: 36px; padding: 0 .75rem 0 2.1rem; border-radius: 4px; border: 1px solid rgba(255,255,255,.25); background: rgba(255,255,255,.12); color: #fff; font-size: .95rem; outline: none; transition: background .15s ease, border-color .15s ease; }}
  #search-input::placeholder {{ color: rgba(255,255,255,.7); }}
  #search-input:focus {{ background: #fff; color: #1f2937; border-color: #fff; }}
  #search-input:focus + #search-results .search-icn {{ color: var(--primary); }}
  .search-wrap:focus-within .search-icn {{ color: var(--primary); }}

  .search-results {{ display: none; position: absolute; top: calc(100% + .35rem); left: 0; right: 0; background: #fff; border: 1px solid #e5e7eb; border-radius: 4px; box-shadow: 0 12px 32px rgba(0,0,0,0.12); z-index: 50; max-height: 70vh; overflow-y: auto; }}
  .search-results.open {{ display: block; }}
  .search-result {{ display: block; padding: .65rem .85rem; border-bottom: 1px solid #f1f5f9; text-decoration: none; color: inherit; }}
  .search-result:last-child {{ border-bottom: 0; }}
  .search-result:hover, .search-result.active {{ background: #eff6fb; }}
  .search-result .r-title {{ color: var(--primary-dark); font-weight: 600; font-size: .95rem; line-height: 1.3; }}
  .search-result .r-crumb {{ color: #6b7280; font-size: .75rem; margin-top: .15rem; }}
  .search-result .r-crumb .sep {{ color: #cbd5e1; margin: 0 .15rem; }}
  .search-result .r-snippet {{ color: #374151; font-size: .8rem; margin-top: .25rem; line-height: 1.45; overflow: hidden; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; }}
  .search-result mark {{ background: #fef9c3; color: inherit; padding: 0 1px; border-radius: 2px; }}
  .search-empty {{ padding: .85rem; color: #6b7280; font-size: .9rem; text-align: center; }}

  .search-toggle {{ display: none; align-items: center; justify-content: center; width: 36px; height: 36px; border-radius: 4px; color: #fff; background: transparent; border: 0; cursor: pointer; padding: 0; }}
  .search-toggle:hover {{ background: rgba(255,255,255,.12); }}
  .search-toggle svg {{ font-size: 22px; }}

  @media (max-width: 640px) {{
    .topbar-nav {{ display: none; }}
    .search-toggle {{ display: inline-flex; }}
    .topbar {{ position: relative; }}
    .search-wrap {{
      position: absolute; top: 100%; left: 0; right: 0; max-width: none;
      padding: .6rem .75rem; background: var(--primary);
      transform: translateY(-110%); transition: transform .2s ease;
      z-index: 30; box-shadow: 0 4px 12px rgba(0,0,0,.12);
    }}
    body.search-open .search-wrap {{ transform: translateY(0); }}
  }}

  /* Mobile sidebar drawer */
  .menu-toggle {{ display: none; align-items: center; justify-content: center; width: 36px; height: 36px; border-radius: 4px; color: #fff; background: transparent; border: 0; cursor: pointer; padding: 0; }}
  .menu-toggle:hover {{ background: rgba(255,255,255,.12); }}
  .menu-toggle svg {{ font-size: 24px; }}
  .menu-toggle .icn-close {{ display: none; }}
  body.menu-open .menu-toggle .icn-open {{ display: none; }}
  body.menu-open .menu-toggle .icn-close {{ display: inline-flex; }}
  .menu-backdrop {{ display: none; position: fixed; inset: 0; background: rgba(15,23,42,.45); z-index: 40; }}
  body.menu-open .menu-backdrop {{ display: block; }}
  @media (max-width: 1023px) {{
    .menu-toggle {{ display: inline-flex; }}
    .sidebar-col {{ position: fixed; top: 0; left: 0; bottom: 0; width: min(420px, 80vw); z-index: 50; transform: translateX(-100%); transition: transform .2s ease; padding: 1rem; overflow-y: auto; background: #f8fafc; box-shadow: 2px 0 16px rgba(0,0,0,.15); }}
    body.menu-open .sidebar-col {{ transform: translateX(0); }}
    .sidebar-col .sidebar {{ position: static; max-height: none; }}
  }}
  @media (max-width: 639px) {{
    .sidebar-col {{ width: 100vw; }}
  }}

  /* Prev / Next navigation */
  .prev-next {{ display: grid; grid-template-columns: 1fr 1fr; gap: .75rem; margin-top: 2.5rem; padding-top: 1.5rem; border-top: 1px solid #e5e7eb; }}
  .nav-card {{ display: flex; align-items: center; gap: .75rem; padding: .85rem 1rem; background: #fff; border: 1px solid #e5e7eb; border-radius: 4px; text-decoration: none; color: inherit; transition: box-shadow .15s ease, border-color .15s ease, transform .15s ease; min-width: 0; }}
  .nav-card:hover {{ border-color: var(--primary); box-shadow: 0 4px 12px rgba(0,0,0,0.06); transform: translateY(-1px); }}
  .nav-card.next {{ flex-direction: row; text-align: right; justify-content: flex-end; }}
  .nav-card .text {{ min-width: 0; flex: 1 1 auto; }}
  .nav-card.next .text {{ text-align: right; }}
  .nav-card .lbl {{ font-size: .7rem; text-transform: uppercase; letter-spacing: .05em; color: #6b7280; font-weight: 600; }}
  .nav-card .ttl {{ color: var(--primary-dark); font-weight: 500; font-size: .95rem; line-height: 1.3; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}
  .nav-card svg {{ font-size: 22px; color: var(--primary); flex: 0 0 22px; }}
  .nav-card-empty {{ display: block; }}
  @media (max-width: 640px) {{
    .prev-next {{ grid-template-columns: 1fr; }}
    .nav-card-empty {{ display: none; }}
  }}
</style>
</head>
<body class="text-gray-800 font-sans antialiased min-h-screen">
<header class="topbar">
  <div class="page-shell mx-auto px-4 sm:px-6 h-14 flex items-center justify-between gap-4">
    <button id="menu-toggle" class="menu-toggle shrink-0" type="button" aria-label="Toggle menu" aria-controls="sidebar-col" aria-expanded="false">
      <span class="icn-open">{menu_icon}</span>
      <span class="icn-close">{close_icon}</span>
    </button>
    <a href="{root}index.html" class="flex items-center gap-2 font-semibold text-lg shrink-0">
      {topbar_icon}
      <span class="topbar-title">{site_title}</span>
    </a>
    <div id="search-wrap" class="search-wrap">
      <span class="search-icn">{search_icon}</span>
      <input id="search-input" type="search" autocomplete="off" spellcheck="false"
             placeholder="Search…  (⌘K)" aria-label="Search">
      <div id="search-results" class="search-results" role="listbox"></div>
    </div>
    <button id="search-toggle" class="search-toggle shrink-0" type="button" aria-label="Toggle search" aria-controls="search-wrap" aria-expanded="false">
      {search_icon}
    </button>
    <nav class="topbar-nav text-sm flex items-center gap-4 shrink-0">
      <a href="{root}index.html" class="opacity-90 hover:opacity-100">Books</a>
    </nav>
  </div>
</header>
<div class="menu-backdrop" id="menu-backdrop"></div>
<div class="page-shell mx-auto px-4 sm:px-6 py-6 grid grid-cols-12 lg:grid-cols-[28%_1fr] gap-6">
  <aside id="sidebar-col" class="sidebar-col col-span-12 lg:col-auto">{sidebar}</aside>
  <main class="col-span-12 lg:col-auto">
    <article class="bg-white rounded-md border border-gray-200 shadow-sm p-6 sm:p-8">
      {breadcrumbs}
      <header class="mb-6">
        <div class="page-heading">
          {heading_icon}
          <h1 class="text-4xl font-bold text-primary-700 leading-tight m-0">{heading}</h1>
        </div>
        {meta_line}
      </header>
      <div class="prose prose-lg max-w-none">
        {content}
      </div>
    </article>
    <footer class="mt-6 text-xs text-gray-400 text-center">
      Source on <a href="https://github.com/paolobasso99/polimi-cs-notes" target="_blank" rel="noopener" class="hover:text-primary-600 underline">GitHub</a>.
    </footer>
  </main>
</div>
<script>
  document.addEventListener('click', function(e) {{
    var btn = e.target.closest('.sidebar .chev');
    if (!btn) return;
    e.preventDefault();
    btn.closest('.tree-node').classList.toggle('open');
  }});
  (function() {{
    var toggle = document.getElementById('menu-toggle');
    var backdrop = document.getElementById('menu-backdrop');
    var sidebar = document.getElementById('sidebar-col');
    function setOpen(open) {{
      document.body.classList.toggle('menu-open', open);
      if (toggle) toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    }}
    if (toggle) toggle.addEventListener('click', function() {{
      setOpen(!document.body.classList.contains('menu-open'));
    }});
    if (backdrop) backdrop.addEventListener('click', function() {{ setOpen(false); }});
    if (sidebar) sidebar.addEventListener('click', function(e) {{
      var a = e.target.closest('a');
      if (a && !e.target.closest('.chev')) setOpen(false);
    }});
    document.addEventListener('keydown', function(e) {{
      if (e.key === 'Escape' && document.body.classList.contains('menu-open')) setOpen(false);
    }});
  }})();
  (function() {{
    var btn = document.getElementById('search-toggle');
    var input = document.getElementById('search-input');
    if (!btn) return;
    function setOpen(open) {{
      document.body.classList.toggle('search-open', open);
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      if (open && input) setTimeout(function() {{ input.focus(); }}, 200);
    }}
    btn.addEventListener('click', function() {{
      setOpen(!document.body.classList.contains('search-open'));
    }});
    document.addEventListener('keydown', function(e) {{
      if (e.key === 'Escape' && document.body.classList.contains('search-open')) {{
        setOpen(false);
        if (input) input.blur();
      }}
    }});
  }})();
</script>
<script src="{root}assets/vendor/minisearch.min.js"></script>
<script defer src="{root}assets/search.js"></script>
</body>
</html>
"""


ION_NAMES = {
    "book": "library-outline",
    "chapter": "folder-outline",
    "page": "document-text-outline",
    "chevron": "chevron-forward-outline",
}


def _load_icons() -> dict[str, str]:
    out: dict[str, str] = {}
    if not ICONS_DIR.exists():
        return out
    for p in ICONS_DIR.glob("*.svg"):
        out[p.stem] = p.read_text(encoding="utf-8").strip()
    return out


_ICON_SVGS = _load_icons()


def _ion(kind: str, cls: str = "") -> str:
    name = ION_NAMES.get(kind, kind)
    svg = _ICON_SVGS.get(name)
    if not svg:
        return ""
    extra = f' class="{cls}"' if cls else ""
    return svg.replace(
        'class="ionicon"',
        f'data-name="{name}" width="1em" height="1em"{extra}',
        1,
    )


def _heading_icon(kind: str) -> str:
    if kind not in ION_NAMES:
        return ""
    bg = {"book": "#206ea7", "chapter": "#3b7a3a", "page": "#4f97c4"}[kind]
    return f'<span class="heading-icon" style="background:{bg}">{_ion(kind)}</span>'


def render_layout(
    *,
    title: str,
    heading: str,
    content_html: str,
    breadcrumbs_html: str,
    sidebar_html: str,
    root: str,
    meta_line: str = "",
    heading_icon: str = "",
    description: str = "",
    og_title: str = "",
    og_type: str = "article",
    page_url: str = "",
) -> str:
    desc = description or SITE_DESCRIPTION
    canonical_meta = ""
    if SITE_URL:
        href = f"{SITE_URL}/{page_url}" if page_url else f"{SITE_URL}/"
        canonical_meta = f'<link rel="canonical" href="{_esc(href)}">\n<meta property="og:url" content="{_esc(href)}">'
    return LAYOUT.format(
        title=_esc(title),
        site_title=_esc(SITE_TITLE),
        sidebar=sidebar_html,
        breadcrumbs=breadcrumbs_html,
        heading=_esc(heading),
        content=content_html,
        meta_line=meta_line,
        root=root,
        heading_icon=heading_icon,
        topbar_icon=_ion("book"),
        search_icon=_ion("search-outline"),
        menu_icon=_ion("menu-outline"),
        close_icon=_ion("close-outline"),
        description=_esc(desc),
        og_title=_esc(og_title or heading),
        og_type=_esc(og_type),
        canonical_meta=canonical_meta,
    )


def _meta_line(meta: dict[str, Any]) -> str:
    updated = meta.get("updated_at")
    if not updated:
        return ""
    try:
        dt = datetime.fromisoformat(str(updated).replace("Z", "+00:00"))
        when = dt.strftime("%b %d, %Y")
    except Exception:
        when = str(updated)
    return f'<p class="text-sm text-gray-500 mt-1">Updated {_esc(when)}</p>'


# ---------- page renderers ------------------------------------------------- #


def _snippet(html_text: str, n: int = 180) -> str:
    s = re.sub(r"<[^>]+>", " ", html_text)
    s = re.sub(r"\s+", " ", s).strip()
    if len(s) > n:
        s = s[:n].rsplit(" ", 1)[0] + "…"
    return s


def _entity_card(href: str, kind: str, title: str, desc: str) -> str:
    desc_html = f'<div class="desc">{_esc(desc)}</div>' if desc else ""
    return (
        f'<a href="{_esc(href)}" class="entity-card">'
        f'<div class="cover {kind}">{_ion(kind)}</div>'
        f'<div class="body"><div class="title">{_esc(title)}</div>{desc_html}</div>'
        f"</a>"
    )


def render_index(books: list[Book]) -> str:
    sidebar = render_sidebar(books, current={}, from_url="index.html")
    breadcrumbs = render_breadcrumbs([(SITE_TITLE, None)])

    parts = [
        '<p class="lead">'
        'These are notes from <a href="https://github.com/paolobasso99" target="_blank" rel="noopener">Paolo Basso</a> '
        "of some of the courses taken at the Master of Computer Science and Engineering "
        "at Politecnico di Milano in 2021-2023. "
        'Source on <a href="https://github.com/paolobasso99/polimi-cs-notes" target="_blank" rel="noopener">GitHub</a>.'
        "</p>"
    ]
    parts.append('<h2 class="!mt-8 !mb-3">Books</h2>')
    parts.append('<div class="grid sm:grid-cols-2 gap-3 not-prose">')
    for book in books:
        href = link(book.url, "index.html")
        desc_html = render_markdown(book.description_body, book.url)
        parts.append(_entity_card(href, "book", book.title, _snippet(desc_html)))
    parts.append("</div>")

    return render_layout(
        title=SITE_TITLE,
        heading=SITE_TITLE,
        content_html="".join(parts),
        breadcrumbs_html=breadcrumbs,
        sidebar_html=sidebar,
        root="",
        heading_icon=_heading_icon("book"),
        description=SITE_DESCRIPTION,
        og_title=SITE_TITLE,
        og_type="website",
        page_url="index.html",
    )


def render_book_index(book: Book, books: list[Book]) -> str:
    from_url = book.url
    sidebar = render_sidebar(books, current={"book_slug": book.slug}, from_url=from_url)
    crumbs = [(SITE_TITLE, link("index.html", from_url)), (book.title, None)]
    breadcrumbs = render_breadcrumbs(crumbs)

    body_html = render_markdown(book.description_body, from_url)

    cards = ['<h2 class="!mt-8 !mb-3">Contents</h2>', '<div class="flex flex-col gap-3 not-prose">']
    for item in book.items:
        href = link(item.url, from_url)
        if isinstance(item, Chapter):
            desc_html = render_markdown(item.description_body, from_url)
            page_count = len(item.pages)
            preview = _snippet(desc_html, 200) or (
                f"{page_count} page{'s' if page_count != 1 else ''}" if page_count else ""
            )
            cards.append(_entity_card(href, "chapter", item.title, preview))
        else:
            page = item
            cards.append(_entity_card(href, "page", page.title, _snippet(render_markdown(page.body, from_url), 200)))
    cards.append("</div>")

    content = body_html + "\n" + "".join(cards)

    book_desc = _snippet(body_html, 200) or f"Notes for {book.title}."
    return render_layout(
        title=f"{book.title} — {SITE_TITLE}",
        heading=book.title,
        content_html=content,
        breadcrumbs_html=breadcrumbs,
        sidebar_html=sidebar,
        root=root_prefix(from_url),
        meta_line=_meta_line(book.description_meta),
        heading_icon=_heading_icon("book"),
        description=book_desc,
        og_title=book.title,
        page_url=from_url,
    )


def render_chapter_index(book: Book, chapter: Chapter, books: list[Book]) -> str:
    from_url = chapter.url
    sidebar = render_sidebar(books, current={"book_slug": book.slug, "chapter_slug": chapter.slug}, from_url=from_url)
    crumbs = [
        (SITE_TITLE, link("index.html", from_url)),
        (book.title, link(book.url, from_url)),
        (chapter.title, None),
    ]
    breadcrumbs = render_breadcrumbs(crumbs)

    body_html = render_markdown(chapter.description_body, from_url)

    cards = ['<h2 class="!mt-8 !mb-3">Pages</h2>', '<div class="flex flex-col gap-3 not-prose">']
    for p in chapter.pages:
        cards.append(
            _entity_card(link(p.url, from_url), "page", p.title, _snippet(render_markdown(p.body, from_url), 200))
        )
    cards.append("</div>")

    prev_it, next_it = _prev_next_for(book, chapter.url)
    nav_html = _render_prev_next(prev_it, next_it, from_url)

    chap_desc = _snippet(body_html, 200) or f"{chapter.title} — {book.title}."
    return render_layout(
        title=f"{chapter.title} — {book.title}",
        heading=chapter.title,
        content_html=body_html + "\n" + "".join(cards) + nav_html,
        breadcrumbs_html=breadcrumbs,
        sidebar_html=sidebar,
        root=root_prefix(from_url),
        meta_line=_meta_line(chapter.description_meta),
        heading_icon=_heading_icon("chapter"),
        description=chap_desc,
        og_title=chapter.title,
        page_url=from_url,
    )


def _book_nav_items(book: Book) -> list[BookItem]:
    """Flat list of nav targets in display order: chapter index pages + leaf pages."""
    items: list[BookItem] = []
    for it in book.items:
        if isinstance(it, Chapter):
            items.append(it)
            items.extend(it.pages)
        else:
            items.append(it)
    return items


def _prev_next_for(book: Book, current_url: str) -> tuple[BookItem | None, BookItem | None]:
    items = _book_nav_items(book)
    idx = next((i for i, it in enumerate(items) if it.url == current_url), None)
    if idx is None:
        return None, None
    prev_it = items[idx - 1] if idx > 0 else None
    next_it = items[idx + 1] if idx + 1 < len(items) else None
    return prev_it, next_it


def _render_prev_next(prev_it: BookItem | None, next_it: BookItem | None, from_url: str) -> str:
    if not prev_it and not next_it:
        return ""
    parts = ['<nav class="prev-next not-prose">']
    if prev_it:
        parts.append(
            f'<a href="{_esc(link(prev_it.url, from_url))}" class="nav-card prev">'
            f"{_ion('arrow-back-outline')}"
            f'<div class="text"><div class="lbl">Previous</div>'
            f'<div class="ttl">{_esc(prev_it.title)}</div></div>'
            f"</a>"
        )
    else:
        parts.append('<span class="nav-card-empty"></span>')
    if next_it:
        parts.append(
            f'<a href="{_esc(link(next_it.url, from_url))}" class="nav-card next">'
            f'<div class="text"><div class="lbl">Next</div>'
            f'<div class="ttl">{_esc(next_it.title)}</div></div>'
            f"{_ion('arrow-forward-outline')}"
            f"</a>"
        )
    else:
        parts.append('<span class="nav-card-empty"></span>')
    parts.append("</nav>")
    return "".join(parts)


def render_page(book: Book, chapter: Chapter | None, page: Page, books: list[Book]) -> str:
    from_url = page.url
    sidebar = render_sidebar(
        books,
        current={
            "book_slug": book.slug,
            "chapter_slug": chapter.slug if chapter else None,
            "page_url": page.url,
        },
        from_url=from_url,
    )
    crumbs: list[tuple[str, str | None]] = [
        (SITE_TITLE, link("index.html", from_url)),
        (book.title, link(book.url, from_url)),
    ]
    if chapter:
        crumbs.append((chapter.title, link(chapter.url, from_url)))
    crumbs.append((page.title, None))
    breadcrumbs = render_breadcrumbs(crumbs)

    body_html = render_markdown(page.body, from_url)

    prev_it, next_it = _prev_next_for(book, page.url)
    nav_html = _render_prev_next(prev_it, next_it, from_url)

    page_desc = _snippet(body_html, 200) or f"{page.title} — {book.title}."
    return render_layout(
        title=f"{page.title} — {book.title}",
        heading=page.title,
        content_html=body_html + nav_html,
        breadcrumbs_html=breadcrumbs,
        sidebar_html=sidebar,
        root=root_prefix(from_url),
        meta_line=_meta_line(page.meta),
        heading_icon=_heading_icon("page"),
        description=page_desc,
        og_title=page.title,
        page_url=from_url,
    )


# ---------- assets --------------------------------------------------------- #


def _index_text(html_text: str) -> str:
    s = re.sub(r"<[^>]+>", " ", html_text)
    return re.sub(r"\s+", " ", s).strip()


def build_search_index(books: list[Book]) -> list[dict[str, str]]:
    docs: list[dict[str, str]] = []
    for book in books:
        docs.append(
            {
                "id": book.url,
                "url": book.url,
                "title": book.title,
                "book": book.title,
                "chapter": "",
                "body": _index_text(render_markdown(book.description_body, book.url)),
            }
        )
        for item in book.items:
            if isinstance(item, Chapter):
                docs.append(
                    {
                        "id": item.url,
                        "url": item.url,
                        "title": item.title,
                        "book": book.title,
                        "chapter": item.title,
                        "body": _index_text(render_markdown(item.description_body, item.url)),
                    }
                )
                for page in item.pages:
                    docs.append(
                        {
                            "id": page.url,
                            "url": page.url,
                            "title": page.title,
                            "book": book.title,
                            "chapter": item.title,
                            "body": _index_text(render_markdown(page.body, page.url)),
                        }
                    )
            else:
                page = item
                docs.append(
                    {
                        "id": page.url,
                        "url": page.url,
                        "title": page.title,
                        "book": book.title,
                        "chapter": "",
                        "body": _index_text(render_markdown(page.body, page.url)),
                    }
                )
    return docs


def write_pygments_css(out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    css: str = HtmlFormatter(style="friendly").get_style_defs(".highlight")  # type: ignore[no-untyped-call]
    extra = (
        ".highlight { background: #f8fafc; border-radius: 4px; padding: 0.75rem 1rem; "
        "overflow-x: auto; font-size: 0.9rem; }\n"
    )
    (out_dir / "highlight.css").write_text(extra + css)


def _copy_local_assets_for_md(md_path: Path, out_path: Path) -> None:
    """Copy files referenced via relative paths from this markdown into the site.

    Resolves each `![](...)` / `[..](...)` target relative to the md file,
    figures out where it should live in site/, and copies it. Only handles
    paths that resolve inside CONTENT_DIR.
    """
    try:
        text = md_path.read_text(encoding="utf-8")
    except Exception:
        return
    refs = set()
    for m in re.finditer(r"!\[[^\]]*\]\(([^)\s]+)", text):
        refs.add(m.group(1))
    for m in re.finditer(r"(?<!\!)\[[^\]]*\]\(([^)\s]+)", text):
        refs.add(m.group(1))
    for m in re.finditer(r"""<img\b[^>]*?\bsrc=["']([^"']+)["']""", text, re.IGNORECASE):
        refs.add(m.group(1))

    for ref in refs:
        if ref.startswith(("http://", "https://", "#", "mailto:")):
            continue
        if ref.endswith(".md"):
            continue  # rendered as html elsewhere
        src = (md_path.parent / ref).resolve()
        try:
            src.relative_to(CONTENT_DIR.resolve())
        except ValueError:
            continue
        if not src.is_file():
            continue
        rel = os.path.relpath(src, CONTENT_DIR)
        dest = SITE_DIR / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)


# ---------- driver --------------------------------------------------------- #


def write_html(out_path: Path, content: str) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(content, encoding="utf-8")


def build() -> None:
    if not BOOKS_DIR.exists():
        sys.exit(f"No content found at {BOOKS_DIR}. Run export.py first.")

    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)
    SITE_DIR.mkdir(parents=True)

    books = load_books()
    if not books:
        sys.exit("No books found under content/books/.")

    write_pygments_css(SITE_DIR / "assets")
    if VENDOR_DIR.exists():
        shutil.copytree(VENDOR_DIR, SITE_DIR / "assets" / "vendor")
    else:
        print("warning: assets/vendor/ missing — run `poetry run python vendor.py` first.")
    search_js = ROOT / "assets" / "search.js"
    if search_js.exists():
        shutil.copy2(search_js, SITE_DIR / "assets" / "search.js")
    (SITE_DIR / ".nojekyll").write_text("")

    (SITE_DIR / "search.json").write_text(
        json.dumps(build_search_index(books), ensure_ascii=False),
        encoding="utf-8",
    )

    # Index
    write_html(SITE_DIR / "index.html", render_index(books))

    # Books / chapters / pages
    for book in books:
        write_html(SITE_DIR / book.url, render_book_index(book, books))
        for item in book.items:
            if isinstance(item, Chapter):
                write_html(SITE_DIR / item.url, render_chapter_index(book, item, books))
                for page in item.pages:
                    write_html(SITE_DIR / page.url, render_page(book, item, page, books))
                # copy assets referenced by chapter description and pages
                _copy_local_assets_for_md(
                    BOOKS_DIR / book.slug / item.slug / "_chapter.md",
                    SITE_DIR / item.url,
                )
                for page in item.pages:
                    _copy_local_assets_for_md(page.md_path, SITE_DIR / page.url)
            else:
                page = item
                write_html(SITE_DIR / page.url, render_page(book, None, page, books))
                _copy_local_assets_for_md(page.md_path, SITE_DIR / page.url)

        _copy_local_assets_for_md(BOOKS_DIR / book.slug / "_book.md", SITE_DIR / book.url)

    print(f"site built at {SITE_DIR}")


if __name__ == "__main__":
    build()
