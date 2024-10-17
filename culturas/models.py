# culturas/models.py
from django.db import models
from django.conf import settings

class Plantacao(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    ruas = models.CharField(max_length=255)
    data_plantacao = models.DateField(null=True, blank=True)
    data_regada = models.DateField(null=True, blank=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)  # Permitir nulo

    def __str__(self):
        return self.nome
