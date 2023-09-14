from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from rdmo.core.views import about, home

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),

    path('', include('rdmo.core.urls')),
    path('api/v1/', include('rdmo.core.urls.v1')),
    path('api/v1/', include('rdmo.core.urls.swagger')),

    path('admin/', admin.site.urls)
]

handler400 = 'rdmo.core.views.bad_request'
handler403 = 'rdmo.core.views.forbidden'
handler404 = 'rdmo.core.views.not_found'
handler500 = 'rdmo.core.views.internal_server_error'

# dev: add debug toolbar urls
if settings.DEBUG_TOOLBAR:
    import debug_toolbar
    path('__debug__/', include(debug_toolbar.urls))
