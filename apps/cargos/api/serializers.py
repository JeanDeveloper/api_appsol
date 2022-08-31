from rest_framework import serializers

class CargosSerializer(serializers.Serializer):
    codigo     = serializers.DecimalField(max_digits=18, decimal_places=0)
    cargo      = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)

