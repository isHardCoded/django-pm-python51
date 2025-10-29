from django.db import models

from projects.models import Project
from users.models import CustomUser

class TaskStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE)
    assign = models.ForeignKey(CustomUser, related_name="assigned_tasks", on_delete=models.CASCADE)
    owner = models.ForeignKey(CustomUser, related_name="owned_tasks", on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True)