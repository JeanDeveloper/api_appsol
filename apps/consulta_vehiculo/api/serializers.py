from rest_framework import serializers

class ConsultaVehiculoSerializer(serializers.Serializer):
    codigo_vehiculo            = serializers.DecimalField(max_digits=18, decimal_places=0)
    codigo_empresa             = serializers.DecimalField(max_digits=18, decimal_places=0)
    empresa                    = serializers.CharField(max_length= 100, allow_null=True, allow_blank=True)
    codigo_tipo_vehiculo       = serializers.DecimalField(max_digits=18, decimal_places=0)
    tipo_vehiculo              = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)
    placa                      = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)
    tarjeta_propiedad          = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)
    ultimo_movimiento          = serializers.DecimalField(max_digits=18, decimal_places=0)
    codigo_carreta             = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)
    codigo_carga               = serializers.DecimalField(max_digits=18, decimal_places=0)
    dni_conductor              = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)
    codigo_autorizante         = serializers.DecimalField(max_digits=18, decimal_places=0)
    codigo_motivo              = serializers.DecimalField(max_digits=18, decimal_places=0)
    ultimo_movimiento_peatonal = serializers.DecimalField(max_digits=18, decimal_places=0)
    codigo_productor           = serializers.DecimalField(max_digits=18, decimal_places=0)
    tipo_traslado              = serializers.DecimalField(max_digits=18, decimal_places=0)
    nombre_conductor           = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)

class VerificacionVehiculoSerializer(serializers.Serializer):
    valor   = serializers.DecimalField( max_digits=18, decimal_places=0)
    mensaje = serializers.CharField( max_length=100,  allow_null=True,  allow_blank=True )
    marca   = serializers.CharField( max_length=100,  allow_null=True,  allow_blank=True )
    codigo  = serializers.DecimalField(max_digits=18, decimal_places=0)