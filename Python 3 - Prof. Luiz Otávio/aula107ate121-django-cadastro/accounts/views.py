from django.shortcuts import render
from django.contrib import messages


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/logout.html')


def register(request):
    response = render(request, 'accounts/register.html')

    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        passwordConfirm = request.POST.get('password-confirm')

        if not nome or not sobrenome or not email or not usuario or not password or\
                not passwordConfirm:
            messages.add_message(request, messages.ERROR, 'Nenhum campo pode estar vazio')
            response = render(request, 'accounts/register.html')

        else:
            pass

    return response


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
