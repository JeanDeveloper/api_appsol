from django.db import models

class Dispositivo(models.Model):
    codigo_dispositivo  = models.DecimalField(max_digits=18, decimal_places=0)
    serial              = models.CharField(max_length=50)
    hardware            = models.CharField(max_length=50)
    modelo              = models.CharField(max_length=50)
    fabricante          = models.CharField(max_length=50)
    numero              = models.CharField(max_length=50)
    fecha_creacion      = models.DateTimeField()
    estado              = models.BooleanField()
    sdk                 = models.IntegerField()
    incremental         = models.CharField(max_length=50)
    dispositivo         = models.CharField(max_length=50)
    compilacion         = models.CharField(max_length=50)
    id_dispositivo      = models.CharField(max_length=50)
    version_api         = models.CharField(max_length=50)
