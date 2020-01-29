from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView
from .models import Category, Importance, Status, Tasks


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
    if requests.method == 'GET':
        categories = Category.objects.all()
        importances = Importance.objects.all()
        status = Status.objects.all()
        context = {
            'categories': categories,
            'importances': importances,
            'status': status,
        }
        return render(requests, 'tasks/create_task.html', context=context)
    else:
        pass

def update_task(requests):
    pass
