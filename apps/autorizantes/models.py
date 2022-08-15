from django.db import models


class Autorizantes(models.Model):

    CODIGO   = models.DecimalField(max_digits=18, decimal_places=0)
    COD_PERS = models.CharField(max_length=255)
    PERSONAL = models.CharField(max_length=255)
    DNI      = models.CharField(max_length=255)
