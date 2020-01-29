from django.shortcuts import render
from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView
from .models import Tasks, Status


def tasks_table(requests):
    tasks = Tasks.objects.all()
    status = Status.objects.all()
    context = {
        'tasks': tasks,
        'status': status,
    }
    return render(requests, 'tasks/tasks_table.html', context=context)


# class TasksCreate(CreateView):
#     model = Tasks
#     fields = '__all__'
#     success_url = reverse_lazy('')


def create_task(requests):
    model = Tasks
    form = TasksForm()
    fields = ['name', 'category', 'status', 'description', 'duedate',
              'importance', ]



def edit_task(requests):
    pass
