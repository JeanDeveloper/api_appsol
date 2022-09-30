from apps.device.api.serializers import *
from django.db import connections
from rest_framework import viewsets, status
from rest_framework.response import Response

class RegistrarDispositivoViewSet(viewsets.GenericViewSet):

    serializer_class = RegistrarDispositivoSerializer

    def create(self, request):

        with connections['test_solmar'].cursor() as cursor:

            cursor.execute(
                "DECLARE @result VARCHAR(500), @codigo NUMERIC(18,0), @estado SMALLINT; "
                "EXECUTE @result = [dbo].[APPS_INSERTAR_DISPOSITIVOS] '{0}', '{1}', '{2}', '{3}', {4}, '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', @estado_transaccion=@estado OUTPUT, @codigo_dispositivo_creado=@codigo OUTPUT "
                "SELECT  @estado AS 'estado', @codigo as 'codigo'".format(
                    request.data['serial'], request.data['hardware'], request.data['modelo'], 
                    request.data['fabricante'], request.data['version_api'], request.data['numero'],
                    request.data['sdk'], request.data['incremental'], request.data['dispositivo'], 
                    request.data['id'], request.data['id_fb'],
                )
            )

            dispositivo_data = cursor.fetchone()

            if dispositivo_data[0] == 1:
                return Response({
                    'estado' : dispositivo_data[0],
                    'message': 'El dispositivo fue registrado satisfactoriamente',
                    'id_dispositivo': int(dispositivo_data[1])
                }, status=status.HTTP_201_CREATED)

            elif dispositivo_data[0] == 2:
                return Response({
                    'estado' : dispositivo_data[0],
                    'message': 'El dispositivo se encuentra registrado, pero no esta habilitado',
                    'id_dispositivo': int(dispositivo_data[1])
                }, status=status.HTTP_403_FORBIDDEN)

            elif dispositivo_data[0] == 3:
                return Response({
                    'estado' : dispositivo_data[0],
                    'message': 'El dispositivo se encuentra registrado y esta habilitado',
                    'id_dispositivo': int(dispositivo_data[1])
                }, status=status.HTTP_403_FORBIDDEN)

            elif dispositivo_data[0] == 4:
                return Response({
                    'estado' : dispositivo_data[0],
                    'message': 'El numero ya se encuentra registrado',
                    'id_dispositivo': int(dispositivo_data[1])
                }, status = status.HTTP_403_FORBIDDEN)

            else:
                return Response({
                    'estado' : dispositivo_data[0],
                    'message': 'El dispositivo no se ha podido registrar',
                    'id_dispositivo': -1
                }, status=status.HTTP_400_BAD_REQUEST)

class ConsultarEstadoViewSet(viewsets.GenericViewSet):

    serializer_class = ConsultarEstadoSerializer

    def list(self, request):
        try:
            params = self.request.query_params.dict()
            
            if params.keys().__contains__('serial'):
                with connections['test_solmar'].cursor() as cursor:
                    serialNumber = params['serial']
                    cursor.execute( 
                        "DECLARE @result SMALLINT, @state SMALLINT;" 
                        "EXECUTE @result = [dbo].[APPS_VERIFICAR_ESTADO_DISPOSITIVO] '{0}',@estado=@state OUTPUT "
                        "SELECT  @state AS 'estado';".format(serialNumber)
                    )

                    estado = cursor.fetchone()

                    return Response({
                        'estado': estado[0]
                    },status= status.HTTP_200_OK)
            else:
                return Response({
                    'error': 'No se encontro el parametro solicitado'
                }, status= status.HTTP_400_BAD_REQUEST)
        finally:
            pass

class RelacionDispositivoServicioViewSet(viewsets.GenericViewSet):

    serializer_class = RelacionDispositivoServicioSerializer

    def list(self, request):

        try:
            params = self.request.query_params.dict()

            if params.keys().__contains__('serial'):
                serial = params['serial']

                with connections['test_solmar'].cursor() as cursor:
                    cursor.execute("EXEC [dbo].[APPS_OBTENER_INFO_DISPOSITIVO_SERVICIO] '{0}'".format(serial))
                    dispositivo_x_servicio = cursor.fetchone()

                    data = {
                        'codigo_dispositivo'   : dispositivo_x_servicio[0],
                        'codigo_servicio'      : dispositivo_x_servicio[1],
                        'codigo_cliente'       : dispositivo_x_servicio[2],
                        'codigo_sub_area'      : int(dispositivo_x_servicio[3]),
                        'nombre_area'          : dispositivo_x_servicio[4],
                        'nombre_sub_area'      : dispositivo_x_servicio[5],
                        'nombre_sucursal'      : dispositivo_x_servicio[6],
                        'nombre_cliente'       : dispositivo_x_servicio[7],
                        'alias_sede'           : dispositivo_x_servicio[8],
                        'codigo_tipo_servicio' : int(dispositivo_x_servicio[9]),
                        'nombre_puesto'        : dispositivo_x_servicio[10],
                    }

                    return Response(data, status= status.HTTP_200_OK)

            else:

                return Response({
                    'error': 'No se encontro el parametro solicitado'},
                    status= status.HTTP_400_BAD_REQUEST
                )

        except NameError:
                return Response({
                    'error':NameError},
                    status= status.HTTP_400_BAD_REQUEST
                )
