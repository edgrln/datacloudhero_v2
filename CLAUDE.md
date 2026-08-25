# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A [Pelican](https://getpelican.com) (Python static site generator) project for **datacloudhero.com**. Content is written in Markdown, rendered through a custom theme (`themes/mytheme`), and the built `output/` is deployed as a static site.

The site has two independent parts that never share templates:
- **Site root** (`/`) — a single self-contained static HTML landing page, hand-authored, not run through Pelican's theme/Jinja pipeline at all.
- **`/blog/`** — everything Pelican actually generates (articles, tags, categories, authors, search index) via `themes/mytheme`.

## Commands

```bash
pip install -r requirements.txt      # pelican, markdown — the only real deps

make html        # one-off build with pelicanconf.py -> output/
make devserver   # build + watch + serve at http://localhost:8000 (edit-reload loop)
make serve       # serve an already-built output/ without regenerating
make publish     # production build with publishconf.py -> output/ (absolute URLs, feeds on)
make clean       # rm -rf output/

# equivalent raw commands (what devserver/publish wrap):
pelican content -o output -s pelicanconf.py    # dev config, SITEURL=""
pelican content -o output -s publishconf.py    # prod config, SITEURL="https://datacloudhero.com"
```

There is no lint/test suite in this repo. `DELETE_OUTPUT_DIRECTORY = True`, so `output/` is wiped and fully regenerated on every build — never hand-edit files under `output/`, they don't survive the next build.

Deployment is automatic: `.github/workflows/gh-pages.yml` runs `pelican content -o output -s publishconf.py` on every push to `main`/`master` and publishes `output/` to GitHub Pages. `make github` (local `ghp-import` to a `gh-pages` branch) is an older/alternate path defined in the Makefile but not what CI uses.

## Architecture

### URL scheme is centralized in `pelicanconf.py`

Every content type is deliberately routed under `blog/...` (`ARTICLE_URL`, `ARTICLE_SAVE_AS`, `TAG_URL`, `CATEGORY_URL`, `AUTHOR_URL`, `INDEX_SAVE_AS`, etc. are all overridden away from Pelican's defaults). The site root path is reserved for the static landing page. When adding any new content type/URL, follow this `blog/{...}` convention rather than Pelican's defaults.

### The landing page bypasses Pelican's templates

`content/extra/index.html` is copied verbatim to `output/index.html` via `STATIC_PATHS` + `EXTRA_PATH_METADATA` (not the `PAGES` mechanism — `ARTICLE_EXCLUDES`/`PAGE_EXCLUDES = ['extra']` keep the content readers from also trying to parse it). It's a fully standalone HTML file with its own inline `<style>`, Tailwind CDN, and Google Fonts — it does **not** extend `themes/mytheme/templates/base.html`. Any change to nav/branding/assets on the landing page has to be made directly in that file; it will not pick up changes made to the theme templates.

Because it's standalone, asset paths inside it are easy to get wrong: theme static files (logo, favicon, social-card) live under `theme/img/...` in the built output (see below), not `img/...` — a past bug was the landing page linking to the wrong prefix.

### Theme structure (`themes/mytheme/`)

- `templates/base.html` — full HTML shell (nav, search widget, theme toggle, footer, global `<script>` blocks) used by every Pelican-rendered page.
- `templates/blog_base.html` — extends `base.html`, adds the year-grouped sidebar of all posts; everything under `/blog/` extends this, not `base.html` directly.
- `templates/article.html`, `page.html`, `category.html`, `tag.html`, `author.html`, `authors.html`, `archives.html`, `index.html`, `404.html` — extend `blog_base.html`.
- `templates/partials/` — small includes pulled into article pages: `author_card.html`, `cta.html` (driven by the `CTA_*` settings in `pelicanconf.py`), `ai_actions.html` (see below).
- `templates/search.html` — a `DIRECT_TEMPLATES` entry; the site has no server-side search, it's Alpine-less vanilla JS (in `base.html`) that fetches `blog/search-index.json` (generated via `SEARCH_SAVE_AS`/`SEARCH_URL`) and filters client-side.
- `static/img/` — `favicon.ico`, `logo.svg`, `social-card.png`. Pelican copies this whole tree to `output/theme/...`, so **any reference to these assets — including from the standalone landing page — must use the `theme/img/...` prefix**, not `img/...`.
- `static/css/style.css` — single stylesheet; Bootstrap 5 (via CDN in `base.html`) supplies the base, this file layers a small `:root` accent-color override plus component-specific classes (`.sidebar-*`, `.author-*`, `.search-*`, `.tag-pill`, `.cta-box`, `.ai-actions`, ...).

### Content authoring

Markdown files in `content/` (flat, not `content/articles/`). Metadata is the classic Pelican `Key: value` header block terminated by a blank line (`Title`, `Date`, `Category`, `Author`, `Tags`, `Summary`). `AUTHORS_INFO` in `pelicanconf.py` maps author names to avatar/title/social links used by `author_card.html` — a new author must be added there, not just in the article's `Author:` field, or the card renders without the extra info.

### Generated machine-readable mirrors (`pelicanconf.py`, bottom half)

Two custom generators are wired up via `pelican.signals.article_generator_finalized` directly inside `pelicanconf.py` (no separate plugin package/folder — this project doesn't use `pelican-plugins`):

- `_write_markdown_mirrors` — for every article `blog/{slug}/index.html`, also writes a sibling `blog/{slug}.md` containing the raw Markdown body (metadata block stripped) plus a short source/date header. This is what the "Copy page as Markdown" article button and `llms.txt` links point at.
- `_write_llms_txt` — writes `output/llms.txt` at the site root, following the [llmstxt.org](https://llmstxt.org) format (`# title`, `> summary`, `## Blog` section with `- [title](md_url): desc` entries), listing every article's `.md` mirror.

Both run automatically on every build (dev and publish) — no extra command needed. If article URL/save-as conventions in `pelicanconf.py` change, the `_os.path.dirname(article.save_as) + '.md'` path derivation in both functions needs to change with them.

### `ai_actions.html` partial

Renders a per-article dropdown ("Copy page as Markdown" / "View as Markdown" / "Open in ChatGPT" / "Open in Claude" / "Open in Perplexity"), included from `article.html`. The clipboard-copy behavior is a delegated click handler in `base.html` (`.js-copy-markdown`), not in the partial itself — keep the two in sync if either is renamed. The ChatGPT/Claude/Perplexity links only pre-fill a prompt referencing the article's `.md` URL; they don't guarantee the target service fetches it (depends on that service's browsing being enabled).
