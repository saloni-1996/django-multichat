from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, reverse

from event.models import Event


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


def dashboard(request):
    """dashboard for coordinator."""
    pass
