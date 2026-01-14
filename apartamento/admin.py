from django.contrib import admin

from . import models


class IndisponibilidadeInline(admin.TabularInline):
    model = models.Indisponibilidade
    min_num = 1
    extra = 0
    can_delete = True


class ApartamentoAdmin(admin.ModelAdmin):
    list_display = ["nome", "descricao", "diaria"]
    inlines = [IndisponibilidadeInline]


admin.site.register(models.Apartamento, ApartamentoAdmin)
admin.site.register(models.Indisponibilidade)
