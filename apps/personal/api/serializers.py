from rest_framework import serializers


class PersonalSerializer(serializers.Serializer):
    codigo_personal       = serializers.DecimalField(max_digits=18, decimal_places=0)
    codigo_tipo_personal  = serializers.DecimalField(max_digits=18, decimal_places=0)
    codigo_empresa        = serializers.DecimalField(max_digits=18, decimal_places=0)
    codigo_tipo_documento = serializers.DecimalField(max_digits=18, decimal_places=0)
    codigo_cargo          = serializers.DecimalField(max_digits=18, decimal_places=0)
    codigo_area           = serializers.DecimalField(max_digits=18, decimal_places=0)
    nombre1               = serializers.CharField(max_length=50, allow_null=True, allow_blank=True)
    nombre2               = serializers.CharField(max_length=50, allow_null=True, allow_blank=True)
    apellido1             = serializers.CharField(max_length=50, allow_null=True, allow_blank=True)
    apellido2             = serializers.CharField(max_length=50, allow_null=True, allow_blank=True)
    doc_personal          = serializers.CharField(max_length=25, allow_null=True, allow_blank=True)
    sexo                  = serializers.CharField(max_length=1, allow_blank=True, allow_null=True)
    es_autorizante        = serializers.BooleanField()
    es_lista_negra        = serializers.DecimalField(max_digits=2, decimal_places=0, allow_null=True )
    tiene_foto            = serializers.DecimalField(max_digits=2, decimal_places=0, allow_null=True )
    imgPath               = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)
    brevete               = serializers.CharField(max_length=75, allow_null=True, allow_blank=True)
    nombre_turno_personal = serializers.CharField(max_length=255, allow_null=True, allow_blank=True)
    f_nacimiento          = serializers.CharField( allow_blank=True, allow_null=True)
    dosis_completa        = serializers.DecimalField(max_digits=2, decimal_places=0, allow_null=True)
    telefono              = serializers.CharField(max_length=100, allow_null=True, allow_blank=True)


class TiposPersonalSerializer(serializers.Serializer):
    codigo    = serializers.DecimalField(max_digits=18, decimal_places=0)
    personal   = serializers.CharField(max_length=50, allow_null=True, allow_blank=True)


class ValidacionPersonalSerializer(serializers.Serializer):
    estado_transaccion = serializers.IntegerField()
    cod_personal       = serializers.DecimalField(max_digits=18, decimal_places=0)


