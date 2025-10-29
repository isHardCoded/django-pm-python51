from django.shortcuts import render

from tasks.models import TaskStatus, Task


def kanban(request):
    context = {
        "status_planning": TaskStatus.objects.get(name="Планируется"),
        "status_progress": TaskStatus.objects.get(name="Выполняется"),
        "tasks_planning": Task.objects.filter(status=TaskStatus.objects.get(name="Планируется")),
        "tasks_progress": Task.objects.filter(status=TaskStatus.objects.get(name="Выполняется")),
    }

    return render(request, 'tasks/kanban.html', context)