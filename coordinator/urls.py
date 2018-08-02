from django.urls import path, include
from coordinator import views
#import eventcoord

urlpatterns = [
	path(r'^$', views.main_panel, name='coord_main_panel'),
	path(r'^(?P<event_id>\d+)/dashboard/$', views.dashboard, name='coord_dashboard'),

]
