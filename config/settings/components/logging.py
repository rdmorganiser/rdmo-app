
'''
Logging configuration, see also:
http://rdmo.readthedocs.io/en/latest/configuration/logging.html
'''

if not isinstance(LOG_PATH, Path):
    LOG_PATH = Path(LOG_PATH)

if not LOG_PATH.exists():
    raise ImproperlyConfigured('LOG_PATH %s does not exist.' % LOG_PATH)

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
