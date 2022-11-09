from rest_framework import serializers

class DatosAccesoSerializer(serializers.Serializer):
    codigo_datos_acceso     = serializers.DecimalField(max_digits=18, allow_null = False, decimal_places = 0 )
    codigo_movimiento       = serializers.DecimalField(max_digits=18, allow_null = False, decimal_places = 0 )
    guia_movimiento         = serializers.CharField(allow_null = True, allow_blank = True)
    foto_guia_movimiento    = serializers.CharField(allow_null = True, allow_blank = True)
    material_movimiento     = serializers.CharField(allow_null = True, allow_blank = True)
    foto_material_movimiento= serializers.CharField(allow_null = True, allow_blank = True)
    fecha_creacion          = serializers.DateTimeField()

class DatosAccesoSalidaSerializer(serializers.Serializer):
    cod_mov          = serializers.DecimalField(max_digits=18, allow_null = True, decimal_places = 0 )
    cod_datos_acceso = serializers.DecimalField(max_digits=18, allow_null = True, decimal_places = 0 )
    guia_mov         = serializers.CharField(allow_null = True, allow_blank = True)
    url_guia_mov     = serializers.CharField(allow_null = True, allow_blank = True)
    material_mov     = serializers.CharField(allow_null = True, allow_blank = True)
    url_material_mov = serializers.CharField(allow_null = True, allow_blank = True)
