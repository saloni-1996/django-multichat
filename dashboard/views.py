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
