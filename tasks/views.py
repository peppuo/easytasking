from django.contrib.auth.models import User
from django.shortcuts import redirect, render
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
        print(context, 'context')
        return render(requests, 'tasks/create_task.html', context=context)
    else:
        print('\n REQUESTS', requests)
        print(requests.POST)
        print('\n\nDIR', type(requests.POST))
        task = Tasks()
        # Required fields
        task.tsk_name = requests.POST['tsk_name']
        task.tsk_due_date = requests.POST['tsk_due_date']
        # Fields with default values or that can be empty
        task.tsk_category = Category.objects.filter(pk=requests.POST.get('tsk_category')).first()
        task.tsk_description = requests.POST.get('tsk_description')
        task.tsk_importance = Importance.objects.filter(pk=requests.POST.get('tsk_importance')).first()
        task.tsk_status = Status.objects.filter(pk=requests.POST.get('tsk_status')).first()
        print('\n\nTASK', task)
        task.save()
        print(Tasks.objects.all())
        return redirect(reverse('tasks_table'))


def update_task(requests):
    pass
#         if form.is_valid():
#             # process the data in form.cleaned_data as required (here we just
#             # write it to the model due_back field)
#             book_instance.due_back = form.cleaned_data['renewal_date']
#             book_instance.save()

#             # redirect to a new URL:
#             # reverse() generates a url from a url configuration name plus
#             # any arguments
#             return HttpResponseRedirect(reverse('all-borrowed'))