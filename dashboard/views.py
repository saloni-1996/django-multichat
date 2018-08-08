from django.shortcuts import get_object_or_404, render
from event.models import Event, Question
from dashboard.forms import NewQuestionForm
from django.contrib.auth.decorators import login_required
import json



# Create your questions here.
# def add_question(request, event_id):
#     """Add new question"""
#    new_question_form = NewQuestionForm()
#    return render(request, 'dashboard/dashboard.html', {})

@login_required
def view_dashboard(request, event_id):
    """dashboard for coordinator."""
    print("dashboardcall")
    new_question_form = NewQuestionForm()
    event = get_object_or_404(Event, pk=event_id)
    # add try catch part
    questions_list = event.question_set.all()
    return render(request, 'dashboard/dashboard.html', {'event_id': event_id, 'questions_list': questions_list ,'form': new_question_form})

@login_required
def session_data(request, event_id):
    custom_user = request.user

    event = custom_user.event_set.get(pk=event_id)

    session_response = {}

    question_list = []
    for question in event.question_set.all():
        question_obj = {'question_id': question.id, 'question': question.question_text,
                        'question_type': question.question_type.question_type}

        option_array = []

        for choice in question.choice_set.all():
            choice_obj = {'votes': choice.vote_count, 'text': choice.choice_text, 'id': choice.id}
            option_array.append(choice_obj)

        question_obj['options'] = option_array

        question_list.append(question_obj)

    session_response['questions'] = question_list

    return JsonResponse(session_response, safe=False)