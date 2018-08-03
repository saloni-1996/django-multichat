from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from fil_auth.models import CustomUser
from event.models import Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_ecoord or u.is_superuser)
@login_required
def main_panel(request):
    """Main panel for coordinator."""
    # if request.user.is_authenticated:
    # 	username = request.user.username
    # 	event_list = Event.


@user_passes_test(lambda u: u.is_ecoord or u.is_superuser)
@login_required
def dashboard(request):
    """dashboard for coordinator."""
    pass
