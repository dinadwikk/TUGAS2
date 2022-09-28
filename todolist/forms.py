from django.forms import ModelForm
from todolist.models import TaskItem

class TaskForm(ModelForm):
    class Meta:
        model = TaskItem
        fields = ['title', 'description']