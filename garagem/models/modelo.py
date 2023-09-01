from django.db import models

from garagem.models import Marca, Categoria

class Modelo(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="modelos"
    )
    marca = models.ForeignKey(
        Marca, on_delete=models.PROTECT, related_name="modelos"
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Modelos"

