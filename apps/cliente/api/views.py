from apps.cliente.api.serializers import *
from django.db import connection, connections
from rest_framework import viewsets, status
from rest_framework.response import Response

class ClientesViewSet(viewsets.GenericViewSet):

    serializer_class = ClientesSerializer

    def list(self, request):

        data = []

        try:

            with connection.cursor() as cursor:
                cursor.execute(" EXEC [dbo].[Migracion_Listar_Clientes] '' ")

                clientes_data = cursor.fetchall()

                for cliente in clientes_data:
                    dataTemp = {
                        'codigo'              : cliente[0],
                        'nomb_cliente'                : cliente[1],
                    }
                    data.append(dataTemp)

                cliente_serializer = self.get_serializer(data=data, many=True)

                if cliente_serializer.is_valid():
                    return Response(cliente_serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(cliente_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        finally:
            pass


class ServiciosXClienteViewSet(viewsets.GenericViewSet):
    serializer_class = ServiciosXClienteSerializer

    def list(self, request):

        data = []

        try:
            params = self.request.query_params.dict()

            if params.keys().__contains__('codCliente'):
                codCliente = params['codCliente']

                if codCliente == '00005':  #ES SERVICIO HAYDUK
                    with connections['bd_hayduk'].cursor() as cursor:
                        cursor.execute("EXEC [dbo].[USP_SICOS_2019_BUSCAR_CARGOS_DEALER_S_COMBO_UNIFICACION] '' " )

                        cargos_data = cursor.fetchall()
                        for cargo in cargos_data:
                            dataTemp = {
                                'codigo': cargo[0],
                                'cargo' : cargo[1]
                            }
                            data.append(dataTemp)
                        cargos_serializer = self.get_serializer(data = data, many = True)
                        if cargos_serializer.is_valid():
                            return Response(cargos_serializer.data, status=status.HTTP_200_OK)
                        else:
                            return Response(cargos_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                else:

                    if codCliente == '00002':  # ES SERVICIO TASA
                        with connections['bd_tasa'].cursor() as cursor:
                            cursor.execute("EXEC [dbo].[USP_SICOS_2019_BUSCAR_CARGOS_DEALER_S_COMBO_UNIFICACION] '' " )

                            cargos_data = cursor.fetchall()
                            for cargo in cargos_data:
                                dataTemp = {
                                    'codigo': cargo[0],
                                    'cargo' : cargo[1]
                                }
                                data.append(dataTemp)
                            cargos_serializer = self.get_serializer(data = data, many = True)
                            if cargos_serializer.is_valid():
                                return Response(cargos_serializer.data, status=status.HTTP_200_OK)
                            else:
                                return Response(cargos_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                    else:

                        with connection.cursor() as cursor:
                            cursor.execute(" EXEC [dbo].[APPS_LISTAR_SERVICIOS_X_CLIENTE] {0}".format(codCliente))

                            servicios_data = cursor.fetchall()


                            for servicio in servicios_data:
                                dataTemp = {
                                    'codigo'              : servicio[0],
                                    'sede'                : servicio[1],
                                    'codigo_sub_area'     : servicio[2],
                                    'nombre_area'         : servicio[3],
                                    'nombre_sub_area'     : servicio[4],
                                    'nombre_sucursal'     : servicio[5],
                                    'alias_sede'          : servicio[6],
                                    'codigo_tipo_servicio': servicio[7],
                                }
                                data.append(dataTemp)

                            servicio_serializer = self.get_serializer(data=data, many=True)

                            if servicio_serializer.is_valid():
                                return Response(servicio_serializer.data, status=status.HTTP_200_OK)
                            else:
                                return Response(servicio_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:

                return Response({
                    'error': 'Por favor ingresar el parametro requerido'
                }, status=status.HTTP_400_BAD_REQUEST)

        finally:
            pass

