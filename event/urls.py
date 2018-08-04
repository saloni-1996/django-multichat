from django.conf.urls import url
from django.urls import path
from event import views

# import eventcoord

app_name = 'event'
urlpatterns = [
    url(r'create/', views.create_event, name='create_event'),
    url(r'^(?P<event_id>\d+)/edit/$', views.edit_event, name='edit_event'),
    path('<int:event_id>/details/', views.view_event, name='view_event'),
    url(r'^(?P<event_id>\d+)/details/$', views.view_event, name='view_event'),
    url(r'^(?P<event_id>\d+)/qr/$', views.show_event_qr, name='view_event_qr'),
]
