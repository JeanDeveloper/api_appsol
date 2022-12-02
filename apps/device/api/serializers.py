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


class RelacionDispositivoServicioSerializer(serializers.Serializer):
    codigo_dispositivo   = serializers.IntegerField(),
    codigo_servicio      = serializers.IntegerField(),
    codigo_cliente       = serializers.CharField(max_length=50),
    codigo_sub_area      = serializers.IntegerField(),
    nombre_area          = serializers.CharField(max_length=50),
    nombre_sub_area      = serializers.CharField(max_length=50),
    nombre_sucursal      = serializers.CharField(max_length=50),
    nombre_cliente       = serializers.CharField(max_length=50),
    alias_sede           = serializers.CharField(max_length=50),
    codigo_tipo_servicio = serializers.IntegerField(),
    codigo_puesto        = serializers.DecimalField(max_digits=18, decimal_places=0)
    nombre_puesto        = serializers.CharField(max_length=255, allow_null = True, allow_blank = True)
    codigo_perfil        = serializers.DecimalField(max_digits=18, decimal_places=0)
