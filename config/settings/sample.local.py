'''
A secret key for a particular Django installation. This is used to provide
cryptographic signing, and should be set to a unique, unpredictable value.
Can be generated with:
python3 manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'
'''

SECRET_KEY = 'this is not a very secret key'

'''
The list of URLs und which this application available
'''

ALLOWED_HOSTS += ['rdmo.example.com']

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
Choose:
    'ENGINE': 'django.db.backends.postgresql_psycopg2'
or
    'ENGINE': 'django.db.backends.mysql'
'''

DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

'''
Theme, see also:
http://rdmo.readthedocs.io/en/latest/configuration/themes.html
'''

# INSTALLED_APPS = ['rdmo_theme'] + INSTALLED_APPS

'''
Authentication configuration, see also:
http://rdmo.readthedocs.io/en/latest/configuration/authentication.html
Choose your authentication system and configure it here.
'''
RDMO_AUTHENTICATION = ["allauth"]  # "allauth" and/or "shibboleth" or "ldap"

'''
Logging configuration, see also:
http://rdmo.readthedocs.io/en/latest/configuration/logging.html
'''
LOG_LEVEL = 'INFO'  # or 'DEBUG' for the full logging experience
LOG_PATH = BASE_DIR / 'log' # this directory needs to exist and be writable by the rdmo user