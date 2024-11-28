from django.db import models
from django.conf import settings
from datetime import datetime
import pytz

class Nota(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        # Define o fuso horário de Brasília
        fuso_brasilia = pytz.timezone('America/Sao_Paulo')

        # Salva a data e hora de Brasília no campo data_criacao
        if not self.id:  # Apenas para novas instâncias
            self.data_criacao = datetime.now(fuso_brasilia)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.conteudo[:50]  # Exibe os primeiros 50 caracteres da anotação
