from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Tasks


def render_tasks_table(requests):
    return render(requests, 'tasks/tasks_table.html')


class TaskCreate(CreateView):
    model = Tasks
    fields = ['name', 'category', 'status', 'description', 'duedate',
              'importance', ]
    success_url = reverse_lazy('')


def render_edit_task(requests):
    pass
