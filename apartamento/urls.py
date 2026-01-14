from django.urls import path

from . import views

urlpatterns = [
    path("", views.ListaApartamentos, name="lista"),
    path("<slug>", views.DetalheApartamento.as_view(), name="detalhe"),
    path("busca/", views.Busca.as_view(), name="busca"),
]
