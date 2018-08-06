from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from fil_auth.views import auth_test
from administrator import urls as admin_urls
from coordinator import urls as coord_urls
from event import urls as event_urls
from presenter import urls as persenter_urls
from attendee import urls as attendee_urls

urlpatterns = [
    url(r'^$', auth_test, name='index'),  # The start point for index view
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin_urls)),
    url(r'^coord/', include(coord_urls)),
    url(r'^event/', include(event_urls)),
    url(r'^presenter/', include(persenter_urls)),
    url(r'^accounts/login/$', logout, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),  # The base django logout view
    url(r'^django-admin/', admin.site.urls),  # etc :D
    url(r'^attendee/',include(attendee_urls))
]
