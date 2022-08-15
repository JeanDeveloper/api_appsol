from rest_framework import serializers


class PersonalSerializer(serializers.Serializer):
    codigo_personal = serializers.DecimalField(max_digits=18, decimal_places=0)
    codigo_tipo_personal = serializers.DecimalField(max_digits=18, decimal_places=0)
    codigo_empresa = serializers.DecimalField(max_digits=18, decimal_places=0)
    codigo_tipo_documento = serializers.DecimalField(max_digits=18, decimal_places=0)
    codigo_cargo = serializers.DecimalField(max_digits=18, decimal_places=0)
    # codigo_area = serializers.DecimalField(max_digits=18, decimal_places=0)
    nombre1 = serializers.CharField(max_length=50, allow_null=True, allow_blank=True)
    nombre2 = serializers.CharField(max_length=50, allow_null=True, allow_blank=True)
    apellido1 = serializers.CharField(max_length=50, allow_null=True, allow_blank=True)
    apellido2 = serializers.CharField(max_length=50, allow_null=True, allow_blank=True)
    doc_personal = serializers.CharField(max_length=25, allow_null=True, allow_blank=True)
    sexo = serializers.CharField(max_length=1, allow_blank=True, allow_null=True)
    creado_por = serializers.CharField(max_length=75, allow_null=True, allow_blank=True)
    brevete = serializers.CharField(max_length=75, allow_null=True, allow_blank=True)
    es_autorizante = serializers.DecimalField(max_digits=2, decimal_places=0, allow_null=True)
    habilitado = serializers.BooleanField(default=1)
    tiene_foto = serializers.BooleanField()
    codigo_cliente_control = serializers.CharField(max_length=5, allow_null=True, allow_blank=True)
    # estado_transaccion = serializers.DecimalField(max_digits=2, decimal_places=0, allow_null=True)
    # codigo_personal_creado = serializers.DecimalField(max_digits=2, decimal_places=0, allow_null=True)
