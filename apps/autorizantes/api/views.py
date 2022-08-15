from django.db import connection
from rest_framework.response import Response
from apps.autorizantes.api.serializers import AutorizantesSerializer
from rest_framework import viewsets, status


class AutorizantesViewSet(viewsets.GenericViewSet):
    serializer_class = AutorizantesSerializer

    def list(self, request):

        data = []

        with connection.cursor() as cursor:
            params = self.request.query_params.dict()

            if params:

                if params['idServicio'] and params['tipoPersonal']:

                    idServicio = params['idServicio']
                    tipoPersonal = params['tipoPersonal']

                    if idServicio == '' or tipoPersonal == '':
                        return Response({
                            'error': 'hay algun campo requerido que se encuentra vacio'
                        }, status=status.HTTP_400_BAD_REQUEST)

                    else:
                        cursor.execute('EXEC [dbo].[AppCa_LISTAR_AUTORIZANTES] {0}, {1}'.format(idServicio, tipoPersonal))
                        autorizantes_data = cursor.fetchall()

                        if autorizantes_data:

                            for autorizante in autorizantes_data:
                                dataTemp = {
                                    'codigo': autorizante[0],
                                    'cod_personal': autorizante[1],
                                    'nombre_personal': autorizante[2],
                                    'dni_personal': autorizante[3]
                                }

                                data.append(dataTemp)

                            autorizantes_serializer = self.get_serializer(data=data, many=True)

                            if autorizantes_serializer.is_valid():
                                return Response(autorizantes_serializer.data, status=status.HTTP_200_OK)

                            else:
                                return Response(autorizantes_serializer.errors,
                                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                        else:
                            return Response({
                                'message': 'no hay data en la consulta'
                            }, status=status.HTTP_200_OK)

                else:
                    return Response({
                        'error': 'Se necesitan los dos parametros solicitados'
                    }, status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response({
                    'error': 'Por favor enviar los parametros requeridos'
                }, status=status.HTTP_400_BAD_REQUEST)
