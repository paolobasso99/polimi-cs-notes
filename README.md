# polimi-cs-notes

> 📚 **Read the notes online: [bookstack.bassopaolo.com](https://bookstack.bassopaolo.com/)**

My notes from the Computer Science and Engineering Master's at Politecnico
di Milano (2021–2023).

I used to keep them in a self-hosted [BookStack](https://github.com/BookStackApp/BookStack)
instance, but I decided to stop running the server. To avoid losing the
content, I exported everything to markdown and built this static site so
the notes can live on GitHub Pages instead — published at
**<https://bookstack.bassopaolo.com/>**.

The rest of this README documents the export/build pipeline that was
written for that migration — useful if you want to do the same with your
own BookStack instance.

Built with [Claude Code](https://claude.com/claude-code) (Opus 4.7).

## Pipeline

Export a [BookStack](https://www.bookstackapp.com/) instance to a markdown
tree, then build a static HTML site (Tailwind, BookStack-ish styling) ready
for GitHub Pages.

```
BookStack  ──(export.py)──►  content/  ──(build.py)──►  site/
                              (editable                  (deployable
                               markdown)                  static HTML)
```

`content/` is the source of truth after the initial export — edit it freely
and re-run `build.py` to regenerate the site.

## Setup

Dependencies are managed with [Poetry](https://python-poetry.org/).

```bash
poetry install
cp .env.example .env
```

Run commands inside the Poetry environment with `poetry run …` (e.g. `poetry run python export.py`), or open a shell with `poetry shell`.

Edit `.env` and fill in:

- `BOOKSTACK_BASE_URL` — e.g. `https://bookstack.example.com`
- `BOOKSTACK_TOKEN_ID` and `BOOKSTACK_TOKEN_SECRET` — create from your
  BookStack profile → *API Tokens*. The token must belong to a user with
  read access to every book you want to export.
- `SITE_TITLE` — shown in the header and `<title>` (optional).
- `SITE_BASE_PATH` — reserved for future use; currently the build uses
  fully relative URLs and works under any path.

## Export

```bash
poetry run python export.py
```

Walks every book → chapter → page and writes:

```
content/
  books/
    <book-slug>/
      _book.md                  # book description + frontmatter
      <page-slug>.md            # pages directly under the book
      <chapter-slug>/
        _chapter.md             # chapter description + frontmatter
        <page-slug>.md
  images/
    <hash>_<original-name>      # deduped by URL hash
```

Each markdown file has YAML frontmatter (`title`, `slug`, `priority`,
`id`, timestamps). Images embedded in pages are downloaded and rewritten
to relative paths, so the markdown stays portable.

The script is idempotent — re-running it overwrites pages but reuses
already-downloaded images. Drafts are skipped.

## Edit

Edit any `.md` file under `content/` with your favourite editor. Common
changes:

- **Reorder** — adjust `priority` in frontmatter (lower = earlier).
- **Rename** — change `title` in frontmatter; the filename becomes the URL
  slug.
- **Move** — drag a `.md` file between book/chapter folders. Update any
  relative image paths if they break.
- **Add a page** — drop a new `.md` file with at least
  `title:` frontmatter into the relevant folder.
- **Add a chapter** — create a folder, optionally with a `_chapter.md`
  for its description.

## Build

```bash
poetry run python build.py
```

Generates `site/`:

```
site/
  index.html                    # list of books
  books/<book>/index.html       # book home (description + TOC)
  books/<book>/<chapter>/index.html
  books/<book>/.../<page>.html
  images/                       # mirrored from content/images
  assets/highlight.css          # Pygments theme for code blocks
  .nojekyll                     # disables Jekyll on GitHub Pages
```

`site/` is wiped and rebuilt on every run.

## Deploy to GitHub Pages

1. Create a GitHub repository and push this project.
2. In *Settings → Pages*, choose either:
   - **GitHub Actions** with a workflow that uploads `site/` as the Pages
     artifact, or
   - **Deploy from a branch** — push the contents of `site/` to a `gh-pages`
     branch, e.g.:
     ```bash
     poetry run python build.py
     cd site
     git init && git checkout -b gh-pages
     git add . && git commit -m "publish"
     git remote add origin <your-repo-url>
     git push -f origin gh-pages
     ```
3. If you use a project page (`https://<user>.github.io/<repo>/`) the
   site works as-is — all internal links are relative.

## Styling

Tailwind is loaded via the Play CDN with the typography plugin. Colours
are tuned to match BookStack's primary blue (`#206ea7`); fonts use Source
Sans Pro. Code blocks are styled with a Pygments stylesheet generated at
build time (`site/assets/highlight.css`). Tweak the inline `tailwind.config`
or the `<style>` block in `build.py` to adjust.

## Files

- `export.py` — BookStack API → `content/`
- `build.py` — `content/` → `site/`
- `pyproject.toml` / `poetry.lock` — Python dependencies (Poetry)
- `.env.example` — environment template
