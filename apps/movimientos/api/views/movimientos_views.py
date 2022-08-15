from apps.movimientos.api.serializers.movimiento_serializers import *
from django.db import connection
from rest_framework import viewsets, status
from rest_framework.response import Response


class MovimientosViewSet(viewsets.GenericViewSet):

    serializer_class = MovimientosListSerializer

    def list(self, request):

        data = []
        cursor = connection.cursor()

        try:

            params = self.request.query_params.dict()

            if params.keys().__contains__('tipoMovimiento') & params.keys().__contains__(
                    'idServicio') & params.keys().__contains__('tipoPersonal'):

                tipoMovimiento = params['tipoMovimiento']
                idServicio = params['idServicio']
                tipoPersonal = params['tipoPersonal']

                cursor.execute(
                    "EXEC [dbo].[AppCA_ListadoMovimientosPeople] {0}, {1}, {2} , {3}".format(idServicio, tipoPersonal,
                                                                                            "''", tipoMovimiento))

                movimientos_data = cursor.fetchall()

                for movimiento in movimientos_data:
                    dataTemp = {
                        'cod_movimiento': movimiento[0],
                        'nombres': movimiento[1],
                        'dni': movimiento[2],
                        'sexo': movimiento[3],
                        'cargo': movimiento[4],
                        'empresa': movimiento[5],
                        'fecha_movimiento': movimiento[6],
                        'fecha_salida': '' if movimiento[7] is None else movimiento[7],
                        'tipo_ingreso': movimiento[8],
                        'tipo_personal': movimiento[9],
                        'imagen': movimiento[10],
                    }

                    data.append(dataTemp)

                movimientos_serializer = self.get_serializer(data=data, many=True)

                if movimientos_serializer.is_valid():
                    return Response(movimientos_serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(movimientos_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response({
                    'error': 'Por favor ingresar los 3 parametros requeridos'
                }, status=status.HTTP_400_BAD_REQUEST)

        finally:
            cursor.close()

    def create(self, request):
        date = datetime.datetime.now()

        with connection.cursor() as cursor:

            cursor.execute( "DECLARE @result SMALLINT, @result1 SMALLINT;"
                            "EXECUTE @result = [dbo].[USP_SICOS_2014_INSERTAR_MOVIMIENTO_PEATONAL_2019_I_UNIFICACION]"
                            " 0, {0}, {1}, {2}, {3}, {4}, 0, 0, {5}, \" \", '', 0, '', 0,'N', '{6}', 1, -1, '', '', '', {7}, '00', 0, 0," 
                            "@estado_transaccion=@result1 OUTPUT "
                            "select @result1 as RESULTADO".format(
                            request.data['codigo_personal'], request.data['codigo_servicio'], request.data['codigo_tipo_movimiento'],
                            request.data['codigo_tipo_motivo'], request.data['codigo_empresa'], request.data['autorizado_por'],
                            request.data['creado_por'], request.data['codigo_area']
            ))

            movimiento_id = cursor.fetchone()

            if movimiento_id:
                return Response({
                    'message': 'movimiento creado satisfactoriamente',
                    'id_movimiento': movimiento_id[0]
                }, status=status.HTTP_201_CREATED)
            else:

                return Response({
                    'message': 'hubo un error al momento de crear un movimiento'
                }, status=status.HTTP_400_BAD_REQUEST)
