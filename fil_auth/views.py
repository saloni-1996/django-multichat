from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import CustomUser

# Create your views here.
@login_required	
def adminpanel(request):
	if request.user.is_authenticated:
		username = request.user.username
		usertype = CustomUser.objects.get(username = username)
		if((usertype.is_admin)):
			request.session['usertype'] = 'admin'
			usertype = CustomUser.objects.all().filter(is_ecoord = True)
			return render(request, 'fil_auth/adminpanel.html', { 'ecoordlist' : usertype})
		if(  (not usertype.is_admin) and(usertype.is_ecoord) ):
			request.session['usertype'] = 'ecoord'
			return HttpResponseRedirect(reverse('ecpanel'))
		if(  (not usertype.is_admin) and (not usertype.is_ecoord) and (usertype.is_presenter)):
			request.session['usertype'] = 'presenter'
			return HttpResponse("is_presenter")
			

# @login_required
# def ecpanel(request):
# 	if request.user.is_authenticated:
# 		return render(request, 'eventcoord/ecpanel.html',{})