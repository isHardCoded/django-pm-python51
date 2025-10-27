from django.shortcuts import render

from projects.models import ProjectStatus, Project


def kanban(request):
    context = {
        "status_planning": ProjectStatus.objects.get(name="Планируется"),
        "status_progress": ProjectStatus.objects.get(name="Выполняется"),
        "projects_planning": Project.objects.filter(status=ProjectStatus.objects.get(name="Планируется")),
        "projects_progress": Project.objects.filter(status=ProjectStatus.objects.get(name="Выполняется")),
    }

    return render(request, 'projects/kanban.html', context)