'''
Debug mode, don't use this in production
'''

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

# dev: use md5 hasher
PASSWORD_HASHERS = ("django.contrib.auth.hashers.MD5PasswordHasher",)

# dev: enable browsable api
if DEBUG:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    )

# dev: enable debug toolbar
if DEBUG_TOOLBAR:
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware', *MIDDLEWARE]
    INTERNAL_IPS = ['127.0.0.1']
