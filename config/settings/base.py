import os

from django.utils.translation import ugettext_lazy as _

from rdmo.core.settings import INSTALLED_APPS, AUTHENTICATION_BACKENDS

SITE_ID = 1

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components_root')

FIXTURE_DIRS = (
   os.path.join(BASE_DIR, 'fixtures'),
)

'''
Allauth configuration, see also:
http://rdmo.readthedocs.io/en/latest/configuration/authentication/allauth.html
'''

# ACCOUNT = True
# ACCOUNT_SIGNUP = True
# SOCIALACCOUNT = False
#
# INSTALLED_APPS += [
#     'allauth',
#     'allauth.account',
#     'allauth.socialaccount'
#     'allauth.socialaccount.providers.facebook',
#     'allauth.socialaccount.providers.github',
#     'allauth.socialaccount.providers.google',
#     'allauth.socialaccount.providers.orcid',
#     'allauth.socialaccount.providers.twitter',
# ]
#
# AUTHENTICATION_BACKENDS.append('allauth.account.auth_backends.AuthenticationBackend')

'''
LDAP, see also:
http://rdmo.readthedocs.io/en/latest/configuration/authentication/ldap.html
'''

# PROFILE_UPDATE = False
#
# import ldap
# from django_auth_ldap.config import LDAPSearch
#
# AUTH_LDAP_SERVER_URI = "ldap://ldap.example.com"
# AUTH_LDAP_BIND_DN = "cn=admin,dc=ldap,dc=example,dc=com"
# AUTH_LDAP_BIND_PASSWORD = "admin"
# AUTH_LDAP_USER_SEARCH = LDAPSearch("dc=ldap,dc=example,dc=com", ldap.SCOPE_SUBTREE, "(uid=%(user)s)")
#
# AUTH_LDAP_USER_ATTR_MAP = {
#     "first_name": "givenName",
#     "last_name": "sn",
#     'email': 'mail'
# }
#
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
#
# INSTALLED_APPS += ['shibboleth']
#
# SHIBBOLETH_ATTRIBUTE_MAP = {
#     'uid': (True, 'username'),
#     'givenName': (True, 'first_name'),
#     'sn': (True, 'last_name'),
#     'mail': (True, 'email'),
# }
#
# AUTHENTICATION_BACKENDS.append('shibboleth.backends.ShibbolethRemoteUserBackend')
#
# MIDDLEWARE_CLASSES.insert(
#     MIDDLEWARE_CLASSES.index('django.contrib.auth.middleware.AuthenticationMiddleware') + 1,
#     'shibboleth.middleware.ShibbolethRemoteUserMiddleware'
# )
#
# LOGIN_URL = '/Shibboleth.sso/Login?target=/projects'
# LOGOUT_URL = '/Shibboleth.sso/Logout'

'''
Theme, see also:
http://rdmo.readthedocs.io/en/latest/configuration/themes.html
'''

# THEME_DIR = os.path.join(BASE_DIR, 'theme')

'''
Export Formats
'''

# EXPORT_FORMATS = (
#     ('pdf', _('PDF')),
#     ('rtf', _('Rich Text Format')),
#     ('odt', _('Open Office')),
#     ('docx', _('Microsoft Office')),
#     ('html', _('HTML')),
#     ('markdown', _('Markdown')),
#     ('mediawiki', _('mediawiki')),
#     ('tex', _('LaTeX'))
# )
