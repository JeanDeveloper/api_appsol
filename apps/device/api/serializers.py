from rest_framework import serializers

class RegistrarDispositivoSerializer(serializers.Serializer):
    codigo_dispositivo  = serializers.DecimalField(max_digits=18, decimal_places=0)
    serial              = serializers.CharField(max_length=50)
    hardware            = serializers.CharField(max_length=50)
    modelo              = serializers.CharField(max_length=50)
    fabricante          = serializers.CharField(max_length=50)
    numero              = serializers.CharField(max_length=50)
    fecha_creacion      = serializers.DateTimeField()
    estado              = serializers.BooleanField()
    sdk                 = serializers.IntegerField()
    incremental         = serializers.CharField(max_length=50)
    dispositivo         = serializers.CharField(max_length=50)
    compilacion         = serializers.CharField(max_length=50)
    id_dispositivo      = serializers.CharField(max_length=50)
    version_api         = serializers.CharField(max_length=50)



class ConsultarEstadoSerializer(serializers.Serializer):
    estadoId = serializers.DecimalField(max_digits=18, decimal_places=0)



