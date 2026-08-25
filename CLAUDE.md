# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**Keep this file current as you work.** Whenever a change adds or alters a build-time convention future work would need to know about — a new signal-based generator in `pelicanconf.py`, a new `PLUGINS`/`STATIC_PATHS`/`EXTRA_PATH_METADATA` entry, a new dependency, a new template/partial wiring pattern — update the relevant section here (or add one) in the same change, not as a separate follow-up. Don't wait to be asked.

## What this is

A [Pelican](https://getpelican.com) (Python static site generator) project for **datacloudhero.com**. Content is written in Markdown, rendered through a custom theme (`themes/mytheme`), and the built `output/` is deployed as a static site.

The site has two independent parts that never share templates:
- **Site root** (`/`) — a Pelican `Page` rendered through its own standalone template (`landing.html`), hand-authored, entirely separate from the blog's Bootstrap theme (see below).
- **`/blog/`** — everything else Pelican generates (articles, tags, categories, authors, search index) via `themes/mytheme`.

## Commands

```bash
pip install -r requirements.txt      # pelican, markdown, pelican-sitemap — the only real deps

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

### The landing page is a real Page, but with its own document shell

The landing page is a real Pelican `Page` (`content/pages/landing.html` + `themes/mytheme/templates/landing.html`), but it deliberately does **not** extend `themes/mytheme/templates/base.html` — it has an entirely different visual identity (dark hero, Tailwind CDN utility classes, Alpine.js interactivity, Google Fonts) from the Bootstrap-based blog theme, so it carries its own full `<head>`/`<body>` shell instead.

The split, and why it's shaped this way: Pelican's built-in `HTMLReader` (used for `.html` content files) only extracts `<title>` and `<meta name="...">` from `<head>`, and everything between `<body>`/`</body>` — it silently drops everything else in `<head>` (so raw `<style>` blocks, CDN `<script src>` tags, font links can't live in the content file) and it discards attributes on the `<body>` tag itself (so anything that has to be on `<body>`, like Alpine's root `x-data`/`x-init` scope, can't live in the content file either). Given that:
- `themes/mytheme/templates/landing.html` holds the whole document shell: `<head>` (Tailwind CDN, Alpine.js, Google Fonts, the custom `<style>` blocks, OG/Twitter meta), the `<body class="grid-bg" x-data="{...}" x-init="...">` opening tag (this is where the page's Alpine root scope - menu state, contact form, reveal-on-scroll - lives), then `{{ page.content|safe }}`, then the trailing footer `<script>` tags before `</body></html>`.
- `content/pages/landing.html` holds just what used to be *inside* `<body>` (nav, hero, services, stack, process, contact modal, FAQ), plus a small metadata `<head>` using Pelican's HTML-page convention (`<meta name="save_as" content="index.html">`, `<meta name="url" content="">`, `<meta name="template" content="landing">`) to route it to `output/index.html` via the `landing` template instead of the blog's default `PAGE_URL`/`PAGE_SAVE_AS` pattern.

`ARTICLE_EXCLUDES` includes `'pages'` for a non-obvious reason: `ARTICLE_PATHS` defaults to `[""]`, so Pelican's `ArticlesGenerator` walks *all* of `content/`, including `content/pages/` — without the exclude, `landing.html` gets picked up as both an Article and a Page and they race to write `output/index.html`.

Because the landing template is standalone, asset paths inside it are easy to get wrong: theme static files (logo, favicon, social-card) live under `theme/img/...` in the built output (see below), not `img/...` — a past bug was the landing page linking to the wrong prefix.

Two more root-level files ride along via `STATIC_PATHS`/`EXTRA_PATH_METADATA` (unrelated to the Page above — these are still verbatim-copied static files, not Pelican content):
- `content/extra/favicon.ico` — a duplicate of `themes/mytheme/static/img/favicon.ico`, kept only so `/favicon.ico` exists at the domain root (browsers fall back to fetching that path for tabs with no `<link rel="icon">` to read, e.g. the raw-text `blog/{slug}.md` mirrors below).
- `content/extra/index.md` — a **hand-written** Markdown summary of the landing page (services, stack, process, contact), linked from `llms.txt`. It is *not* auto-derived from `content/pages/landing.html`: that page has no clean text to extract (nav/tech-stack markup is legitimately duplicated for responsive/marquee reasons, the contact email is Cloudflare-obfuscated in the source, and the FAQ copy only exists inside an Alpine `x-for="... in [...]"` JS array, invisible to any HTML→text pass). Update it by hand when the pitch changes materially.

The landing page's contact `mailto:` (and the blog's `CTA_BUTTON_LINK`/`CTA_FOOTNOTE` in `pelicanconf.py`) is `info@datacloudhero.com`. Note Cloudflare's Email Address Obfuscation rewrites any plain `mailto:` into a `data-cfemail="..."` blob at the edge on every response — seeing that in a live `curl`/view-source is expected, not a sign the address reverted; decode it (XOR each byte with the first byte) to check what it actually points at.

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

Three custom generators are wired up via `pelican.signals.article_generator_finalized` directly inside `pelicanconf.py` (no separate plugin package/folder for these — they're plain functions + `_signals.connect(...)` calls at module scope):

- `_write_markdown_mirrors` — for every article `blog/{slug}/index.html`, also writes a sibling `blog/{slug}.md` containing the raw Markdown body (metadata block stripped) plus a short source/date header. This is what the "Copy page as Markdown" article button, `llms.txt`, and the ChatGPT/Claude/Perplexity links in `ai_actions.html` all point at.
- `_write_llms_txt` — writes `output/llms.txt` at the site root, following the [llmstxt.org](https://llmstxt.org) format: `# title` / `> summary`, a `## Site` section linking `content/extra/index.md`, then a `## Blog` section with `- [title](md_url): desc` for every article.
- `_write_robots_txt` — writes a minimal `output/robots.txt` (`Disallow:` = allow everything) pointing `Sitemap:` at `sitemap.xml`. The domain is proxied through Cloudflare, which was observed serving its own "Content Signals" boilerplate text at that path *only as a fallback* when origin had no `robots.txt` at all — once this file exists, Cloudflare passes it through untouched.

`sitemap.xml` itself comes from the real 3rd-party `pelican-sitemap` plugin, pinned via `PLUGINS = ['sitemap']` and `SITEMAP = {...}` (both in `pelicanconf.py`) rather than left to Pelican's auto-discovery — leaving `PLUGINS` unset makes Pelican auto-load *any* installed `pelican.plugins.*` package, which previously caused `sitemap.xml` to appear in local dev (because `pelican-sitemap` happened to be pip-installed there) while being silently absent from the real CI build (`requirements.txt` didn't have it). Pin new plugins in both `PLUGINS` and `requirements.txt` together, never rely on auto-discovery. (There used to be a fourth generator, `_queue_homepage_for_sitemap`, that manually fired `content_written` for the landing page because it was a `STATIC_PATHS`-copied file the sitemap plugin's listener never saw — removed once the landing page became a real Page, see below, since it now fires that signal on its own.)

All three run automatically on every build (dev and publish) — no extra command needed. If article URL/save-as conventions in `pelicanconf.py` change, the `_os.path.dirname(article.save_as) + '.md'` path derivation used by more than one of these functions needs to change with them.

### `ai_actions.html` partial

Renders a per-article dropdown ("Copy page as Markdown" / "View as Markdown" / "Open in ChatGPT" / "Open in Claude" / "Open in Perplexity"), included from `article.html`. The clipboard-copy behavior is a delegated click handler in `base.html` (`.js-copy-markdown`), not in the partial itself — keep the two in sync if either is renamed. The ChatGPT/Claude/Perplexity links only pre-fill a prompt referencing the article's `.md` URL; they don't guarantee the target service fetches it (depends on that service's browsing being enabled).
