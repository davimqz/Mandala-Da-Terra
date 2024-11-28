from django.db import models
from datetime import timedelta


from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    rua = models.TextField(default='Rua desconhecida')
    completed = models.BooleanField(default=False)
    data_plantio = models.DateField(null=True, blank=True)  # Data de plantio
    data_colheita = models.DateField(null=True, blank=True)  # Data de colheita

    def __str__(self):
        return self.title

    


from django.db import models

class Cultura(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    tempo_colheita_dias = models.IntegerField(default=90)  # Tempo médio de colheita em dias

    def __str__(self):
        return self.nome

class PlantaCompanheira(models.Model):
    cultura = models.ForeignKey(Cultura, on_delete=models.CASCADE, related_name='companheiras')
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


