from django.urls import path
from projects.views import *

urlpatterns = [
    path('kanban/', kanban, name='projects_kanban'),
]