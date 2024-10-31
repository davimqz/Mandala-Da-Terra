from django.db import models
from django.conf import settings


class Nota(models.Model):
    titulo = models.CharField(max_length=25)
    conteudo = models.TextField(max_length=100)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
