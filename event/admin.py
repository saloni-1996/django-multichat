from django.contrib import admin

# Register your models here.
from .models import Event, EventSession, QuestionType, Question, Choice

admin.site.register(Event)
admin.site.register(EventSession)
admin.site.register(Question)
admin.site.register(QuestionType)