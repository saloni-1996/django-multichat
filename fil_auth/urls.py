from django.urls import path, include
from . import views
#import eventcoord

urlpatterns = [
	path('', views.adminpanel, name='adminpanel'),
	#ath('eventcpanel/', include('eventcoord.urls')),	
]