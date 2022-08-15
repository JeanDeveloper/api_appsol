from rest_framework import serializers


class MotivosListSerializer(serializers.Serializer):
    codigo = serializers.DecimalField(max_digits=18, decimal_places=0)
    tipo = serializers.CharField(allow_null=True)

    class Meta:
        fields= '__all__'

