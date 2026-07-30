AUTHOR = 'Edgar L'
SITENAME = 'datacloudhero'
SITEURL = ""

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
CTA_TEXT = "Опишите вашу задачу — обсудим без лишних продаж, чисто по делу."
CTA_BUTTON_TEXT = "Написать"
CTA_BUTTON_LINK = "mailto:you@example.com"
CTA_FOOTNOTE = "you@example.com · Работаю удалённо"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'En'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = [
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
]

# Social widget
SOCIAL = [
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
]

DEFAULT_PAGINATION = 1

# Clean stale files (e.g. old *.html paths) before each build
DELETE_OUTPUT_DIRECTORY = True

# Pretty URLs (no .html suffix)
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

# Client-side search index (see themes/mytheme/templates/search.html)
DIRECT_TEMPLATES = ["index", "tags", "categories", "authors", "archives", "search"]
SEARCH_SAVE_AS = "search-index.json"
SEARCH_URL = "search-index.json"

import json as _json
JINJA_FILTERS = {"tojson": _json.dumps}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
