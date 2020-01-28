from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostIndex.as_view(), name='index'),
    path('categoria/<str:categoria>', views.PostCategoria.as_view(), name='post_categoria'),
    path('buscar/', views.PostBuscar.as_view(), name='post_buscar'),
    path('post/<int:id>', views.PostDetalhes.as_view(), name='post_detalhes'),
]
