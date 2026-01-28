from ckeditor.fields import RichTextField
from django.db import models


class Apartamento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = RichTextField(verbose_name="Descricao Detalhada")
    preco_diaria = models.DecimalField(max_digits=10, decimal_places=2)
    foto_principal = models.ImageField(upload_to="apartamentos/")
    capacidade_hospedes = models.PositiveIntegerField(default=1)
    link_anuncio = models.URLField(verbose_name="Link do anuncio (airbnb)", blank=True)
    ical_url = models.URLField(verbose_name="Link do calendario (iCal)", blank=True)

    def __str__(self):
        return self.nome


class Foto(models.Model):
    apartamento = models.ForeignKey(
        Apartamento, on_delete=models.CASCADE, related_name="fotos"
    )
    imagem = models.ImageField(upload_to="apartamentos/galeria")

    def __str__(self):
        return f"Foto de {self.apartamento.nome}"


class Indisponibilidade(models.Model):
    apartamento = models.ForeignKey(
        Apartamento, on_delete=models.CASCADE, related_name="bloqueios"
    )
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return f"{self.apartamento.nome} - {self.data_inicio} até {self.data_fim}"
