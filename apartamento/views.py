from django.db.models import Q
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from . import models


class ListaApartamentos(ListView):
    model = models.Apartamento
    template_name = "apartamentos/lista.html"
    context_object_name = "apartamentos"
    paginate_by = 10
    ordering = ["-id"]


class Busca(ListaApartamentos):
    def get_queryset(self, *args, **kwargs):
        termo = self.request.GET.get("termo") or self.request.session["termo"]
        qs = super().get_queryset(*args, **kwargs)

        if not termo:
            return qs

        self.request.session["termo"] = termo

        qs = qs.filter(
            Q(nome__icontains=termo)
            | Q(descricao_curta__icontains=termo)
            | Q(descricao_longa__icontains=termo)
        )

        self.request.session.save()
        return qs


class DetalheApartamento(DetailView):
    model = models.Apartamento
    template_name = "apartamentos/detalhe.html"
    context_object_name = "apartamentos"
    slug_url_kwarg = "slug"
