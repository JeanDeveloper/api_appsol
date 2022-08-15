from rest_framework import serializers


class AreasListSerializer(serializers.Serializer):
    codigo = serializers.DecimalField(max_digits=18, allow_null=False, decimal_places=0)
    area = serializers.CharField(allow_null=True)

    class Meta:
        fields = '__all__'
