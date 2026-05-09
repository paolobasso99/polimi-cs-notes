"""Download external CDN assets to assets/vendor/ for offline / archival use.

Run once after adding/updating CDN dependencies. Re-run to refresh versions.
After running this, build.py uses the local copies and makes no external requests.

Layout:
  assets/vendor/tailwind.js          — Tailwind Play CDN (JIT + typography plugin)
  assets/vendor/fonts.css            — Google Fonts CSS, rewritten to use local woff2
  assets/vendor/fonts/*.woff2        — font files
  assets/vendor/katex/katex.min.css  — KaTeX CSS
  assets/vendor/katex/fonts/*.woff2  — KaTeX fonts
  assets/vendor/katex/*.js           — KaTeX core + auto-render
  assets/vendor/icons/*.svg          — Ionicons SVGs we use, inlined at build time
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
VENDOR = ROOT / "assets" / "vendor"

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)


def fetch(url: str, *, binary: bool = False):
    req = Request(url, headers={"User-Agent": UA})
    with urlopen(req) as r:
        data = r.read()
    return data if binary else data.decode("utf-8")


def write(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(data, bytes):
        path.write_bytes(data)
    else:
        path.write_text(data, encoding="utf-8")
    rel = path.relative_to(ROOT)
    size = path.stat().st_size
    print(f"  {rel}  ({size:,} bytes)")


def vendor_tailwind() -> None:
    print("Tailwind Play CDN (JIT + typography plugin)…")
    js = fetch("https://cdn.tailwindcss.com?plugins=typography")
    write(VENDOR / "tailwind.js", js)


def vendor_fonts() -> None:
    print("Google Fonts: Inter + JetBrains Mono…")
    css = fetch(
        "https://fonts.googleapis.com/css2"
        "?family=Inter:wght@400;500;600;700"
        "&family=JetBrains+Mono:wght@400;500"
        "&display=swap"
    )
    out = css
    for url in re.findall(r"url\((https://fonts\.gstatic\.com/[^)]+)\)", css):
        data = fetch(url, binary=True)
        fname = url.rsplit("/", 1)[-1]
        write(VENDOR / "fonts" / fname, data)
        out = out.replace(url, f"./fonts/{fname}")
    write(VENDOR / "fonts.css", out)


def vendor_katex() -> None:
    print("KaTeX 0.15.1 …")
    base = "https://cdn.jsdelivr.net/npm/katex@0.15.1/dist"
    css = fetch(f"{base}/katex.min.css")
    # Font urls inside katex.min.css are relative paths like "fonts/KaTeX_AMS-Regular.woff2"
    for ref in re.findall(r"url\(([^)]+)\)", css):
        ref = ref.strip("\"'")
        if ref.startswith("data:"):
            continue
        full = f"{base}/{ref}"
        data = fetch(full, binary=True)
        write(VENDOR / "katex" / ref, data)
    write(VENDOR / "katex" / "katex.min.css", css)
    write(VENDOR / "katex" / "katex.min.js", fetch(f"{base}/katex.min.js"))
    write(VENDOR / "katex" / "auto-render.min.js", fetch(f"{base}/contrib/auto-render.min.js"))


def vendor_minisearch() -> None:
    print("MiniSearch (client-side search) …")
    js = fetch("https://cdn.jsdelivr.net/npm/minisearch@7.1.2/dist/umd/index.min.js")
    write(VENDOR / "minisearch.min.js", js)


def vendor_icons() -> None:
    print("Ionicons SVGs (inlined at build time)…")
    icons = [
        "library-outline",
        "folder-outline",
        "document-text-outline",
        "chevron-forward-outline",
        "arrow-back-outline",
        "arrow-forward-outline",
        "search-outline",
        "close-outline",
        "menu-outline",
    ]
    base = "https://cdn.jsdelivr.net/npm/ionicons@7.1.0/dist/svg"
    for name in icons:
        svg = fetch(f"{base}/{name}.svg")
        write(VENDOR / "icons" / f"{name}.svg", svg)


def main() -> None:
    VENDOR.mkdir(parents=True, exist_ok=True)
    vendor_tailwind()
    vendor_fonts()
    vendor_katex()
    vendor_minisearch()
    vendor_icons()
    print("\nDone. assets/vendor/ is populated; build.py will use local copies.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        sys.exit(f"vendor failed: {e}")
