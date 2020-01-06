from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Contato


def index(request):
    contatos = Contato.objects.all()  # Faz um select em todos os contatos
    paginator = Paginator(contatos, 20)

    page = request.GET.get('page')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def ver_contato(request, contato_id):
    # contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id)

    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })
