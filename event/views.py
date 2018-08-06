from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings

from .models import Event

# Create your views here.
@user_passes_test(lambda u: u.is_ecoord or u.is_superuser)
@login_required
def create_event(request):
    """Create a new event."""
    pass

@user_passes_test(lambda u: u.is_ecoord or u.is_superuser)
@login_required
def edit_event(request, event_id):
    """Edit event."""
    pass

@login_required
def view_event(request, event_id):
    """View event details."""
    event = Event.objects.get(pk=event_id)
    return render(request, 'event/view_event.html', {'event':event, 'SITE_URL': settings.SITE_URL})


@login_required
def show_event_qr(request, event_id):
    """View Qr code for event."""
    pass
