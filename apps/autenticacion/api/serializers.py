from rest_framework import serializers

class AutenticacionDNISerializer(serializers.Serializer):
    codigo_personal     = serializers.CharField(max_length=255,allow_null=True, allow_blank = True)
    dni                 = serializers.CharField(max_length=255,allow_null=True, allow_blank = True)
    p_nombre            = serializers.CharField(max_length=255,allow_null=True, allow_blank = True)
    s_nombre            = serializers.CharField(max_length=255,allow_null=True, allow_blank = True)
    p_apellido          = serializers.CharField(max_length=255,allow_null=True, allow_blank = True)
    s_apellido          = serializers.CharField(max_length=255,allow_null=True, allow_blank = True)
    cargo               = serializers.CharField(max_length=255,allow_null=True, allow_blank = True)
    cod_tipo_usuario    = serializers.DecimalField(max_digits=18, decimal_places=0)