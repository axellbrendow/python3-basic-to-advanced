from django.db import models
from categorias.models import Categoria
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.conf import settings
import os


class Post(models.Model):
    titulo_post = models.CharField(max_length=255, verbose_name='Título')
    autor_post = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name='Autor'
    )
    data_post = models.DateTimeField(default=timezone.now, verbose_name='Data')
    conteudo_post = models.TextField(verbose_name='Conteúdo')
    excerto_post = models.TextField(verbose_name='Excerto')
    categoria_post = models.ForeignKey(
        Categoria, on_delete=models.DO_NOTHING, blank=True,
        null=True, verbose_name='Categoria'
    )
    imagem_post = models.ImageField(
        upload_to='post_img/%Y/%m/%d', blank=True, null=True, verbose_name='Imagem'
    )
    publicado_post = models.BooleanField(default=False, verbose_name='Publicado')

    def __str__(self):
        return self.titulo_post

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save(force_insert, force_update, using, update_fields)

        self.redimensionar_imagem(self.imagem_post.name, 800)

    @staticmethod
    def redimensionar_imagem(nome_imagem, nova_largura):
        caminho_imagem = os.path.join(settings.MEDIA_ROOT, nome_imagem)
        imagem = Image.open(caminho_imagem)

        largura, altura = imagem.size
        nova_altura = round(nova_largura * altura / largura)

        if largura > nova_largura:
            nova_imagem = imagem.resize((nova_largura, nova_altura), Image.ANTIALIAS)
            nova_imagem.save(
                caminho_imagem,
                optimize=True,
                quality=60
            )
            nova_imagem.close()

        imagem.close()
