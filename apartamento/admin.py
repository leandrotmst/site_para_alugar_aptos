from django.contrib import admin

from . import models
from .models import Foto


class FotoInLine(admin.TabularInline):
    model = Foto
    extra = 3


class IndisponibilidadeInline(admin.TabularInline):
    model = models.Indisponibilidade
    min_num = 1
    extra = 0
    can_delete = True


class ApartamentoAdmin(admin.ModelAdmin):
    list_display = ["nome", "descricao", "preco_diaria"]
    inlines = [IndisponibilidadeInline, FotoInLine]


admin.site.register(models.Apartamento, ApartamentoAdmin)
admin.site.register(models.Indisponibilidade)
