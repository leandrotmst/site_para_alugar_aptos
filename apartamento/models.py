from django.db import models


class Apartamento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco_diaria = models.DecimalField(max_digits=10, decimal_places=2)
    foto_principal = models.ImageField(upload_to="apartamentos/")

    def __str__(self):
        return self.nome


class Indisponibilidade(models.Model):
    apartamento = models.ForeignKey(
        Apartamento, on_delete=models.CASCADE, related_name="bloqueios"
    )
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return f"{self.apartamento.nome} - {self.data_inicio} até {self.data_fim}"
