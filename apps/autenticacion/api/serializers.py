from rest_framework import serializers

class AutenticacionDNISerializer(serializers.Serializer):
    codigo_personal = serializers.CharField(max_length=255,allow_null=True, allow_blank = True)
    codigo_usuario  = serializers.IntegerField()
    dni             = serializers.CharField(max_length=255,allow_null=True, allow_blank = True)
    nombre          = serializers.CharField(max_length=255,allow_null=True, allow_blank = True)
    p_apellido      = serializers.CharField(max_length=255,allow_null=True, allow_blank = True)
    s_apellido      = serializers.CharField(max_length=255,allow_null=True, allow_blank = True)
    rol             = serializers.IntegerField()
    codigo_cliente  = serializers.CharField(max_length=255,allow_null=True, allow_blank = True)
