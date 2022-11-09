from apps.datos_acceso.api.serializers import *
from django.db import connection
from rest_framework import viewsets, status
from rest_framework.response import Response

class DatosAccesoViewSet(viewsets.GenericViewSet):

    serializer_class = DatosAccesoSerializer

    def list(self, request):

        data = []
        params = self.request.query_params.dict()

        if params:

            if params['codigo_servicio'] and params['codigo_personal']:

                with connection.cursor() as cursor:

                    cursor.execute('EXEC [dbo].[APPS_OBTENER_DATOS_ACCESO] {0}, {1}'.format(
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


class DatosAccesoSalidaViewSet(viewsets.GenericViewSet):

    serializer_class = DatosAccesoSalidaSerializer

    def list(self, request):

        params = self.request.query_params.dict()

        if params.keys().__contains__('codServicio') & params.keys().__contains__('documento'):
            codServicio = params['codServicio']
            documento   = params['documento']

            with connection.cursor() as cursor:
                cursor.execute("EXEC [dbo].[APPS_OBTENER_DATOS_ACCESO_ULTIMO_MOVIMIENTO] {0}, {1} ".format(codServicio, documento))
                datos_acceso_salida = cursor.fetchone()

                print(datos_acceso_salida)
                
                

                data = {
                    'cod_mov'          : '' if datos_acceso_salida == None else datos_acceso_salida[0],
                    'cod_datos_acceso' : 0  if datos_acceso_salida == None else datos_acceso_salida[1],
                    'guia_mov'         : '' if datos_acceso_salida == None else datos_acceso_salida[2],
                    'url_guia_mov'     : '' if datos_acceso_salida == None else datos_acceso_salida[3],
                    'material_mov'     : '' if datos_acceso_salida == None else datos_acceso_salida[4],
                    'url_material_mov' : '' if datos_acceso_salida == None else datos_acceso_salida[5],
                }

                datos_acceso_serializer = self.get_serializer(data=data)

                if(datos_acceso_serializer.is_valid()):
                    return Response(datos_acceso_serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(datos_acceso_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({
                'error': 'Por favor ingrese los parametros requeridos'
            }, status=status.HTTP_400_BAD_REQUEST )


