
'''
Shibboleth, see also:
http://rdmo.readthedocs.io/en/latest/configuration/authentication/shibboleth.html
'''

SHIBBOLETH = True
PROFILE_UPDATE = False
PROFILE_DELETE = False

INSTALLED_APPS += ['shibboleth']

AUTHENTICATION_BACKENDS.append('shibboleth.backends.ShibbolethRemoteUserBackend')

MIDDLEWARE.insert(
    MIDDLEWARE.index('django.contrib.auth.middleware.AuthenticationMiddleware') + 1,
    'shibboleth.middleware.ShibbolethRemoteUserMiddleware'
)

SHIBBOLETH_ATTRIBUTE_MAP = {
    'uid': (True, 'username'),
    'givenName': (True, 'first_name'),
    'sn': (True, 'last_name'),
    'mail': (True, 'email'),
}

# Optional, regular expression to identify usernames created with Shibboleth,
# those users will be directed to SHIBBOLETH_LOGOUT_URL on logout, others will not.
# If not set, all users will be redirected to SHIBBOLETH_LOGOUT_URL.
SHIBBOLETH_USERNAME_PATTERN = r'@example.com$'

# Can be used to display the regular login form next to the Shibboleth login button.
LOGIN_FORM = False

LOGOUT_URL = '/account/shibboleth/logout/'
