from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from event.models import Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from event.forms import EventForm, NewQuestionForm
from dashboard.views import view_dashboard
import uuid
# Create your views here.


@user_passes_test(lambda u: u.is_ecoord or u.is_superuser)
@login_required
def create_event(request):
    """Create a new event."""
    new_event_form = EventForm()
    if request.method == 'POST':
        response_new_event_form = EventForm(request.POST)
        print(response_new_event_form)
        if response_new_event_form.is_valid():
            event_name = response_new_event_form.cleaned_data['event_name']
            date_event = response_new_event_form.cleaned_data['date_event']
            duration = response_new_event_form.cleaned_data['duration']
            coordinator = request.user
            description = response_new_event_form.cleaned_data['description']
            Event.objects.create(event_name=event_name, timestamp=date_event,
                                 duration=duration, coordinator=coordinator, description=description)
            print("saved event")
            return HttpResponseRedirect(reverse('coord_main_panel'))

        else:
            print("error")
            return render(request, 'event/new_event_form.html', {'form': new_event_form})

    return render(request, 'event/new_event_form.html', {'form': new_event_form})


@user_passes_test(lambda u: u.is_ecoord or u.is_superuser)
@login_required
def edit_event(request, event_id):
    """Edit event."""
    event_details = Event.objects.get(pk=event_id)
    event_data = {	'event_name': event_details.event_name,
                   'date_event': event_details.timestamp,
                   'duration': event_details.duration,
                   'description': event_details.description}
    descriptionfield = event_details.description

    populated_form = EventForm(event_data, initial=event_data)

    if request.method == 'POST':
        changed_event_details = EventForm(request.POST)
        if changed_event_details.is_valid():
            event_name = changed_event_details.cleaned_data['event_name']
            date_event = changed_event_details.cleaned_data['date_event']
            duration = changed_event_details.cleaned_data['duration']
            coordinator = request.user
            description = changed_event_details.cleaned_data['description']
            Event.objects.filter(pk=event_id).update(event_name=event_name, timestamp=date_event,
                                                     duration=duration, coordinator=coordinator, description=description)
            print("saved event")
            return HttpResponseRedirect(reverse('coord_main_panel'))

    return render(request, 'event/edit_event.html', {'form': populated_form})


@login_required
def view_event(request, event_id):
    """View event details."""
    pass


@login_required
def show_event_qr(request, event_id):

    eventuuid = (str(uuid.uuid4())).strip()
    event_details = Event.objects.get(pk=event_id)
    """View Qr code for event."""
    return render(request, 'event/qr.html', {'event_details': event_details, 'eventuuid': eventuuid})


@login_required
def view_dashboard(request, event_id):
    return HttpResponseRedirect(reverse('view_dashboard'))


@login_required
def add_question(request, event_id):
    new_question_form = NewQuestionForm()
    # if request.method == 'POST':

    return render(request, 'event/addquestion.html', {'form': new_question_form})
