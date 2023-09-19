from os import environ
from pathlib import Path

from django.core.exceptions import ImproperlyConfigured

from split_settings.tools import include, optional

from rdmo.core.settings import *  # import all rdmo default settings
from rdmo.core.utils import sanitize_url

ENV = environ.get('DJANGO_ENV') or 'production'

BASE_DIR = Path(__file__).parent.parent.parent
MEDIA_ROOT = BASE_DIR / 'media_root'
STATIC_ROOT = BASE_DIR / 'static_root'
STATICFILES_DIRS = [BASE_DIR / 'vendor']

# First include the settings from local.py, this file is not under version control
include(optional('local.py'))
include(
    "components/cache.py",
    "components/email.py",
    "components/logging.py",
    optional("components/export_import.py"),
)
# DEBUG can be set in local.py for example
if DEBUG or ENV == 'development':
    include(
        "environments/development.py",
    )

# RDMO_AUTHENTICATION is imported from local.py
AUTHENTICATION_OPTIONS = ("allauth", "ldap", "shibboleth")
if not all(auth_option in AUTHENTICATION_OPTIONS for auth_option in RDMO_AUTHENTICATION):
    _msg = "RDMO_AUTHENTICATION must be a subset of {} and not\n\t {}".format(
        str(AUTHENTICATION_OPTIONS), str(RDMO_AUTHENTICATION)
    )
    raise ImproperlyConfigured(_msg)

for auth_option in RDMO_AUTHENTICATION:
    # imports the settings from the chosen auth modules:
    include(f"components/auth/{auth_option}.py")

# prepend the BASE_URL to the different URL settings
if BASE_URL:
    BASE_URL = sanitize_url(BASE_URL)
    LOGIN_URL = sanitize_url(BASE_URL + LOGIN_URL)
    LOGIN_REDIRECT_URL = sanitize_url(BASE_URL + LOGIN_REDIRECT_URL)
    LOGOUT_URL = sanitize_url(BASE_URL + LOGOUT_URL)
    MEDIA_URL = sanitize_url(BASE_URL + MEDIA_URL)
    STATIC_URL = sanitize_url(BASE_URL + STATIC_URL)

    ACCOUNT_LOGOUT_REDIRECT_URL = BASE_URL
    CSRF_COOKIE_PATH = BASE_URL
    LANGUAGE_COOKIE_PATH = BASE_URL
    SESSION_COOKIE_PATH = BASE_URL
