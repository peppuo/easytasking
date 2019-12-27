from django.urls import path
from tasks.views import render_tasks_table


urlpatterns = [
    path('', render_tasks_table, name='tasks_table'),
]
