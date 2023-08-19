'''
Theme, see also:
http://rdmo.readthedocs.io/en/latest/configuration/themes.html
'''

# INSTALLED_APPS = ['rdmo_theme'] + INSTALLED_APPS

'''
Language code and time zone
'''

# LANGUAGE_CODE = 'de-de'
# TIME_ZONE = 'Europe/Berlin'

'''
Allauth configuration, see also:
http://rdmo.readthedocs.io/en/latest/configuration/authentication/allauth.html
'''

# from rdmo.core.settings import AUTHENTICATION_BACKENDS  # noqa: 402
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

'''
LDAP, see also:
http://rdmo.readthedocs.io/en/latest/configuration/authentication/ldap.html
'''

# import ldap  # noqa: 402
# from django_auth_ldap.config import LDAPSearch  # noqa: 402
# from rdmo.core.settings import AUTHENTICATION_BACKENDS  # noqa: 402

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

# from rdmo.core.settings import AUTHENTICATION_BACKENDS, MIDDLEWARE  # noqa: 402

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
