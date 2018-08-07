from django.shortcuts import render
from dashboard.forms import NewQuestionForm
from django.contrib.auth.decorators import login_required


# Create your questions here.
# def add_question(request, event_id):
#     """Add new question"""
#    new_question_form = NewQuestionForm()
#    return render(request, 'dashboard/dashboard.html', {})

@login_required
def view_dashboard(request, event_id):
    """dashboard for coordinator."""
    return render(request, 'dashboard/dashboard.html',{'event_id':event_id})

def add_question(request, event_id):
 	new_question_form = NewQuestionForm()
 	return render(request, 'dashboard/dashboard.html', {'form': new_question_form})
