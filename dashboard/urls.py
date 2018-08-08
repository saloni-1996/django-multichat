from django.conf.urls import url
from dashboard import views
#import eventcoord
from django.urls import path

app_name = 'dashboard'
urlpatterns = [
	url(r'^$', views.view_dashboard, name='view_dashboard'),
	# path('questions/<int:event_id>/', views.session_data, name='session_data'),
	#url(r'^(?P<event_id>\d+)/addquestion/$',  views.add_question, name='add_question'),
]
