from django.conf.urls import url
from coordinator import views

urlpatterns = [
	url(r'^$', views.main_panel, name='coord_main_panel'),
	url(r'^(?P<event_id>\d+)/dashboard/$', views.dashboard, name='coord_dashboard'),
]
