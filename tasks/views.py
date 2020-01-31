from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404,redirect, render
from django.urls import reverse, reverse_lazy
# from django.views.generic.edit import CreateView
from tasks.models import Category, Importance, Status, Tasks


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
        task = Tasks()

        # Required fields
        task.tsk_name = requests.POST['tsk_name']
        task.tsk_due_date = requests.POST['tsk_due_date']

        # Fields with default values or values that can be empty
        task.tsk_description = requests.POST.get('tsk_description')
        try:
            task.tsk_category = Category.objects.get(pk=requests.POST['tsk_category'])
        except Category.DoesNotExist:
            task.tsk_category = Category.objects.get(pk=3)
        try:
            task.tsk_importance = Importance.objects.get(pk=requests.POST['tsk_importance'])
        except Importance.DoesNotExist:
            task.tsk_importance = Importance.objects.get(pk=3)
        try:
            task.tsk_status = Status.objects.get(pk=requests.POST['tsk_status'])
        except Status.DoesNotExist:
            task.tsk_status = Status.objects.get(pk=1)

        task.save()

        return redirect(reverse('tasks_table'))


def update_task(requests, pk):
    if requests.method == 'GET':
        task = get_object_or_404(Tasks, pk=pk)
        categories = Category.objects.all()
        importances = Importance.objects.all()
        status = Status.objects.all()
        context = {
            'task': task,
            'categories': categories,
            'importances': importances,
            'status': status,
        }
        return render(requests, 'tasks/update_task.html', context=context)
    else:
        task = get_object_or_404(Tasks, pk=pk)
        task.tsk_name = requests.POST['tsk_name']
        task.tsk_due_date = requests.POST['tsk_due_date']
        task.tsk_description = requests.POST.get('tsk_description')
        task.tsk_category = Category.objects.get(pk=requests.POST['tsk_category'])
        task.tsk_importance = Importance.objects.get(pk=requests.POST['tsk_importance'])
        task.tsk_status = Status.objects.get(pk=requests.POST['tsk_status'])
        task.save()

        return redirect(reverse('tasks_table'))
