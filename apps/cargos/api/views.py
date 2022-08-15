# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets, status
from apps.cargos.api.serializers import CargosSerializer
from django.db import connection


class CargosViewSet(viewsets.GenericViewSet):
    serializer_class = CargosSerializer

    def list(self, request):
        data = []

        try:
            params = self.request.query_params.dict()

            if params.keys().__contains__('cargo') & params.keys().__contains__('codCliente'):
                cargo = params['cargo']
                codCliente = params['codCliente']

                with connection.cursor() as cursor:
                    cursor.execute(" EXEC [dbo].[USP_SICOS_2019_BUSCAR_CARGOS_DEALER_S_COMBO_UNIFICACION] '', 25866")
                    cargos_data = cursor.fetchall()

                    for cargo in cargos_data:
                        dataTemp = {
                            'codigo': cargo[0],
                            'cargo': cargo[1],
                            'habilitado': cargo[2],
                        }
                        data.append(dataTemp)

                    cargos_serializer = self.get_serializer(data=data, many=True)

                    if cargos_serializer.is_valid():
                        return Response(cargos_serializer.data, status=status.HTTP_200_OK)
                    else:
                        return Response(cargos_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:

                return Response({
                    'error': 'Por favor ingresar los 2 parametros requeridos'
                }, status=status.HTTP_400_BAD_REQUEST)

        finally:
            pass


