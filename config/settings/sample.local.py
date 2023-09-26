'''
Debug mode, don't use this in production
'''

# DEBUG = False

'''
A secret key for a particular Django installation. This is used to provide
cryptographic signing, and should be set to a unique, unpredictable value.
'''

# SECRET_KEY = 'this is not a very secret key'

'''
The list of URLs und which this application available
'''

# ALLOWED_HOSTS += ['rdmo.example.com']

'''
The root url of your application, only needed when its not '/'
'''

# BASE_URL = '/path'

'''
Language code and time zone
'''

# LANGUAGE_CODE = 'de-de'
# TIME_ZONE = 'Europe/Berlin'

'''
The database connection to be used, see also:
http://rdmo.readthedocs.io/en/latest/configuration/databases.html
'''

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': '',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': '',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': '',
#         'PORT': '',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': '',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': '',
#         'PORT': '',
#     }
# }

'''
Theme, see also:
http://rdmo.readthedocs.io/en/latest/configuration/themes.html
'''

# INSTALLED_APPS = ['rdmo_theme'] + INSTALLED_APPS

'''
Allauth configuration, see also:
http://rdmo.readthedocs.io/en/latest/configuration/authentication/allauth.html
'''

# ACCOUNT = True
# ACCOUNT_SIGNUP = True
# SOCIALACCOUNT = False

# INSTALLED_APPS += [
#     'allauth',
#     'allauth.account',
#     'allauth.socialaccount',
#     'allauth.socialaccount.providers.facebook',
#     'allauth.socialaccount.providers.github',
#     'allauth.socialaccount.providers.google',
#     'allauth.socialaccount.providers.orcid',
#     'allauth.socialaccount.providers.twitter',
# ]

# AUTHENTICATION_BACKENDS.append('allauth.account.auth_backends.AuthenticationBackend')
# MIDDLEWARE.append('allauth.account.middleware.AccountMiddleware')

'''
LDAP, see also:
http://rdmo.readthedocs.io/en/latest/configuration/authentication/ldap.html
'''

# import ldap
# from django_auth_ldap.config import LDAPSearch

# PROFILE_UPDATE = False

# AUTH_LDAP_SERVER_URI = "ldap://ldap.example.com"
# AUTH_LDAP_BIND_DN = "cn=admin,dc=ldap,dc=example,dc=com"
# AUTH_LDAP_BIND_PASSWORD = "admin"
# AUTH_LDAP_USER_SEARCH = LDAPSearch("dc=ldap,dc=example,dc=com", ldap.SCOPE_SUBTREE, "(uid=%(user)s)")

# AUTH_LDAP_USER_ATTR_MAP = {
#     "first_name": "givenName",
#     "last_name": "sn",
#     'email': 'mail'
# }

# AUTHENTICATION_BACKENDS.insert(
#     AUTHENTICATION_BACKENDS.index('django.contrib.auth.backends.ModelBackend'),
#     'django_auth_ldap.backend.LDAPBackend'
# )

'''
Shibboleth, see also:
http://rdmo.readthedocs.io/en/latest/configuration/authentication/shibboleth.html
'''

# SHIBBOLETH = True
# PROFILE_UPDATE = False
# PROFILE_DELETE = False

# INSTALLED_APPS += ['shibboleth']

# AUTHENTICATION_BACKENDS.append('shibboleth.backends.ShibbolethRemoteUserBackend')

# MIDDLEWARE.insert(
#     MIDDLEWARE.index('django.contrib.auth.middleware.AuthenticationMiddleware') + 1,
#     'shibboleth.middleware.ShibbolethRemoteUserMiddleware'
# )

# SHIBBOLETH_ATTRIBUTE_MAP = {
#     'uid': (True, 'username'),
#     'givenName': (True, 'first_name'),
#     'sn': (True, 'last_name'),
#     'mail': (True, 'email'),
# }

# # Optional, regular expression to identify usernames created with Shibboleth,
# # those users will be directed to SHIBBOLETH_LOGOUT_URL on logout, others will not.
# # If not set, all users will be redirected to SHIBBOLETH_LOGOUT_URL.
# SHIBBOLETH_USERNAME_PATTERN = r'@example.com$'

# # Can be used to display the regular login form next to the Shibboleth login button.
# LOGIN_FORM = False

# LOGOUT_URL = '/account/shibboleth/logout/'

'''
E-Mail configuration, see also:
http://rdmo.readthedocs.io/en/latest/configuration/email.html
'''

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'localhost'
# EMAIL_PORT = '25'
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_USE_TLS = False
# EMAIL_USE_SSL = False
# DEFAULT_FROM_EMAIL = ''

'''
Logging configuration, see also:
http://rdmo.readthedocs.io/en/latest/configuration/logging.html
'''

# from pathlib import Path
#
# LOG_LEVEL = 'INFO'          # or 'DEBUG' for the full logging experience
# LOG_PATH = '/var/log/rdmo'  # this directory needs to exist and be writable by the rdmo user
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse'
#         },
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue'
#         }
#     },
#     'formatters': {
#         'default': {
#             'format': '[%(asctime)s] %(levelname)s: %(message)s'
#         },
#         'name': {
#             'format': '[%(asctime)s] %(levelname)s %(name)s: %(message)s'
#         }
#     },
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'filters': ['require_debug_false'],
#             'class': 'django.utils.log.AdminEmailHandler'
#         },
#         'error_log': {
#             'level': 'ERROR',
#             'class': 'logging.FileHandler',
#             'filename': Path(LOG_PATH) / 'error.log',
#             'formatter': 'default'
#         },
#         'ldap_log': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': Path(LOG_PATH) / 'ldap.log',
#             'formatter': 'name'
#         },
#         'rules_log': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': Path(LOG_PATH) / 'rules.log',
#             'formatter': 'name'
#         },
#         'rdmo_plugins_log': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': Path(LOG_PATH) / 'rdmo_plugins.log',
#             'formatter': 'name'
#         },
#         'rdmo_log': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': Path(LOG_PATH) / 'rdmo.log',
#             'formatter': 'name'
#         }
#     },
#     'loggers': {
#         'django.request': {
#             'handlers': ['mail_admins', 'error_log'],
#             'level': 'ERROR',
#             'propagate': True
#         },
#         'django_auth_ldap': {
#             'handlers': ['ldap_log'],
#             'level': LOG_LEVEL,
#             'propagate': True
#         },
#         'rules': {
#             'handlers': ['rules_log'],
#             'level': LOG_LEVEL,
#             'propagate': True,
#         },
#         'rdmo_plugins': {
#             'handlers': ['rdmo_plugins_log'],
#             'level': LOG_LEVEL,
#             'propagate': True
#         },
#         'rdmo': {
#             'handlers': ['rdmo_log'],
#             'level': LOG_LEVEL,
#             'propagate': True
#         }
#     }
# }
