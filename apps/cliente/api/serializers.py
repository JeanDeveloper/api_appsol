from rest_framework import serializers

class ServiciosXClienteSerializer(serializers.Serializer):
    codigo               = serializers.DecimalField(max_digits=18, decimal_places=0)
    sede                 = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    codigo_sub_area      = serializers.IntegerField()
    nombre_area          = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    nombre_sub_area      = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    nombre_sucursal      = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    alias_sede           = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    codigo_tipo_servicio = serializers.DecimalField(max_digits=18, decimal_places=0)


class ClientesSerializer(serializers.Serializer):
    codigo       = serializers.DecimalField( max_digits=18, decimal_places= 0 )
    nomb_cliente = serializers.CharField( max_length=255, allow_null=True, allow_blank=True )