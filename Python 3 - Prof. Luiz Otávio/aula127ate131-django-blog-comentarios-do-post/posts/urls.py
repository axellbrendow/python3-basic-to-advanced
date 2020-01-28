from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostIndex.as_view(), name='index'),
    path('categoria/<str:categoria>', views.PostCategoria.as_view(), name='post_categoria'),
    path('buscar/', views.PostBuscar.as_view(), name='post_buscar'),
    # É obrigatório usar 'pk' na URL para indicar primary key
    path('post/<int:pk>', views.PostDetalhes.as_view(), name='post_detalhes'),
]
