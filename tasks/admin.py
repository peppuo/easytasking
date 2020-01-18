from django.contrib import admin

from tasks.models import Category, Importance, Status, Tasks

admin.site.register(Category)
admin.site.register(Importance)
admin.site.register(Status)
admin.site.register(Tasks)
