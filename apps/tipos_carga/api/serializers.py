from unicodedata import decimal
from rest_framework import serializers

class TiposCargaListSerializer(serializers.Serializer):
    codigo_carga = serializers.DecimalField(max_digits=18, decimal_places=0)
    carga     = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)

    class Meta:
        fields = '__all__'