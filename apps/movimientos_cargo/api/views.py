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

            if params.keys().__contains__('codTipoCarga') & params.keys().__contains__('codServicio') & params.keys().__contains__('datoBuscar') & params.keys().__contains__('tipoConsulta') :

                codTipoCarga = params['codTipoCarga']
                codServicio  = params['codServicio']
                datoBuscar   = params['datoBuscar']
                tipoConsulta = params['tipoConsulta']

                with connection.cursor() as cursor:
                    cursor.execute("EXEC [dbo].[AppCA_ListadoMovimientosCargo] {0}, {1}, '{2}', '{3}' ".format(
                        codServicio, codTipoCarga, datoBuscar, tipoConsulta))
                    movimientos_data = cursor.fetchall()

                    for movimiento in movimientos_data:
                        dataTemp = {
                            'cod_movimiento': movimiento[0],
                            'codigo_vehicular': movimiento[1],
                            'placa': movimiento[2],
                            'tipo_carga': movimiento[3],
                            'nombres': movimiento[4],
                            'dni': movimiento[5],
                            'cargo': movimiento[6],
                            'empresa': '' if movimiento[7] is None else movimiento[7],
                            'fecha': movimiento[8],
                            'fecha_salida': movimiento[9],
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
