from django.urls import path, include
from administrator import views
#import eventcoord

urlpatterns = [
	path(r'^$', views.main_panel, name='admin_main_panel'),
]
