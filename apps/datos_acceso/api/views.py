from apps.datos_acceso.api.serializers import DatosAccesoSerializer
from django.db import connection, connections
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

class DatosAccesoViewSet(viewsets.GenericViewSet):

    serializer_class = DatosAccesoSerializer

    def list(self, request):

        data = []

        params = self.request.query_params.dict()

        if params:
            

            if params['codigo_servicio'] and params['codigo_personal']:

                with connection.cursor() as cursor:

                    cursor.execute('EXEC[dbo].[APPS_OBTENER_DATOS_ACCESO] {0}, {1}'.format(
                        params['codigo_servicio'], params['codigo_personal']
                    ))

                    datos_acceso = cursor.fetchone()
                    data = {
                        'codigo_datos_acceso'       : datos_acceso[0],
                        'codigo_movimiento'         : datos_acceso[1],
                        'guia_movimiento'           : datos_acceso[2],
                        'foto_guia_movimiento'      : datos_acceso[3],
                        'material_movimiento'       : datos_acceso[4],
                        'foto_material_movimiento'  : datos_acceso[5],
                        'fecha_creacion'            : datos_acceso[6]
                    }

                    datos_acceso_serializer = self.get_serializer(data=data)

                    if datos_acceso_serializer.is_valid():
                        return Response(datos_acceso_serializer.data, status=status.HTTP_200_OK )
                    else:
                        return Response(datos_acceso_serializer.errors, status=status.HTTP_400_BAD_REQUEST )
