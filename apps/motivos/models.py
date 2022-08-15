from django.db import models


class Motivos(models.Model):
    CODIGO = models.DecimalField(max_digits=18, decimal_places=0)
    TIPO = models.CharField(max_length=255)
