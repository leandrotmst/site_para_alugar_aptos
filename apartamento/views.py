from datetime import datetime

from django.db.models import Q
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from . import models
from .models import Indisponibilidade


class ListaApartamentos(ListView):
    model = models.Apartamento
    template_name = "apartamento/lista.html"
    context_object_name = "apartamentos"
    paginate_by = 10
    ordering = ["-id"]


class Busca(ListaApartamentos):
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)

        termo = self.request.GET.get("termo")
        checkin = self.request.GET.get("checkin")
        checkout = self.request.GET.get("checkout")
        hospedes = self.request.GET.get("hospedes")

        if termo:
            qs = qs.filter(Q(nome__icontains=termo) | Q(descricao__icontains=termo))

        if hospedes:
            qs = qs.filter(capacidade_hospedes__gte=hospedes)

        if checkin and checkout:
            try:
                d_in = datetime.strptime(checkin, "%Y-%m-%d").date()
                d_out = datetime.strptime(checkout, "%Y-%m-%d").date()

                bloqueados = Indisponibilidade.objects.filter(
                    Q(data_inicio__lt=d_out) & Q(data_fim__gt=d_in)
                ).values_list("apartamento_id", flat=True)

                qs = qs.exclude(id__in=bloqueados)

            except ValueError:
                pass
        return qs


class DetalheApartamento(DetailView):
    model = models.Apartamento
    template_name = "apartamento/detalhe.html"
    context_object_name = "apartamento"
    slug_url_kwarg = "slug"
