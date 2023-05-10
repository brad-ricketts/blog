AUTHOR = "Brad Ricketts"
SITENAME = "Fitness and Injuries"
SITEURL = ""

PATH = "content"

TIMEZONE = "America/Indianapolis"

# DEFAULT_LANG = "English"
DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Pelican Theme
# I'm using the Pelican Alchemy theme
# https://github.com/nairobilug/pelican-alchemy
THEME = "./alchemy"
PYGMENTS_STYLE = "default"
THEME_CSS_OVERRIDES = ["theme/css/oldstyle.css"]
SITEIMAGE = (
    "/images/vecteezy_gym-barbell-with-kettle-bell-and-medical-cross-symbol-inside_.jpg"
)
SITESUBTITLE = "Navigating fitness at 40+ years old"
# Social widget
SOCIAL = "https://www.facebook.com/brad.ricketts"

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Image processing plugin
IMAGE_PROCESS = {
    "crisp": {
        "type": "responsive-image",
        "srcset": [
            ("1x", ["scale_in 600 800 True"]),
            ("2x", ["scale_in 1200 1600 True"]),
            ("4x", ["scale_in 2400 3200 True"]),
        ],
        "default": "1x",
    },
    "large-photo": {
        "type": "responsive-image",
        "sizes": (
            "(min-width: 1200px) 800px, "
            "(min-width: 992px) 650px, "
            "(min-width: 768px) 718px, "
            "100vw"
        ),
        "srcset": [
            ("600w", ["scale_in 450 600 True"]),
            ("800w", ["scale_in 600 800 True"]),
            ("1600w", ["scale_in 1200 1600 True"]),
        ],
        "default": "800w",
    },
}
