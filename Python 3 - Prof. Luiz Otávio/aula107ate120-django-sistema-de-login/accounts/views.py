from django.shortcuts import render
from django.contrib import messages


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/logout.html')


def register(request):
    messages.add_message(request, messages.SUCCESS, 'Hello World!')
    return render(request, 'accounts/register.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
