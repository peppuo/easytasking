from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView  #, UpdateView, DeleteView
# from django.forms import formset_factory
from .forms import TasksForm
from .models import Tasks, Status


def render_tasks_table(requests):
    tasks = Tasks.objects.all()
    status = Status.objects.all()
    context = {
        'tasks': tasks,
        'status': status,
    }
    return render(requests, 'tasks/tasks_table.html', context=context)


class TaskCreate(CreateView):
    model = Tasks
    form = TasksForm()
    fields = ['name', 'category', 'status', 'description', 'duedate',
              'importance', ]
    success_url = reverse_lazy('')


def render_edit_task(requests):
    pass
