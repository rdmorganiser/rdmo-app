from django.contrib import admin
from django.urls import include, path

from rdmo.core.views import about, api, home

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('api/', api, name='api'),

    path('', include('rdmo.core.urls')),
    path('api/v1/', include('rdmo.core.urls.v1')),

    path('admin/', admin.site.urls)
]

handler400 = 'rdmo.core.views.bad_request'
handler403 = 'rdmo.core.views.forbidden'
handler404 = 'rdmo.core.views.not_found'
handler500 = 'rdmo.core.views.internal_server_error'
