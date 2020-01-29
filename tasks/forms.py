from django import forms
from django.contrib.auth.models import User


class TasksForm(forms.Form):
    model = Tasks


class CreateTaskForm(forms.Form):
    pass