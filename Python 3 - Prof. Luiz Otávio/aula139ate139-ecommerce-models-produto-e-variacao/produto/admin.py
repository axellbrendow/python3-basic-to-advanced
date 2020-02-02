from django.contrib import admin
from .models import Produto
from .models import Variacao


class VariacaoInline(admin.TabularInline):
    models = models.Variacao
    extra = 1


class ProdutoAdmin(admin.ModelAdmin):
    inlines = [
        VariacaoInline
    ]


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Variacao)
