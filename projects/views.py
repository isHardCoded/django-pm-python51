from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from projects.models import ProjectStatus, Project

@login_required(login_url='login')
def kanban(request):
    context = {
        "status_planning": ProjectStatus.objects.get(name="Планируется"),
        "status_progress": ProjectStatus.objects.get(name="Выполняется"),
        "projects_planning": Project.objects.filter(status=ProjectStatus.objects.get(name="Планируется")),
        "projects_progress": Project.objects.filter(status=ProjectStatus.objects.get(name="Выполняется")),
    }

    return render(request, 'projects/kanban.html', context)

@login_required(login_url='login')
def add(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        status = request.POST["status"]
        date_start = request.POST["date_start"]
        date_end = request.POST["date_end"]

        if title and description and status and date_start and date_end:
            if not Project.objects.filter(title=title).exists():
                Project.objects.create(
                    title=title,
                    description=description,
                    status_id=status,
                    owner_id=request.user.id,
                    date_start=date_start,
                    date_end=date_end)

                return redirect("projects_kanban")
            else:
                error = "Проект с таким названием уже существует"
        else:
            error = "Заполните все поля"

        return render(request, "projects/add-form.html", { "error": error })

    context = {
        "statuses": ProjectStatus.objects.all()
    }

    return render(request, "projects/add-form.html", context)