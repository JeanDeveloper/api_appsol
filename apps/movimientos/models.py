from django.db import models

class Movimientos(models.Model):
    COD_MOVIMIENTO = models.DecimalField(max_digits=18, decimal_places=0)
    NOMBRES = models.CharField(max_length=250)
    DNI = models.CharField(max_length=25)
    SEXO = models.CharField(max_length=1)
    CARGO = models.CharField(max_length=100)
    EMPRESA = models.CharField(max_length=100)
    FECHA = models.DateTimeField(blank=True, null=True)
    TIPO_INGRESO = models.CharField(max_length=50)
