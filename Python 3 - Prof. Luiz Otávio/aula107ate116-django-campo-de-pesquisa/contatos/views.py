from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from .models import Contato


def index(request):
    # 'objects' é uma propriedade injetada nas Models pelo construtor da classe
    # django.db.models.ModelBase. Trata-se de um objeto para fazer queries.
    # Faz a busca dos Contatos na base de dados
    contatos = Contato.objects.order_by('-id').filter(
        mostrar=True
    )
    paginator = Paginator(contatos, 20)

    page = request.GET.get('page')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def ver_contato(request, contato_id):
    # contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id)

    if not contato.mostrar:
        raise Http404()

    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })


def buscar(request):
    termo = request.GET.get('termo')

    if termo is None or not termo:
        raise Http404()

    # Imita um campo provisório
    campo_nome_completo = Concat('nome', Value(' '), 'sobrenome')

    contatos = Contato.objects.annotate(
        nome_completo=campo_nome_completo  # Cria um campo provisório na Model
    ).filter(
        # Faz o filtro por esse novo campo
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )
    paginator = Paginator(contatos, 20)

    # print(contatos.query)

    page = request.GET.get('page')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/buscar.html', {
        'contatos': contatos
    })
