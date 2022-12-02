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


class AutenticacionLoginSerializer(serializers.Serializer):
    codigo_usuario      = serializers.IntegerField()
    documento           = serializers.CharField(max_length=255,allow_null=True, allow_blank = True)
    nombres             = serializers.CharField(max_length=255,allow_null=True, allow_blank = True)
    apellidos           = serializers.CharField(max_length=255,allow_null=True, allow_blank = True)
    usuario             = serializers.CharField(max_length=255,allow_null=True, allow_blank = True)
    codigo_cliente      = serializers.CharField(max_length=255,allow_null=True, allow_blank = True)
    codigo_tipo_usuario = serializers.DecimalField(max_digits=18, decimal_places=0)