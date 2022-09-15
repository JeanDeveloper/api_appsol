from rest_framework import serializers

class MovimientosCargoSerializer(serializers.Serializer):
    cod_movimiento  = serializers.DecimalField(max_digits=18, decimal_places=0)
    codigo_vehicular= serializers.DecimalField(max_digits=18, decimal_places=0)
    placa           = serializers.CharField(max_length=20)
    tipo_carga      = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)
    nombres         = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    dni             = serializers.CharField(max_length=25,  allow_null=True, allow_blank=True)
    cargo           = serializers.CharField(max_length=100,  allow_null=True, allow_blank=True)
    empresa         = serializers.CharField(max_length=100,  allow_null=True, allow_blank=True)
    fecha_ingreso   = serializers.DateTimeField(allow_null = True)
    fecha_salida    = serializers.CharField(allow_null=True, allow_blank=True)

    # fecha_salida    = serializers.DateTimeField(allow_null = True)

    class Meta:
        fields = '__all__'