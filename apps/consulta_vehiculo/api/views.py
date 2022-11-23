from apps.consulta_vehiculo.api.serializers import *
from django.db import connection
from rest_framework import viewsets, status
from rest_framework.response import Response

class ConsultaVehiculoViewSet(viewsets.GenericViewSet):

    serializer_class = ConsultaVehiculoSerializer

    def list(self, request):

        try:

            params = self.request.query_params.dict()

            if params.keys().__contains__('codServicio') & params.keys().__contains__('placa'):

                with connection.cursor() as cursor:

                    codServicio = params['codServicio']
                    placa       = params['placa']

                    cursor.execute(" EXEC [CONSULTAR_DATOS_VEHICULO] {0}, {1} ". format(
                        placa, codServicio
                    ))

                    consulta_data = cursor.fetchone()

                    data = {
                        'codigo_vehiculo': consulta_data[0],
                        'codigo_empresa': consulta_data[1],
                        'empresa': consulta_data[2],
                        'codigo_tipo_vehiculo': consulta_data[3],
                        'tipo_vehiculo': consulta_data[4],
                        'placa': consulta_data[5],
                        'tarjeta_propiedad': consulta_data[6],
                        'ultimo_movimiento': consulta_data[7],
                        'codigo_carreta': consulta_data[8],
                        'codigo_carga':consulta_data[9],
                        'dni_conductor':consulta_data[10],
                        'codigo_autorizante':consulta_data[11],
                        'codigo_motivo':consulta_data[12],
                        'ultimo_movimiento_peatonal': consulta_data[13],
                        'codigo_productor': consulta_data[14],
                        'tipo_traslado': consulta_data[18],
                        'nombre_conductor': consulta_data[19],
                    }

                    consulta_serializer  = self.get_serializer(data=data)

                    if consulta_serializer.is_valid():
                        return Response(consulta_serializer.data, status = status.HTTP_200_OK)
                    else:
                        return Response(consulta_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        except NameError:
            return Response({
                'error': NameError
            }, status=status.HTTP_400_BAD_REQUEST)

        else:

            return Response({
                'error': 'Por favor ingresar los parametros requeridos'
            }, status=status.HTTP_400_BAD_REQUEST)

class VerificarVehiculoViewSet(viewsets.GenericViewSet):
    serializer_class = VerificacionVehiculoSerializer

    def list(self, request):

        try:
            params = self.request.query_params.dict()

            if params.keys().__contains__('codServicio') & params.keys().__contains__('codVehiculo'):

                codServicio = params['codServicio']
                codVehiculo  = params['codVehiculo']

                with connection.cursor() as cursor:
                    cursor.execute(" EXEC [dbo].[APPS_VERIFICAR_PERMISO_VEHICULO]  {0}, {1}".format(
                        codServicio, codVehiculo
                    ))
                    verificacion_data = cursor.fetchone()

                    data = {
                        'valor': verificacion_data[0],
                        'mensaje': verificacion_data[1],
                        'marca': verificacion_data[2],
                        'codigo': verificacion_data[3],
                    }

                    verificacion_data = self.get_serializer(data=data)

                    if verificacion_data.is_valid():
                        return Response(verificacion_data.data, status = status.HTTP_200_OK)
                    else:
                        return  Response(verificacion_data.errors, status = status.HTTP_400_BAD_REQUEST)

            else:

                return Response({
                    'error': 'Por favor ingresar los 2 parametros requeridos'
                }, status=status.HTTP_400_BAD_REQUEST)

        except NameError:
            return Response({
                'error': NameError
            }, status=status.HTTP_400_BAD_REQUEST)