from django.urls import path
from tasks.views import *

urlpatterns = [
    path('kanban/', kanban, name='tasks_kanban'),
    path('table/', table, name='tasks_table'),
    path('add/', add, name='tasks_add'),
]