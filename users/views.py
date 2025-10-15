from django.shortcuts import render

def register(request):
    return render(request, "users/sign_up.html")