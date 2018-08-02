from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from fil_auth.models import CustomUser

@login_required
def main_panel(request):
	if request.user.is_authenticated:
		username = request.user.username
		usertype = CustomUser.objects.get(username = username)
		if((usertype.is_admin)):
			request.session['usertype'] = 'admin'
			ecoord_list = CustomUser.objects.all().filter(is_ecoord = True)
			return render(request, 'fil_auth/adminpanel.html', { 'ecoordlist' : ecoord_list})
