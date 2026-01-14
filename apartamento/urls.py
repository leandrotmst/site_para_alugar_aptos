from django.urls import path

from . import views

app_name = "apartamento"

urlpatterns = [
    path("", views.ListaApartamentos.as_view(), name="lista"),
    path("<int:pk>/", views.DetalheApartamento.as_view(), name="detalhe"),
    path("busca/", views.Busca.as_view(), name="busca"),
]
