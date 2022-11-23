from rest_framework import serializers

class DatosAccesoSerializer(serializers.Serializer):
    codigo_dato_acceso      = serializers.IntegerField (allow_null = True) 
    codigo_mov_peatonal     = serializers.IntegerField (allow_null = True)
    descripcion             = serializers.CharField    (allow_null = True, allow_blank = True)
    fecha_creacion          = serializers.DateTimeField()
    creado_por              = serializers.CharField    (allow_null = True, allow_blank = True)
    cod_tipo_dato_acceso    = serializers.IntegerField (allow_null = True)
    pathImage               = serializers.CharField    (allow_null = True, allow_blank = True)

class DatosAccesoSalidaSerializer(serializers.Serializer):
    cod_mov          = serializers.DecimalField(max_digits=18, allow_null = True, decimal_places = 0 )
    cod_datos_acceso = serializers.DecimalField(max_digits=18, allow_null = True, decimal_places = 0 )
    guia_mov         = serializers.CharField(allow_null = True, allow_blank = True)
    url_guia_mov     = serializers.CharField(allow_null = True, allow_blank = True)
    material_mov     = serializers.CharField(allow_null = True, allow_blank = True)
    url_material_mov = serializers.CharField(allow_null = True, allow_blank = True)
