from django.db import models
from fil_auth.models import CustomUser

# Create your models here.
class Event(models.Model):
    """
    Events Model
    """
    event_name = models.CharField(max_length=200)
    timestamp = models.DateTimeField()
    duration = models.IntegerField()
    coordinator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)


class EventSession(models.Model):
    """
    Event Session model
    """
    session_name = models.CharField(max_length=200)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='session_set')
    # Event Presenter
    presenter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class QuestionType(models.Model):
    question_type = models.CharField(max_length=100)


class Question(models.Model):
    """
    is_active,is_mandatory if True will displayed on userpage and mandatory
    """
    question_text = models.CharField(max_length=500, null=False)
    # TODO: Replace class name for seesion in event/models.py.
    session = models.ForeignKey(EventSession, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    is_mandatory = models.BooleanField(default=False)
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)




class Choice(models.Model):
    """There will be three type of choices->
    multi-select,single choice&rating corresponding to any question_id.
    """
    choice_text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    vote_count = models.IntegerField(default=0)
