from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class meta:
        model = Task
        fields = '__all__'
