from django.contrib import admin
from tasks.models import Task, TaskStatus

admin.site.register(TaskStatus)
admin.site.register(Task)