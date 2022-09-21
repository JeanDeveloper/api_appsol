from apps.movimientos_cargo.api.serializers import *
from django.db import connection
from rest_framework import viewsets, status
from rest_framework.response import Response

class MovimientosCargoViewSet(viewsets.GenericViewSet):
    serializer_class = MovimientosCargoSerializer

    def list(self, request):
        data = []

        try:
            params =  self.request.query_params.dict()

            if params.keys().__contains__('codTipoCarga') & params.keys().__contains__('codServicio') & params.keys().__contains__('tipoConsulta') :

                codTipoCarga = params['codTipoCarga']
                codServicio  = params['codServicio']
                tipoConsulta = params['tipoConsulta']

                with connection.cursor() as cursor:
                    cursor.execute("EXEC [dbo].[AppCA_ListadoMovimientosCargoQA] {0}, {1}, '', '{2}' ".format(codServicio, codTipoCarga, tipoConsulta))
                    movimientos_data = cursor.fetchall()


                    for movimiento in movimientos_data:
                        dataTemp = {
                            'cod_movimiento': movimiento[0],
                            'codigo_vehicular': movimiento[1],
                            'placa': movimiento[2],
                            'cod_tipo_carga': movimiento[3],
                            'tipo_carga': movimiento[4],
                            'nombres': movimiento[5],
                            'dni': movimiento[6],
                            'cargo': movimiento[7],
                            'empresa': '' if movimiento[8] is None else movimiento[8],
                            'fecha_ingreso': movimiento[9],
                            'fecha_salida': movimiento[10],
                        }

                        data.append(dataTemp)
                    movimientos_serializer = self.get_serializer( data=data, many=True )
                    if movimientos_serializer.is_valid():
                        return Response(movimientos_serializer.data, status=status.HTTP_200_OK)
                    else:
                        return Response(movimientos_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response({
                    'error': 'Por favor ingresar los 3 parametros requeridos'
                }, status=status.HTTP_400_BAD_REQUEST)

        except ValueError:
            print(ValueError)
