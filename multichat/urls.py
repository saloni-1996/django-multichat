from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from chat.views import index


urlpatterns = [
    url(r'^$', index, name='index'),  # The start point for index view
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/logout/$', logout, name='logout'),  # The base django logout view
    url(r'^admin/', admin.site.urls),  # etc :D
]
