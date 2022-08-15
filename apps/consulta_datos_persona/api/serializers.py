from rest_framework import serializers


class ConsultaDatosPersonaSerializer(serializers.Serializer):
    valor = serializers.DecimalField(max_digits=18, decimal_places=0)
    mensaje = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    cod_autorizacion= serializers.DecimalField(max_digits=18, decimal_places=0)
    cod_motivo = serializers.DecimalField(max_digits=18, decimal_places=0)
    cod_autorizante = serializers.DecimalField(max_digits=18, decimal_places=0)
    cod_area = serializers.DecimalField(max_digits=18, decimal_places=0)
    emo_fv = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    sctr_pension_fv = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    sctr_salud_fv = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    fi_autorizacion = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    fv_autorizacion = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)

