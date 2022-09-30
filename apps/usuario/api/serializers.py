from rest_framework import serializers

class UsuarioPermisosSerializer(serializers.Serializer):

    codigo_relacion = serializers.DecimalField(max_digits=18, decimal_places=0)
    codigo_accion   = serializers.DecimalField(max_digits=18, decimal_places=0)
    codigo_alcance  = serializers.DecimalField(max_digits=18, decimal_places=0)
