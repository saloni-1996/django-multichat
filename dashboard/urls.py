from django.conf.urls import url
from dashboard import views
#import eventcoord
urlpatterns = [	
	url(r'^$', views.view_dashboard, name='view_dashboard'),
	#url(r'^(?P<event_id>\d+)/addquestion/$',  views.add_question, name='add_question'),
]
