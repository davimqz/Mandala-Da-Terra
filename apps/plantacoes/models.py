from django.db import models

class Plantacao(models.Model):
    SAF = 'Saf'
    HORTA = 'Horta'
    RUA1 = 'Rua1'
    RUA2 = 'Rua2'
    RUA3 = 'Rua3'
    RUA4 = 'Rua4'
    RUA5 = 'Rua5'

    STATUS_CHOICES_TIPO = [
        (SAF, 'Saf'),
        (HORTA, 'Horta'),
    ]

    STATUS_CHOICES_RUAS = [
        (RUA1, 'Rua1'),
        (RUA2, 'Rua2'),
        (RUA3, 'Rua3'),
        (RUA4, 'Rua4'),
        (RUA5, 'Rua5'),
    ]

    nome = models.CharField(max_length=25, null=True, blank=True)
    tipo = models.CharField(
        max_length=12,
        choices=STATUS_CHOICES_TIPO,
        default=None,
    )
    rua = models.CharField(
        max_length=12,
        choices=STATUS_CHOICES_RUAS,
        default=None,
    )
    data_colheita = models.DateField
    data_regada = models.DateField

    def __str__(self):
        return self.nome

   