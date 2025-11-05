from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.models import CustomUser
from projects.models import Project
from tasks.models import TaskStatus, Task

@login_required(login_url='login')
def kanban(request):
    context = {
        "status_planning": TaskStatus.objects.get(name="Планируется"),
        "status_progress": TaskStatus.objects.get(name="Выполняется"),
        "tasks_planning": Task.objects.filter(status=TaskStatus.objects.get(name="Планируется")),
        "tasks_progress": Task.objects.filter(status=TaskStatus.objects.get(name="Выполняется")),
    }

    return render(request, 'tasks/kanban.html', context)

@login_required(login_url='login')
def add(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        status = request.POST["status"]
        assign = request.POST["assign"]
        project = request.POST["project"]
        deadline = request.POST["deadline"]

        if title and description and status and assign and project and deadline:
            if not Task.objects.filter(title=title).exists():
                Task.objects.create(
                    title=title,
                    description=description,
                    status_id=status,
                    owner_id=request.user.id,
                    assign_id=assign,
                    project_id=project,
                    deadline=deadline,
                )

                return redirect("tasks_kanban")
            else:
                error = "Задача с таким названием уже существует"
        else:
            error = "Заполните все поля"

        return render(request, "tasks/add-form.html", { "error": error })

    context = {
        "statuses": TaskStatus.objects.all(),
        "users": CustomUser.objects.all(),
        "projects": Project.objects.all(),
    }

    return render(request, "tasks/add-form.html", context)