AUTHOR = 'Andrey'
AUTHOR_FULL = 'Andrey Ganyushkin'
SITENAME = 'Full Stack Blog'
SITEURL = ''

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
LINKS = ()
# LINKS = (('GitHub', 'https://github.com/AGanyushkin'),
# )

# Social widget
SOCIAL = (('github', 'AGanyushkin'),
          ('linkedin', 'andrey-ganyushkin-7bb99a89'),
          ('habr', 'SleepwalkerOne'),)

DEFAULT_PAGINATION = 13

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'papers']
DISPLAY_PAGES_ON_MENU = True

DEFAULT_METADATA = {
    'status': 'draft',
}

USER_LOGO_URL = '/theme/images/progg_small.jpeg'
# USER_FAVICON_URL = '/favicon.png'

# https://github.com/pelican-plugins/image-process
IMAGE_PROCESS = {
    "thumb": {
        "type": "image",
        "ops": ["crop 0 0 50% 50%", "scale_out 150 150 True", "crop 0 0 150 150"],
    },

    "article-image": {
        "type": "image",
        "ops": ["scale_in 500 300 True"],
    }
}
