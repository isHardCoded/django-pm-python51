from django.urls import path
from projects.views import *

urlpatterns = [
    path('kanban/', kanban, name='projects_kanban'),
    path('add/', add, name='projects_add'),
    path('details/<int:project_id>', details, name='projects_details'),
]