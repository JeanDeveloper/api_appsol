from rest_framework import serializers


class EmpresasSerializer(serializers.Serializer):
    codigo = serializers.DecimalField(max_digits=18, decimal_places=0)
    empresa = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)


