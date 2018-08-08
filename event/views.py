from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from event.models import Event, Question, QuestionType,Choice
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from event.forms import EventForm, NewQuestionForm
from dashboard.views import view_dashboard
import uuid
import json
from django.http import JsonResponse
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
    print("eventcall")
    questions_list = Event.question_set.get(pk=event_id)
    print(questions_list)
    return HttpResponseRedirect(reverse('view_dashboard', kwargs={'questions_list': questions_list}))


@login_required
def add_question(request, event_id):
    new_question_form = NewQuestionForm()
    if request.method == 'POST':
        # print(request.POST.get('question_name'))
        # print(request.POST.get('is_active'))
        question_type = request.POST.get('question_type')
        # print(question_type)
        question_type_name = QuestionType.objects.get(pk=question_type)
        # print(question_type_name)
        question_text = request.POST.get('question_name')
        is_active = request.POST.get('is_active')
        is_mandatory = request.POST.get('is_mandatory')
        #question_type_ = question_type_name
        event = event_id
        question = Question.objects.create(question_text=question_text, event_id=event, is_active=is_active, is_mandatory=is_mandatory,
            question_type=question_type_name)


        form_data= request.POST

            # If the question type is single or multiple save the choice with choice text that can be accessed from post params ("choice_(some int)")
        if question_type_name == "Single Choice" or question_type_name == "Multiple Choice":
            for key in form_data:
                print(key)
                print(form_data[key])
                if key.startswith('choice'):
                        # create a choice
                    choice = Choice(choice_text=form_data[key], question= question)
                    choice.save()
        else:
            # create choices for rating
            # 1 star corresponds to choice with text 1
            # 2 star corresponds to choice with text 2
            # and so on... till 5 star
            for i in range(5):
            # create a choice
                choice = Choice(choice_text=str(i+1), question=question)
                choice.save()


        print("question save")
        return HttpResponseRedirect(reverse('view_dashboard', kwargs={'event_id': event_id}))

    return render(request, 'event/addquestion.html', {'form': new_question_form})


def toggle_status(request, question_id):
    print("toggle")
    print(request.method)
    if request.method == 'POST' and request.is_ajax():
        print("accesd")
        print(question_id)
        try:
            question = Question.objects.get(pk=question_id)
            if question.is_active:
                Question.objects.filter(pk=question_id).update(is_active=False)
                return JsonResponse({'status': 'Success', 'msg': 'Fasle successfully'})
            else:
                Question.objects.filter(pk=question_id).update(is_active=True)
                return JsonResponse({'status': 'Success', 'msg': 'true successfully'})

            #return JsonResponse({'status': 'Success', 'msg': 'save successfully'})
        except Question.DoesNotExist:
            return JsonResponse({'status': 'Fail', 'msg': 'Object does not exist'})
    else:
        return JsonResponse({'status': 'Fail', 'msg': 'Not a valid request'})
