from pathlib import Path

from rdmo.core.utils import sanitize_url

BASE_DIR = Path(__file__).parent.parent.parent
MEDIA_ROOT = BASE_DIR / 'media_root'
STATIC_ROOT = BASE_DIR / 'static_root'
STATICFILES_DIRS = [BASE_DIR / 'vendor']

SITE_ID = 1
LOG_LEVEL = 'INFO'
LOG_PATH = None
DEBUG_TOOLBAR = None

# import all settings from rdmo/core/settings.py
from rdmo.core.settings import *  # noqa: E402,F403

# import all settings from config/settings/base.py
from .base import *  # noqa: E402,F403

# import all settings from config/settings/local.py
from .local import *  # noqa: E402,F403

# prepend the BASE_URL to the different URL settings
if BASE_URL:  # noqa: F405
    BASE_URL = sanitize_url(BASE_URL)  # noqa: F405
    LOGIN_URL = sanitize_url(BASE_URL + LOGIN_URL)  # noqa: F405
    LOGIN_REDIRECT_URL = sanitize_url(BASE_URL + LOGIN_REDIRECT_URL)  # noqa: F405
    LOGOUT_URL = sanitize_url(BASE_URL + LOGOUT_URL)  # noqa: F405
    MEDIA_URL = sanitize_url(BASE_URL + MEDIA_URL)  # noqa: F405
    STATIC_URL = sanitize_url(BASE_URL + STATIC_URL)  # noqa: F405

    ACCOUNT_LOGOUT_REDIRECT_URL = BASE_URL
    CSRF_COOKIE_PATH = BASE_URL
    LANGUAGE_COOKIE_PATH = BASE_URL
    SESSION_COOKIE_PATH = BASE_URL

if DEBUG:  # noqa: F405
    # enable browsable API in DEBUG mode
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (  # noqa: F405
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    )

    # enable debug toolbar in DEBUG mode
    if DEBUG_TOOLBAR:  # noqa: F405
        INSTALLED_APPS += ['debug_toolbar']  # noqa: F405
        MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE   # noqa: F405
        INTERNAL_IPS = ['127.0.0.1']

if LOG_PATH:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            },
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue'
            }
        },
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(levelname)s: %(message)s'
            },
            'name': {
                'format': '[%(asctime)s] %(levelname)s %(name)s: %(message)s'
            }
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            },
            'error_log': {
                'level': 'ERROR',
                'class': 'logging.FileHandler',
                'filename': LOG_PATH / 'error.log',
                'formatter': 'default'
            },
            'ldap_log': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': LOG_PATH / 'ldap.log',
                'formatter': 'name'
            },
            'rules_log': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': LOG_PATH / 'rules.log',
                'formatter': 'name'
            },
            'rdmo_plugins_log': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': LOG_PATH / 'rdmo_plugins.log',
                'formatter': 'name'
            },
            'rdmo_log': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': LOG_PATH / 'rdmo.log',
                'formatter': 'name'
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins', 'error_log'],
                'level': 'ERROR',
                'propagate': True
            },
            'django_auth_ldap': {
                'handlers': ['ldap_log'],
                'level': LOG_LEVEL,
                'propagate': True
            },
            'rules': {
                'handlers': ['rules_log'],
                'level': LOG_LEVEL,
                'propagate': True,
            },
            'rdmo_plugins': {
                'handlers': ['rdmo_plugins_log'],
                'level': LOG_LEVEL,
                'propagate': True
            },
            'rdmo': {
                'handlers': ['rdmo_log'],
                'level': LOG_LEVEL,
                'propagate': True
            }
        }
    }
