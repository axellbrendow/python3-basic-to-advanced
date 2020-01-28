from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Post
from django.db.models import Q, Count, Case, When


class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 6
    context_object_name = 'posts'  # Cria uma variável 'posts' dentro dos templates

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-id').filter(publicado_post=True)
        queryset = queryset.annotate(
            numero_comentarios=Count(
                Case(
                        # model__campo. Nesse caso, o django irá pegar só comentários
                        # relacionados ao post
                    When(comentario__publicado_comentario=True, then=1)
                )
            )
        )

        return queryset


class PostBuscar(PostIndex):
    template_name = 'posts/post_buscar.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        termo = self.request.GET.get('termo')

        if termo:
            queryset = queryset.filter(
                Q(titulo_post__icontains=termo) |
                Q(autor_post__first_name__iexact=termo) |
                Q(data_post__icontains=termo) |
                Q(conteudo_post__icontains=termo) |
                Q(excerto_post__icontains=termo) |
                Q(categoria_post__nome_cat__iexact=termo)
            )

        return queryset


class PostCategoria(PostIndex):
    template_name = 'posts/post_categoria.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        categoria = self.kwargs.get('categoria', None)

        if categoria:                # categoria_post é uma foreign key da Model Post
            queryset = queryset.filter(categoria_post__nome_cat__iexact=categoria)

        return queryset


class PostDetalhes(UpdateView):
    pass
