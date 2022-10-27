from rest_framework import serializers

class FotosAccesoSerializer(serializers.Serializer):
    foto_id = serializers.DecimalField(max_digits=18, decimal_places=0)
    nombre = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    extension = serializers.CharField(max_length=10, allow_null=True, allow_blank=True)
    tipo_dato_acceso = serializers.IntegerField()
    tamanio =serializers.IntegerField()
    fecha_creacion = serializers.DateTimeField()
    creado_por  = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)
    ubicacion = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
