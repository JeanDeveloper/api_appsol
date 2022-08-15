from rest_framework import serializers


class AutorizantesSerializer(serializers.Serializer):
    codigo = serializers.DecimalField(max_digits=18, allow_null=False, decimal_places=0)
    cod_personal = serializers.DecimalField(max_digits=18, allow_null=False, decimal_places=0)
    nombre_personal = serializers.CharField(allow_null=True)
    dni_personal = serializers.CharField(allow_null=True)

    class Meta:
        fields = '__all__'
