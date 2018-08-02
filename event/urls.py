from django.urls import path, include
from event import views
#import eventcoord

urlpatterns = [
	path(r'create/^$', views.create_event, name='create_event'),
	path(r'^(?P<event_id>\d+)/edit/$', views.edit_event, name='edit_event'),
	path(r'^(?P<event_id>\d+)/details/$', views.view_event, name='view_event'),
	path(r'^(?P<event_id>\d+)/qr/$', views.show_event_qr, name='view_event_qr'),
]
