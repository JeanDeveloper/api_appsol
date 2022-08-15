from apps.device.api.serializers import *
from django.db import connection
from rest_framework import viewsets, status
from rest_framework.response import Response


class RegistrarDispositivoViewSet(viewsets.GenericViewSet):

    serializer_class = RegistrarDispositivoSerializer

    def create(self, request):

        with connection.cursor() as cursor:

            cursor.execute(
                "DECLARE @result VARCHAR(500), @codigo NUMERIC(18,0), @estado SMALLINT; "
                "EXECUTE @result = [dbo].[APPS_INSERTAR_DISPOSITIVOS] '{0}', '{1}', '{2}', '{3}', {4}, '{5}', '{6}', '{7}', '{8}', '{9}', @estado_transaccion=@estado OUTPUT, @codigo_dispositivo_creado=@codigo OUTPUT "
                "SELECT  @estado AS 'estado', @codigo as 'codigo'".format(
                    request.data['serial'], request.data['hardware'], request.data['modelo'], 
                    request.data['fabricante'], request.data['version_api'], request.data['numero'],
                    request.data['sdk'], request.data['incremental'], request.data['dispositivo'], 
                    request.data['id']
                )
            )

            dispositivo_data = cursor.fetchone()
            print(dispositivo_data)
            if dispositivo_data[0] == 1:

                return Response({
                    'estado' : dispositivo_data[0],
                    'message': 'El dispositivo fue creado satisfactoriamente',
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
                    'message': 'El dispositivo ya se encuentra registrado y esta habilitado',
                    'id_dispositivo': int(dispositivo_data[1])
                }, status=status.HTTP_403_FORBIDDEN)
            else:
                return Response({
                    'estado' : dispositivo_data[0],
                    'message': 'El dispositivo no se ha podido crear',
                    'id_dispositivo': -1
                }, status=status.HTTP_400_BAD_REQUEST)


class ConsultarEstadoViewSet(viewsets.GenericViewSet):

    serializer_class = ConsultarEstadoSerializer

    def list(self, request):

        try:
            params = self.request.query_params.dict()
            
            if params.keys().__contains__('serial'):

                with connection.cursor() as cursor:

                    serialNumber = params['serial']
                    cursor.execute( 
                        "DECLARE @result SMALLINT, @state SMALLINT;" 
                        "EXECUTE @result = [dbo].[APPS_VERIFICAR_ESTADO_DISPOSITIVO] '{0}',@estado=@state OUTPUT "
                        "SELECT  @state AS 'estado';".format(serialNumber)
                    )

                    estado = cursor.fetchone()

                    print(estado[0])
                    
                    return Response({
                        'estado': estado[0]
                    },status= status.HTTP_200_OK)

            else:
                return Response({
                    'error': 'No se encontro el parametro solicitado'
                }, status= status.HTTO_400_BAD_REQUEST)

        finally:
            pass
            # cursor.close()
