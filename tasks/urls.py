from django.urls import path
from tasks.views import *

urlpatterns = [
    path('kanban/', kanban, name='tasks_kanban'),
]