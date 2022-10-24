from apps.fotos_acceso.api.serializers import FotosAccesoSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db import connection, connections

class FotosAccesoViewSet(viewsets.GenericViewSet):

    serializer_class = FotosAccesoSerializer

    def list(self, request):
        try:

            params = self.request.query_params.dict()

            if params.keys().__contains__('foto_id'):
                foto_id = params['foto_id']
                with connection.cursor() as cursor:
                    cursor.execute("EXEC [dbo].[APPS_OBTENER_FOTO_DE_ACCESO] {0} ". format(foto_id))

                    foto_data = cursor.fetchone()

                    data = {
                        'foto_id' : foto_data[0],
                        'nombre'  : foto_data[1],
                        'extension'  : foto_data[2],
                        'tipo_dato_acceso'  : foto_data[3],
                        'tamanio'  : foto_data[4],
                        'fecha_creacion'  : foto_data[5],
                        'creado_por'  : foto_data[6],
                        'ubicacion'  : foto_data[7],
                    }

                    print(foto_data);
                    
                    foto_serializer = self.get_serializer( data = data)

                    if foto_serializer.is_valid():
                        return Response(foto_serializer.data, status = status.HTTP_200_OK)
                    else:
                        return  Response(foto_serializer.errors, status= status.HTTP_400_BAD_REQUEST)

        except NameError:
            Response({
                'error': NameError
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CopiarFotoViewSet(viewsets.GenericViewSet):

    def list(self, request):
        try:
            params = self.request.query_params.dict()

            if params.keys().__contains__('cod_movimiento')  &  params.keys().__contains__('cod_personal') &  params.keys().__contains__('datoAcceso'):

                cod_movimiento = params['cod_movimiento']
                cod_personal = params['cod_personal']
                dato_acceso = params['datoAcceso']

                with connection.cursor() as cursor:
                    cursor.execute("EXECUTE [dbo].[AppSolgis_Copiar_fotoId] {0}, {1}, {2} ".format(cod_movimiento, cod_personal, dato_acceso))

                    copia_foto = cursor.fetchone()

                    print(copia_foto);

                    if len(copia_foto) == 1:
                        return Response({
                            'message': copia_foto[0]
                        }, status=status.HTTP_201_CREATED)
                    else:
                        return Response({
                            'message': 'hubo un inconveniente '
                        }, status=status.HTTP_201_CREATED)

        except NameError:
            Response({
                'error': NameError
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)