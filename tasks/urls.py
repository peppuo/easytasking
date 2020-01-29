from django.urls import path
from tasks.views import create_task, tasks_table, update_task

urlpatterns = [
    path('', tasks_table, name='tasks_table'),
    # path('create/', TasksCreate.as_view(), name='tasks_create'),
    path('create/', create_task, name='create_task'),
    path('update/', update_task, name='update_task'),
]
