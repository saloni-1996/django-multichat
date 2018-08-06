from django import forms
from django.forms import ModelForm
from event.models import Event

class EventForm(forms.Form):
	event_name = forms.CharField(max_length=200)
	date_event = forms.DateTimeField()
	duration = forms.IntegerField()
	description = forms.CharField(widget=forms.Textarea)
