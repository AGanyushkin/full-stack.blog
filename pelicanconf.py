import os

DEF_PORT = 9999
PORT = os.environ.get('PORT', DEF_PORT)
DEF_BIND = '0.0.0.0'
BIND = os.environ.get('BIND', DEF_BIND)

AUTHOR = 'Andrey'
AUTHOR_FULL = 'Andrey Ganyushkin'
SITENAME = 'Full Stack Blog'
DEF_SITEURL = 'https://full-stack.blog'
SITEURL = os.environ.get('SITEURL', DEF_SITEURL)

TAGLINE = 'I am a software engineer with more than 10 years of experience. I am interested in both the architecture of the application and the development process itself, with full-stack and cloud approaches.'

PATH = 'content'

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Plant Name Parser Service', '/plant-name-parser-service.html'),
)

# Social widget
SOCIAL = (('github', 'AGanyushkin'),
          ('linkedin', 'andrey-ganyushkin-7bb99a89'),
          ('habr', 'SleepwalkerOne'),
          ('docker', 'aganyushkin'),)

DEFAULT_PAGINATION = 13

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'papers', 'personal', 'books']
DISPLAY_PAGES_ON_MENU = True

DEFAULT_METADATA = {
    'status': 'draft',
}

USER_LOGO_URL = '/theme/images/progg_small.jpeg'

# https://github.com/pelican-plugins/image-process
IMAGE_PROCESS = {
    "thumb": {
        "type": "image",
        "ops": ["crop 0 0 50% 50%", "scale_out 150 150 True", "crop 0 0 150 150"],
    },

    "article-image": {
        "type": "image",
        "ops": ["scale_in 500 300 True"],
    },

    "big-article-image": {
        "type": "image",
        "ops": ["scale_in 650 600 True"],
    }
}

MENUITEMS = (

)

SEO_REPORT = True  # SEO report is enabled by default
SEO_ENHANCER = True  # SEO enhancer is disabled by default
SEO_ENHANCER_OPEN_GRAPH = True # Subfeature of SEO enhancer
SEO_ENHANCER_TWITTER_CARDS = True # Subfeature of SEO enhancer

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly"
    }
}

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.toc': {
            'title': 'Table of contents:'
        },
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
