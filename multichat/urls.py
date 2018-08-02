from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.urls import path
from chat.views import index
from fil_auth.views import adminpanel


urlpatterns = [
    url(r'^$', index, name='index'),  # The start point for index view
    url(r'^auth/', include('fil_auth.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/login/$', logout, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),  # The base django logout view
    #url(r'^accounts/register/$', logout, name='register'),
    url(r'^admin/', admin.site.urls),  # etc :D
]
