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

    # check if the user is authenticated
    if request.user.is_authenticated:
        custom_user = request.user

        if custom_user.is_admin:
            event_list = Event.objects.all()
            # flag is used to give option for the user to the edit event
            return render(request, "coordinator/index.html", {'event_list': event_list, 'flag': True})
        else:
            # TODO: Redirect to login page
            return HttpResponse("Login Page")
    else:
        # TODO: Redirect to login page
        return HttpResponse("Login Page")


@user_passes_test(lambda u: u.is_ecoord or u.is_superuser)
@login_required
def dashboard(request):
    """dashboard for coordinator."""
    pass
