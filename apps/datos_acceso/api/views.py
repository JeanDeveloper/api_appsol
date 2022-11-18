from apps.datos_acceso.api.serializers import *
from django.db import connection
from rest_framework import viewsets, status
from rest_framework.response import Response

class DatosAccesoViewSet(viewsets.GenericViewSet):

    serializer_class = DatosAccesoSerializer

    def create( self, request ):

        try:

            with connection.cursor() as cursor:

                cursor.execute(
                    "DECLARE @result INT;"
                    "EXEC [dbo].[APPS_REGISTRAR_DATOS_ACCESO] {0}, '{1}', '{2}', {3}, @codigo_dato_acceso_creado = @result OUTPUT;"
                    "SELECT @result as codigo_dato_acceso".format(
                        request.data['cod_mov_peatonal'], request.data['descripcion'], 
                        request.data['creado_por'], request.data['cod_tipo_dato_acceso']
                    )   
                )

                response = cursor.fetchone()

                if response: 
                    return Response({
                        'codigo_dato_acceso' : response[0] 
                    }, status=status.HTTP_201_CREATED)

        except AssertionError:
            print(AssertionError)

    def list(self, request):

        data = []
        params = self.request.query_params.dict()

        if params:

            if params['tipo_movimiento'] and params['codigo_servicio'] and params['documento']:

                with connection.cursor() as cursor:

                    cursor.execute('EXEC [dbo].[APPS_OBTENER_DATOS_ACCESO_QA] {0}, {1}, {2}'.format(
                        params['tipo_movimiento'], params['codigo_servicio'], params['documento']
                    ))

                    datos_acceso = cursor.fetchall()

                    for dato_acceso in datos_acceso:

                        dataTemp = {
                            'codigo_dato_acceso'    : dato_acceso[0],
                            'codigo_mov_peatonal'   : dato_acceso[1],
                            'descripcion'           : dato_acceso[2],
                            'fecha_creacion'        : dato_acceso[3],
                            'creado_por'            : dato_acceso[4],
                            'cod_tipo_dato_acceso'  : dato_acceso[5],
                            'pathImage'             : dato_acceso[6]
                        }

                        data.append(dataTemp)

                    datos_acceso_serializer = self.get_serializer( data = data, many = True)

                    if datos_acceso_serializer.is_valid():
                        return Response(datos_acceso_serializer.data, status=status.HTTP_200_OK )
                    else:
                        return Response(datos_acceso_serializer.errors, status=status.HTTP_400_BAD_REQUEST )


class DatosAccesoSalidaViewSet(viewsets.GenericViewSet):

    serializer_class = DatosAccesoSalidaSerializer

    def list(self, request):

        params = self.request.query_params.dict()

        if params.keys().__contains__('') & params.keys().__contains__('documento'):
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
