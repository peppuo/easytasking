from django.urls import path
from tasks.views import TaskCreate, render_tasks_table


urlpatterns = [
    path('', render_tasks_table, name='tasks_table'),
    path('create/', TaskCreate.as_view(), name='tasks_create'),
]
