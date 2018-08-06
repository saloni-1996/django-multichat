from django.conf.urls import url
from event import views
#import eventcoord
urlpatterns = [
	url(r'^create/$', views.create_event, name='create_event'),
	url(r'^(?P<event_id>\d+)/edit/$', views.edit_event, name='edit_event'),
	url(r'^(?P<event_id>\d+)/details/$', views.view_event, name='view_event'),
	url(r'^(?P<event_id>\d+)/qr/$', views.show_event_qr, name='view_event_qr'),
]
