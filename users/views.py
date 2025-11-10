from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.shortcuts import render, redirect
from users.models import CustomUser

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if username and email and password:
            if not CustomUser.objects.filter(username=username, email=email).exists():
                CustomUser.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )

                return redirect('login')
            else:
                error = "Пользователь с таким именем или почтой уже существует"
        else:
            error = "Заполните все поля"

        return render(request, "users/sign_up.html", {"error": error})

    return render(request, "users/sign_up.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = authenticate(request, username=username, password=password)

            if user:
                user_login(request, user)
                return redirect('projects_kanban')
            else:
                error = "Неверный логин или пароль"
        else:
            error = "Заполните поля"

        return render(request, 'users/sign_in.html', {"error": error})

    return render(request, 'users/sign_in.html')

def logout(request):
    user_logout(request)
    return redirect('login')