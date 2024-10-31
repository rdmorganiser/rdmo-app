'''
These are development settings for debug mode, don't use this in production
https://docs.djangoproject.com/en/4.2/ref/settings/
https://github.com/rdmorganiser/rdmo/blob/main/rdmo/core/settings.py
https://rdmo.readthedocs.io/en/latest/development/setup.html
'''

if DEBUG is not True:
    from django.core.exceptions import ImproperlyConfigured

    raise ImproperlyConfigured('DEBUG must be True for the development settings')

SECRET_KEY = 'this is not a very secret key'
PASSWORD_HASHERS = ("django.contrib.auth.hashers.MD5PasswordHasher",)
SITE_ID = 1

# http://rdmo.readthedocs.io/en/latest/configuration/databases.html
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

# Optional, theme: http://rdmo.readthedocs.io/en/latest/configuration/themes.html
# INSTALLED_APPS += ['rdmo_theme']

# Optional, RDMO plugins: https://github.com/rdmorganiser?q=rdmo-plugins&type=all&language=&sort=
# INSTALLED_APPS += ['rdmo_pugin']
# PROJECT_EXPORTS += []
# PROJECT_IMPORTS += []

# Optional, browsable API, that comes with the Django Rest Framework
# REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
#     'rest_framework.renderers.JSONRenderer',
#     'rest_framework.renderers.BrowsableAPIRenderer',
# )

# Optional, email port
# EMAIL_PORT = 8025
