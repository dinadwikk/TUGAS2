from django.forms import ModelForm
from todolist.models import TodolistTemplate

class TaskForm(ModelForm):
    class Meta:
        model = TodolistTemplate
        fields = ['title', 'description']