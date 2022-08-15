from django.db import connection
from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.motivos.api.serializers import MotivosListSerializer


class MotivosListViewSet(viewsets.GenericViewSet):
    serializer_class = MotivosListSerializer

    def list(self, request):

        data = []

        with connection.cursor() as cursor:
            params = self.request.query_params.dict()

            if params:

                if params['idServicio'] and params['idCliente']:

                    idServicio = params['idServicio']
                    idCliente = params['idCliente']

                    if idServicio == '' or idCliente == '':
                        return Response({
                            'error': 'hay algun campo requerido que se encuentra vacio'
                        }, status=status.HTTP_400_BAD_REQUEST)

                    else:
                        cursor.execute(" EXEC [dbo].[AppCA_ListarMotivos] {0},'{1}' ".format(idServicio, idCliente))
                        areas_data = cursor.fetchall()

                        if areas_data:

                            for area in areas_data:
                                dataTemp = {
                                    'codigo': area[0],
                                    'tipo': area[1],
                                }

                                data.append(dataTemp)

                            area_serializer = self.get_serializer(data=data, many=True)

                            if area_serializer.is_valid():
                                return Response(area_serializer.data, status=status.HTTP_200_OK)

                            else:
                                return Response(area_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                        else:
                            return Response({'message': 'no hay data en la consulta'}, status=status.HTTP_302_FOUND)

                else:
                    return Response({
                        'error': 'Se necesitan los dos parametros solicitados'
                    }, status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response({
                    'error': 'Por favor enviar los parametros requeridos'
                }, status=status.HTTP_400_BAD_REQUEST)