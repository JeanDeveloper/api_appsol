from rest_framework import viewsets, status
from apps.detalle_personal.api.serializers import DetallePersonalSerializer
from rest_framework.response import Response
from django.db import connection


class DetallePersonaViewSet(viewsets.GenericViewSet):
    serializer_class = DetallePersonalSerializer

    def list(self, request):

        data = []

        with connection.cursor() as cursor:

            params = self.request.query_params.dict()

            if params:

                if params['doc'] and params['idServicio']:

                    documento = params['doc']
                    idServicio = params['idServicio']

                    if documento == '' or idServicio == '':
                        return Response({
                            'error': 'hay algun campo requerido que se encuentra vacio '
                        }, status=status.HTTP_400_BAD_REQUEST)

                    else:
                        cursor.execute("EXEC [dbo].[AppCA_DETALLE_PERSONAL] '{0}',{1}".format(documento, idServicio))
                        detalle_per_data = cursor.fetchall()

                        if detalle_per_data:

                            for detalle in detalle_per_data:
                                dataTemp = {
                                    'resultado': detalle[0],
                                    'mensaje': detalle[1],
                                    'tipo_consulta': detalle[2],
                                    'codigo_persona': detalle[3],
                                    'doc_persona': detalle[4],
                                    'nombres_persona': detalle[5],
                                    'codigo_cargo': detalle[6],
                                    'cargo': detalle[7],
                                    'codigo_tipo_documento': detalle[8],
                                    'tipo_documento': detalle[9],
                                    'codigo_empresa': detalle[10],
                                    'empresa': detalle[11],
                                    'codigo_mov_sgt': detalle[12],
                                    'codigo_autorizante': detalle[13],
                                    'autorizante': detalle[14],
                                    'codigo_motivo': detalle[15],
                                    'motivo': detalle[16],
                                    'codigo_area': detalle[17],
                                    'area': detalle[18],
                                    'codigo_tipo_persona': detalle[19],
                                    'tipo_persona': detalle[20],
                                    'codigo_servicio': detalle[21],
                                    'codigo_cliente_control': detalle[22],
                                    'img': detalle[23],
                                    'nro_pase': detalle[24],
                                }
                                data.append(dataTemp)


                            #VER PRIMERO EL RESULTADO DE LA CONSULTA
                            # if data['resultado'] == 'OK':
                            #
                            #
                            # else:








                            detalle_per_serializer = self.get_serializer(data=data, many=True)

                            if detalle_per_serializer.is_valid():
                                return Response(
                                    detalle_per_serializer.data,
                                    status=status.HTTP_200_OK
                                )

                            else:
                                return Response(
                                    detalle_per_serializer.errors,
                                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                                )

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
