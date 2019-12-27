from django.shortcuts import render


def render_tasks_table(requests):
    return render(requests, 'tasks_table.html')


def render_add_task(requests):
    pass


def render_edit_task(requests):
    pass
