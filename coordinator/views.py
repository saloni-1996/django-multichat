from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from fil_auth.models import CustomUser
from event.models import Event

# Create your views here.
def main_panel(request):
    """Main panel for coordinator."""
    # if request.user.is_authenticated:
    # 	username = request.user.username
    # 	event_list = Event.


def dashboard(request):
    """dashboard for coordinator."""
    pass
