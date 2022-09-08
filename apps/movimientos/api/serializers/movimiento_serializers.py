from email.policy import default
from rest_framework import serializers
import datetime

class MovimientosListSerializer(serializers.Serializer):
    cod_movimiento = serializers.DecimalField(max_digits=18, decimal_places=0)
    nombres = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)
    dni = serializers.CharField(max_length=25)
    sexo = serializers.CharField(max_length=1)
    cargo = serializers.CharField(max_length=100, allow_blank=True)
    empresa = serializers.CharField(max_length=100)
    fecha_movimiento = serializers.DateTimeField()
    fecha_salida = serializers.CharField(allow_null=True, allow_blank=True)
    # fecha_salida = serializers.DateTimeField(input_formats=['', 'YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]'], format=['', 'YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]'], required=False, allow_null = True)
    # tipo_ingreso = serializers.CharField(max_length=50, allow_blank=True)
    tipo_personal = serializers.CharField(max_length=50)
    imagen = serializers.CharField(max_length=255)

    class Meta:
        fields = '__all__'


class MovimientoCreateSerializer(serializers.Serializer):
    codigo_personal = serializers.DecimalField(max_digits=18, decimal_places=0)
    codigo_servicio = serializers.DecimalField(max_digits=18, decimal_places=0)
    codigo_tipo_mov = serializers.DecimalField(max_digits=18, decimal_places=0)
    codigo_motivo = serializers.DecimalField(max_digits=18, decimal_places=0)
    codigo_empresa = serializers.DecimalField(max_digits=18, decimal_places=0)
    codigo_autorizadox = serializers.DecimalField(max_digits=18, decimal_places=0)
    fecha_mov = serializers.DateTimeField(allow_null=True, default=datetime.time())
    observaciones = serializers.CharField(allow_null=True, allow_blank=True)
    tipo_mov = serializers.CharField(allow_blank=True, allow_null=True)
    creado_por = serializers.CharField(allow_blank=True, allow_null=True)
    creado_por = serializers.CharField(allow_blank=True, allow_null=True)
    codigo_area = serializers.DecimalField(max_digits=18, decimal_places=0, allow_null=True)
    num_pase = serializers.CharField(max_length=10, allow_null=True, allow_blank=True, default="00")
    temperatura = serializers.CharField(max_length=10, allow_null=True, allow_blank=True)
