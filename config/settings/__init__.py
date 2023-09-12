from pathlib import Path

from rdmo.core.utils import sanitize_url

BASE_DIR = Path(__file__).parent.parent.parent
MEDIA_ROOT = BASE_DIR / 'media_root'
STATIC_ROOT = BASE_DIR / 'static_root'
STATICFILES_DIRS = [BASE_DIR / 'vendor']

SITE_ID = 1
BASE_URL = None

# import all settings from rdmo/core/settings.py
from rdmo.core.settings import *  # noqa: E402,F403

# import from base.py and local.py to override settings, feel free to add files to
from .local import *  # noqa: E402,F403

# prepend the BASE_URL to the different URL settings
if BASE_URL:
    BASE_URL = sanitize_url(BASE_URL)
    LOGIN_URL = sanitize_url(BASE_URL + LOGIN_URL)  # noqa: F405
    LOGIN_REDIRECT_URL = sanitize_url(BASE_URL + LOGIN_REDIRECT_URL)  # noqa: F405
    LOGOUT_URL = sanitize_url(BASE_URL + LOGOUT_URL)  # noqa: F405
    MEDIA_URL = sanitize_url(BASE_URL + MEDIA_URL)  # noqa: F405
    STATIC_URL = sanitize_url(BASE_URL + STATIC_URL)  # noqa: F405

    ACCOUNT_LOGOUT_REDIRECT_URL = BASE_URL
    CSRF_COOKIE_PATH = BASE_URL
    LANGUAGE_COOKIE_PATH = BASE_URL
    SESSION_COOKIE_PATH = BASE_URL
