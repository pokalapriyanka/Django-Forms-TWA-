from django import forms
from app.models import *
from app.views import *

class TopicForm(forms.Form):
    topic_name=forms.CharField()

class WebpageForm(forms.Form):
    topic_name=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField()
    url=forms.URLField()
    email=forms.EmailField()

class AccessRecordForm(forms.Form):
    name=forms.ModelChoiceField(queryset=Webpage.objects.all())
    date=forms.DateField()
    author=forms.CharField()