AUTHOR = 'Edgar L'
SITENAME = 'datacloudhero.com'
SITEURL = ""
# One-line description used in llms.txt (see bottom of this file) and other
# machine-readable summaries of the site.
SITE_DESCRIPTION = "Practical guides and tutorials on data & AI engineering."

# Google Tag Manager container ID. Empty here (dev) on purpose - set for
# real in publishconf.py only, so `make devserver`/local testing doesn't
# report hits into GTM. Read directly as {{ GTM_ID }} in base.html/
# landing.html (no JINJA_GLOBALS needed - Pelican exposes all settings to
# templates automatically).
GTM_ID = ''

PATH = "content"

THEME = "themes/mytheme"
AUTHORS_INFO = {
    'Edgar L': {
        'avatar': 'https://avatars.githubusercontent.com/u/78014277?v=4',
        'title': 'Technical Content Writer — AI & Data',
        'linkedin': 'https://www.linkedin.com/in/edgarlakshin/',
        'github': 'https://github.com/edgrln',
    },
    'Alina Lane': {
        'avatar': 'https://avatars.githubusercontent.com/u/253337931?v=4',
        'title': 'Founder datacloud.com',
        'linkedin': 'https://www.linkedin.com/in/edgarlakshin/',
        'github': 'https://github.com/edgrln',
    },
}

CTA_TITLE = "Let's build something great"
CTA_TEXT = "Describe your challenge — we'll talk it through directly, no sales pitch."
CTA_BUTTON_TEXT = "Get in touch"
CTA_BUTTON_LINK = "mailto:info@datacloudhero.com"
CTA_FOOTNOTE = "info@datacloudhero.com · Remote across Europe"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Supported site languages: code -> short display label (used for the
# current-language button in the nav dropdown). Order here is the order
# languages render in. Adding a language means: add it here and to
# LANGUAGE_NAMES, add a UI_STRINGS['xx'] bundle below, and start writing
# content/{xx}/ articles + a content/pages/landing-{xx}.html.
LANGUAGES = {
    'en': 'EN',
    'fr': 'FR',
    'de': 'DE',
    'es': 'ES',
}

# Native full names for the same languages, used inside the dropdown menu
# itself (LANGUAGES is just the short code shown on the closed button).
LANGUAGE_NAMES = {
    'en': 'English',
    'fr': 'Français',
    'de': 'Deutsch',
    'es': 'Español',
}

# Translations for template chrome (nav/footer/buttons/etc.) - NOT for
# content itself (articles/pages are translated as separate content files).
# Templates look these up via UI_STRINGS[lang][key], where `lang` is the
# current article/page's `.lang` (see get_ui_lang() in blog_base.html and
# landing.html). Keep keys in sync across all four language dicts.
UI_STRINGS = {
    'en': {
        'blog_nav': 'Blog',
        'all_posts': 'All posts',
        'latest_posts': 'Latest posts',
        'read_more': 'Read more',
        'back_to_posts': '← Back to all posts',
        'tags': 'Tags:',
        'min_read': 'min read',
        'loading_more': 'Loading more posts…',
        'previous': 'Previous',
        'next': 'Next',
        'search_placeholder': 'Search',
        'no_results': 'No results found',
        'see_all_results': 'See all results',
        'copy_page': 'Copy page',
        'copy_page_md': 'Copy page as Markdown',
        'view_as_md': 'View as Markdown',
        'open_in': 'Open in {name}',
        'copied': 'Copied!',
        'copy_failed': 'Copy failed',
        'ready_to_start': 'Ready to start?',
        'cookie_settings': 'Cookie settings',
        'cookie_policy': 'Cookie Policy',
    },
    'fr': {
        'blog_nav': 'Blog',
        'all_posts': 'Tous les articles',
        'latest_posts': 'Derniers articles',
        'read_more': 'Lire la suite',
        'back_to_posts': '← Retour à tous les articles',
        'tags': 'Étiquettes :',
        'min_read': 'min de lecture',
        'loading_more': 'Chargement d’articles supplémentaires…',
        'previous': 'Précédent',
        'next': 'Suivant',
        'search_placeholder': 'Rechercher',
        'no_results': 'Aucun résultat trouvé',
        'see_all_results': 'Voir tous les résultats',
        'copy_page': 'Copier la page',
        'copy_page_md': 'Copier la page en Markdown',
        'view_as_md': 'Voir en Markdown',
        'open_in': 'Ouvrir dans {name}',
        'copied': 'Copié !',
        'copy_failed': 'Échec de la copie',
        'ready_to_start': 'Prêt à commencer ?',
        'cookie_settings': 'Préférences cookies',
        'cookie_policy': 'Politique de cookies',
    },
    'de': {
        'blog_nav': 'Blog',
        'all_posts': 'Alle Beiträge',
        'latest_posts': 'Neueste Beiträge',
        'read_more': 'Weiterlesen',
        'back_to_posts': '← Zurück zu allen Beiträgen',
        'tags': 'Tags:',
        'min_read': 'Min. Lesezeit',
        'loading_more': 'Weitere Beiträge werden geladen…',
        'previous': 'Zurück',
        'next': 'Weiter',
        'search_placeholder': 'Suchen',
        'no_results': 'Keine Ergebnisse gefunden',
        'see_all_results': 'Alle Ergebnisse anzeigen',
        'copy_page': 'Seite kopieren',
        'copy_page_md': 'Seite als Markdown kopieren',
        'view_as_md': 'Als Markdown anzeigen',
        'open_in': 'In {name} öffnen',
        'copied': 'Kopiert!',
        'copy_failed': 'Kopieren fehlgeschlagen',
        'ready_to_start': 'Bereit loszulegen?',
        'cookie_settings': 'Cookie-Einstellungen',
        'cookie_policy': 'Cookie-Richtlinie',
    },
    'es': {
        'blog_nav': 'Blog',
        'all_posts': 'Todas las entradas',
        'latest_posts': 'Últimas entradas',
        'read_more': 'Leer más',
        'back_to_posts': '← Volver a todas las entradas',
        'tags': 'Etiquetas:',
        'min_read': 'min de lectura',
        'loading_more': 'Cargando más entradas…',
        'previous': 'Anterior',
        'next': 'Siguiente',
        'search_placeholder': 'Buscar',
        'no_results': 'No se encontraron resultados',
        'see_all_results': 'Ver todos los resultados',
        'copy_page': 'Copiar página',
        'copy_page_md': 'Copiar página como Markdown',
        'view_as_md': 'Ver como Markdown',
        'open_in': 'Abrir en {name}',
        'copied': '¡Copiado!',
        'copy_failed': 'Error al copiar',
        'ready_to_start': '¿Listo para empezar?',
        'cookie_settings': 'Preferencias de cookies',
        'cookie_policy': 'Política de cookies',
    },
}

# Per-language CTA box copy (see partials/cta.html). English keeps using the
# CTA_* settings above (unchanged, pre-existing copy); this only covers the
# translated languages.
CTA_STRINGS = {
    'fr': {
        'title': "Construisons quelque chose de solide",
        'text': "Décrivez votre projet — on en discute directement, sans discours commercial.",
        'button_text': "Écrivez-nous",
        'footnote': "info@datacloudhero.com · Travail à distance",
    },
    'de': {
        'title': "Lassen Sie uns etwas Gutes aufbauen",
        'text': "Beschreiben Sie Ihre Herausforderung — wir besprechen sie direkt, ohne Verkaufsgespräch.",
        'button_text': "Schreiben Sie uns",
        'footnote': "info@datacloudhero.com · Arbeite remote",
    },
    'es': {
        'title': "Construyamos algo grande",
        'text': "Describa su desafío — hablamos directamente, sin discurso de ventas.",
        'button_text': "Escríbenos",
        'footnote': "info@datacloudhero.com · Trabajo en remoto",
    },
}

JINJA_GLOBALS = {
    'UI_STRINGS': UI_STRINGS,
    'CTA_STRINGS': CTA_STRINGS,
    'SITE_LANGUAGES': LANGUAGES,
    'SITE_LANGUAGE_NAMES': LANGUAGE_NAMES,
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll. Both "Cookie Policy" and "Cookie settings" used to live here as
# dead "#" links - they're now hardcoded directly in base.html's footer
# instead: "Cookie Policy" links to the real content/pages/cookie-policy.md
# page (needs {{ SITEURL }}, which a plain LINKS entry can't carry per
# dev/prod build), and "Cookie settings" is a data-cc="show-preferencesModal"
# button (needs to trigger JS, not navigate anywhere).
LINKS = []

# Social widget
SOCIAL = [
    ("Git Hub", "https://github.com/edgrln/datacloudhero_v2"),
]

DEFAULT_PAGINATION = 10

# Clean stale files (e.g. old *.html paths) before each build
DELETE_OUTPUT_DIRECTORY = True

# Explicit plugin list. Pelican auto-loads any installed pelican.plugins.*
# package if PLUGINS is left unset, which makes builds depend on whatever
# happens to be pip-installed in a given environment - pin it down instead.
PLUGINS = ['sitemap']
SITEMAP = {
    'format': 'xml',
    'exclude': [
        # A JSON data file for the client-side search widget, not a page.
        r'blog/search-index\.json$',
    ],
    'priorities': {
        'articles': 0.6,
        'indexes': 0.5,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    },
}

# All blog content lives under /blog/ — the site root is a separate static
# landing page (see STATIC_PATHS below), not generated by Pelican.
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
PAGE_URL = 'blog/{slug}/'
PAGE_SAVE_AS = 'blog/{slug}/index.html'
# Non-default-language articles (Lang: fr/de/es + a Slug: matching their
# English original - see content/fr/, content/de/, content/es/) get a
# /{lang}/ prefix instead of living at the same /blog/{slug}/ URL. Pelican
# links same-slug articles across languages automatically via
# ARTICLE_TRANSLATION_ID (default: 'slug') - see article.translations in
# templates for the language switcher.
ARTICLE_LANG_URL = '{lang}/blog/{slug}/'
ARTICLE_LANG_SAVE_AS = '{lang}/blog/{slug}/index.html'
AUTHOR_URL = 'blog/author/{slug}/'
AUTHOR_SAVE_AS = 'blog/author/{slug}/index.html'
CATEGORY_URL = 'blog/category/{slug}/'
CATEGORY_SAVE_AS = 'blog/category/{slug}/index.html'
TAG_URL = 'blog/tag/{slug}/'
TAG_SAVE_AS = 'blog/tag/{slug}/index.html'

INDEX_SAVE_AS = 'blog/index.html'
TAGS_SAVE_AS = 'blog/tags.html'
TAGS_URL = 'blog/tags.html'
CATEGORIES_SAVE_AS = 'blog/categories.html'
CATEGORIES_URL = 'blog/categories.html'
AUTHORS_SAVE_AS = 'blog/authors.html'
AUTHORS_URL = 'blog/authors.html'
ARCHIVES_SAVE_AS = 'blog/archives.html'
ARCHIVES_URL = 'blog/archives.html'

# Client-side search index (see themes/mytheme/templates/search.html)
DIRECT_TEMPLATES = ["index", "tags", "categories", "authors", "archives", "search"]
SEARCH_SAVE_AS = "blog/search-index.json"
SEARCH_URL = "blog/search-index.json"

# Landing page: content/pages/landing.html is a real Pelican Page (see
# themes/mytheme/templates/landing.html), NOT run through the blog
# theme/templates - it has its own standalone <head>/<body> shell (Tailwind
# CDN, Alpine.js, custom fonts/CSS) unrelated to base.html. Its per-page
# <meta name="save_as"/"url"/"template"> tags route it to output/index.html
# using the "landing" template instead of the blog PAGE_URL/PAGE_SAVE_AS
# pattern below. (It used to be a hand-copied static file; converted so it
# can go through Pelican's normal pipeline - i18n plugins, Jinja variables,
# etc. - like any other content.)
#
# favicon.ico is duplicated to the site root here (same file as
# themes/mytheme/static/img/favicon.ico). Browsers fall back to fetching
# /favicon.ico at the domain root for tabs that have no <link rel="icon">
# to read from - e.g. the raw-text blog/{slug}.md mirrors - so a root-level
# copy is what lets those tabs pick up a favicon at all.
#
# extra/index.md (+ its -fr/-de/-es siblings) are short hand-written
# Markdown summaries of the landing page (NOT auto-derived from
# landing.html/landing-{lang}.html - those pages are big Tailwind/Alpine.js
# files with no clean text source to extract, e.g. the FAQ copy only exists
# inside an Alpine `x-for` JS array). Keep each in sync by hand when the
# pitch on the corresponding landing page changes materially.
STATIC_PATHS = [
    'extra/index.md', 'extra/index-fr.md', 'extra/index-de.md', 'extra/index-es.md',
    'extra/favicon.ico',
]
EXTRA_PATH_METADATA = {
    'extra/index.md': {'path': 'index.md'},
    'extra/index-fr.md': {'path': 'fr/index.md'},
    'extra/index-de.md': {'path': 'de/index.md'},
    'extra/index-es.md': {'path': 'es/index.md'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}
# Keep the article/page generators from also trying to parse content/extra
# (the static passthrough files above) as blog content. ARTICLE_PATHS
# defaults to [""] - i.e. Pelican's ArticlesGenerator walks the *entire*
# content/ tree, including content/pages/ - so 'pages' has to be excluded
# here too, or content/pages/landing.html gets picked up as both an
# Article and a Page and they race to write the same output/index.html.
ARTICLE_EXCLUDES = ['extra', 'pages']
PAGE_EXCLUDES = ['extra']

import json as _json
JINJA_FILTERS = {"tojson": _json.dumps}

# --- Markdown mirrors (Stripe-style /docs/foo.md) --------------------------
# Alongside every rendered blog/{slug}/index.html, write a plain
# blog/{slug}.md containing the article's raw Markdown body. This gives
# LLMs/scrapers/"copy as markdown" buttons a clean source to fetch instead
# of having to parse the HTML page.
import os as _os
import re as _re

_METADATA_LINE_RE = _re.compile(r'^[A-Za-z][\w ]*:\s')


def _strip_pelican_metadata(raw_text):
    """Return the article body, with the leading `Key: value` metadata
    block (Title/Date/Author/...) that Pelican reads off the top of a
    Markdown source file removed."""
    lines = raw_text.splitlines()
    body_start = 0
    for idx, line in enumerate(lines):
        if not line.strip():
            body_start = idx + 1
            break
        if not _METADATA_LINE_RE.match(line):
            # Doesn't look like a metadata block at all - keep everything.
            body_start = 0
            break
    else:
        body_start = len(lines)
    return "\n".join(lines[body_start:]).strip() + "\n"


def _write_markdown_mirrors(article_generator):
    site_url = article_generator.settings.get('SITEURL', '') or ''
    # .articles only holds one canonical (DEFAULT_LANG) item per slug -
    # French/German/Spanish versions of that same slug live in .translations
    # instead (see _expose_translations_to_context) and need mirrors too.
    all_articles = list(article_generator.articles) + list(article_generator.translations)
    for article in all_articles:
        source_path = getattr(article, 'source_path', None)
        if not source_path or not _os.path.exists(source_path):
            continue

        with open(source_path, encoding='utf-8') as f:
            body = _strip_pelican_metadata(f.read())

        canonical = f"{site_url}/{article.url}" if site_url else f"/{article.url}"
        header = (
            f"# {article.title}\n\n"
            f"> Source: {canonical}\n"
            f"> Published: {article.date:%Y-%m-%d}\n\n"
        )

        # blog/{slug}/index.html -> blog/{slug}.md
        md_relpath = _os.path.dirname(article.save_as) + '.md'
        md_path = _os.path.join(article_generator.output_path, md_relpath)
        _os.makedirs(_os.path.dirname(md_path), exist_ok=True)
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(header + body)


def _collapse_ws(text):
    return _re.sub(r'\s+', ' ', text or '').strip()


def _plain_summary(article):
    """A one-line, tag-free description for an article: prefer the
    `Summary:` metadata, falling back to Pelican's auto-generated summary.
    Pelican's Markdown reader runs both through the Markdown->HTML
    converter, so either way we strip tags before using it."""
    raw = article.metadata.get('summary') or article.summary or ''
    return _collapse_ws(_re.sub(r'<[^>]+>', '', raw))


def _write_llms_txt(article_generator):
    """Write an /llms.txt index (per the llmstxt.org convention) listing
    every article/landing page and its Markdown mirror, so LLM tools can
    discover and fetch the site's content without scraping HTML. Covers
    every language in LANGUAGES: one Homepage entry per language under
    "## Site" (content/extra/index-{lang}.md), and one "## Blog"-style
    section per language (default-language articles under the plain
    "## Blog", others under "## Blog ({LANG})")."""
    settings = article_generator.settings
    site_url = settings.get('SITEURL', '') or ''
    site_name = settings.get('SITENAME', '')
    description = settings.get('SITE_DESCRIPTION', '')
    languages = settings.get('LANGUAGES', {'en': 'EN'})
    default_lang = settings.get('DEFAULT_LANG', 'en').lower()

    def url_for(relpath):
        return f"{site_url}/{relpath}" if site_url else f"/{relpath}"

    lines = [f"# {site_name}", "", f"> {description}", "", "## Site", ""]
    for lang_code, label in languages.items():
        index_relpath = 'index.md' if lang_code == default_lang else f'{lang_code}/index.md'
        lines.append(f"- [Homepage ({label})]({url_for(index_relpath)}): Services, tech stack, process and contact.")
    lines.append("")

    all_articles = list(article_generator.articles) + list(article_generator.translations)
    for lang_code, label in languages.items():
        lang_articles = sorted(
            (a for a in all_articles if a.lang == lang_code),
            key=lambda a: a.date,
            reverse=True,
        )
        if not lang_articles:
            continue
        lines.append("## Blog" if lang_code == default_lang else f"## Blog ({label})")
        lines.append("")
        for article in lang_articles:
            md_relpath = _os.path.dirname(article.save_as) + '.md'
            desc = _plain_summary(article)
            entry = f"- [{article.title}]({url_for(md_relpath)})"
            if desc:
                entry += f": {desc}"
            lines.append(entry)
        lines.append("")

    path = _os.path.join(article_generator.output_path, 'llms.txt')
    _os.makedirs(_os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines) + "\n")


def _write_robots_txt(article_generator):
    """Write a minimal, permissive /robots.txt that just points crawlers at
    the sitemap. Note: this domain is proxied through Cloudflare, which has
    been observed overriding/intercepting robots.txt at the edge with its
    own "Content Signals" policy text regardless of what the origin serves
    - if that's still happening, this file won't be what crawlers actually
    see, and the fix is in the Cloudflare dashboard, not here."""
    site_url = article_generator.settings.get('SITEURL', '') or ''
    lines = [
        "User-agent: *",
        "Disallow:",
        "",
        f"Sitemap: {site_url}/sitemap.xml" if site_url else "Sitemap: /sitemap.xml",
    ]
    path = _os.path.join(article_generator.output_path, 'robots.txt')
    _os.makedirs(_os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines) + "\n")


def _expose_translations_to_context(article_generator):
    """Pelican's shared Jinja context only exposes `articles` - one
    canonical item per translation group (ARTICLE_TRANSLATION_ID='slug'),
    chosen by DEFAULT_LANG. Every other-language version of that same slug
    (our French/German/Spanish articles) lives in
    `article_generator.translations` instead and is otherwise invisible to
    templates. Expose it under the same shared context dict so templates
    can look across all languages via `articles + translations` (see
    blog_base.html's sidebar and _write_lang_blog_indexes below)."""
    article_generator.context['translations'] = article_generator.translations


def _write_lang_blog_indexes(article_generator):
    """/blog/ (English, the default language) is generated normally by
    Pelican's own IndexesGenerator from ARTICLE_URL/INDEX_SAVE_AS. For each
    *other* language in LANGUAGES, hand-render an equivalent listing containing
    only that language's articles, using a dedicated template (no pagination
    machinery - there isn't enough content per language yet to need it).
    Written directly (bypassing Pelican's Writer, like our other custom
    generators), so content_written is fired manually for the sitemap plugin
    to pick these pages up."""
    settings = article_generator.settings
    languages = settings.get('LANGUAGES', {})
    default_lang = settings.get('DEFAULT_LANG', 'en').lower()
    all_articles = list(article_generator.articles) + list(article_generator.translations)

    template = article_generator.get_template('blog_index_lang')
    for lang in languages:
        if lang == default_lang:
            continue  # /blog/ itself already covers the default language
        lang_articles = sorted(
            (a for a in all_articles if a.lang == lang),
            key=lambda a: a.date,
            reverse=True,
        )
        if not lang_articles:
            continue

        local_context = dict(article_generator.context)
        local_context['articles'] = lang_articles
        local_context['current_lang'] = lang
        html = template.render(local_context)

        out_path = _os.path.join(article_generator.output_path, lang, 'blog', 'index.html')
        _os.makedirs(_os.path.dirname(out_path), exist_ok=True)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(html)
        _signals.content_written.send(out_path, context={})


from pelican import signals as _signals
_signals.article_generator_finalized.connect(_write_markdown_mirrors)
_signals.article_generator_finalized.connect(_write_llms_txt)
_signals.article_generator_finalized.connect(_write_robots_txt)
_signals.article_generator_finalized.connect(_expose_translations_to_context)
_signals.article_generator_finalized.connect(_write_lang_blog_indexes)
# NOTE: no manual sitemap injection for the homepage anymore - now that
# content/pages/landing.html is a real Pelican Page (see STATIC_PATHS
# comment above), it fires `content_written` on its own like any other
# page, and the sitemap plugin queues it through its normal path.

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
