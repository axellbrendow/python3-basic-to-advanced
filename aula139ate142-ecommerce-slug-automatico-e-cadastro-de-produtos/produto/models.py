from django.db import models
from PIL import Image
from django.conf import settings
from django.utils.text import slugify

import os

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(
        upload_to='produto_imagens/%Y/%m', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    preco_marketing = models.FloatField(verbose_name='Preço')
    preco_marketing_promocional = models.FloatField(default=0, verbose_name='Preço Promo.')
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variável'),
            ('S', 'Simples'),
        )
    )

    def get_preco_formatado(self):
        return f'R$ {self.preco_marketing:.2f}'.replace('.', ',')

    get_preco_formatado.short_description = 'Preço'

    def get_preco_promocional_formatado(self):
        return f'R$ {self.preco_marketing_promocional:.2f}'.replace('.', ',')

    get_preco_promocional_formatado.short_description = 'Preço Promo.'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.slug:
            self.slug = f'{slugify(self.nome)}'

        super().save(force_insert, force_update, using, update_fields)

        if self.imagem:
            self.redimensionar_imagem(self.imagem.name, 800)

    @staticmethod
    def redimensionar_imagem(nome_imagem, nova_largura):
        caminho_imagem = os.path.join(settings.MEDIA_ROOT, nome_imagem)
        imagem = Image.open(caminho_imagem)

        largura, altura = imagem.size
        nova_altura = round(nova_largura * altura / largura)

        if largura > nova_largura:
            nova_imagem = imagem.resize(
                (nova_largura, nova_altura), Image.ANTIALIAS)
            nova_imagem.save(
                caminho_imagem,
                optimize=True,
                quality=60
            )
            nova_imagem.close()

        imagem.close()

    def __str__(self):
        return self.nome


class Variacao(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    estoque = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nome or self.produto.nome

    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'
