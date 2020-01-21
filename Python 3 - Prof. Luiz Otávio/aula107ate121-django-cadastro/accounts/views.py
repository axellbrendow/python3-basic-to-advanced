from django.shortcuts import render
from django.contrib import messages
from django.core.validators import validate_email


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/logout.html')


def register(request):
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

        else:
            try:
                validate_email(email)

            except:
                messages.add_message(request, messages.ERROR, 'Email inválido')

            if len(password) < 6:
                messages.add_message(request, messages.ERROR, 'Senha precisa ter 6 ou mais caracteres')

            if len(passwordConfirm) < 6:
                messages.add_message(request, messages.ERROR, 'Senha precisa ter 6 ou mais caracteres')

            if password != passwordConfirm:
                messages.add_message(request, messages.ERROR, 'Senhas não conferem')

    response = render(request, 'accounts/register.html')

    return response


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
