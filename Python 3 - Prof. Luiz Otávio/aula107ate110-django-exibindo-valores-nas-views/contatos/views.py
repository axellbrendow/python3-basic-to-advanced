from django.shortcuts import render
from .models import Contato


def index(request):
    contatos = Contato.objects.all()  # Faz um select em todos os contatos

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })
