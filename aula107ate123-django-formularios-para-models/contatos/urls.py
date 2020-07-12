from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buscar/', views.buscar, name='buscar'),
    path('<int:contato_id>', views.ver_contato, name='ver_contato'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
