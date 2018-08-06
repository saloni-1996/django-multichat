from django.conf.urls import url
from django.urls import path

from attendee import views


app_name = 'attendee'
urlpatterns = [
    path('show_event/<int:event_id>/', views.show_event, name='show_event'),
]