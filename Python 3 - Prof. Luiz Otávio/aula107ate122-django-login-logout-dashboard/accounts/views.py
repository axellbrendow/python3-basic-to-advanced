from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method != 'POST':
        response = render(request, 'accounts/login.html')

    else:
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')

        user = auth.authenticate(request, username=usuario, password=password)

        if not user:
            messages.error(request, 'Usuário ou senha inválidos')
            response = render(request, 'accounts/login.html')

        else:
            auth.login(request, user)
            messages.success(request, 'Login bem sucedido')
            response = redirect('dashboard')

    return response


def logout(request):
    auth.logout(request)
    return redirect('login')


def register(request):
    if request.method != 'POST':
        response = render(request, 'accounts/register.html')

    else:
        # Extrai os campos do formulário
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        passwordConfirm = request.POST.get('password-confirm')

        # Faz as validações
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

        # Checa se alguma validação não passou
        if len(messages.get_messages(request)):  # Havendo alguma mensagem de erro,
            response = render(request, 'accounts/register.html')  # Volta ao registro

        else:
            user = User.objects.create_user(username=usuario, email=email,
                                            password=password, first_name=nome,
                                            last_name=sobrenome)
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Usuário registrado com sucesso')
            response = redirect('login')

    return response


@login_required(redirect_field_name='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
