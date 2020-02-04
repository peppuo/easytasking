from django import forms
from django.contrib.auth.models import User
from tasks.models import Tasks


class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'


class EditStatusForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['tsk_status', ]
