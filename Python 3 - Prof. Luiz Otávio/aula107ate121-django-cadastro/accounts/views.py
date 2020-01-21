from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.contrib.auth.models import User


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

        try:
            validate_email(email)

        except:
            messages.add_message(request, messages.ERROR, 'Email inválido')

        if User.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR, 'E-mail já existe')

        if len(usuario) < 6:
            messages.add_message(request, messages.ERROR,
                                 'Usuário precisa ter 6 ou mais caracteres')

        if User.objects.filter(username=usuario).exists():
            messages.add_message(request, messages.ERROR, 'Usuário já existe')

        if len(password) < 6:
            messages.add_message(request, messages.ERROR,
                                 'Senha precisa ter 6 ou mais caracteres')

        if password != passwordConfirm:
            messages.add_message(request, messages.ERROR, 'Senhas não conferem')

        if len(messages.get_messages(request)):  # Havendo alguma mensagem de erro,
            response = render(request, 'accounts/register.html')  # Volta ao registro

        else:
            messages.add_message(request, messages.SUCCESS, 'Usuário registrado com sucesso')

            user = User.objects.create_user(username=usuario, email=email,
                                            password=password, first_name=nome,
                                            last_name=sobrenome)
            user.save()
            response = redirect('login')

    else:
        response = render(request, 'accounts/register.html')

    return response


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
