from django.urls import path, include
from presenter import views

urlpatterns = [
	path(r'^$', views.dashboard, name='presenter_dashboard'),
]
