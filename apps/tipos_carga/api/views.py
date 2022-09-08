from django.db import connection
from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.tipos_carga.api.serializers import TiposCargaListSerializer


class TiposCargaViewSet(viewsets.GenericViewSet):
    serializer_class = TiposCargaListSerializer

    def list(self, request):
        data = []
        try:

            params  =  self.request.query_params.dict()

            if params.keys().__contains__('CodCliente'):
                codigo_cliente = params['CodCliente']

                with  connection.cursor() as cursor:
                    cursor.execute( "EXEC [dbo].[APPS_listar_tipos_carga] {0} ".format(codigo_cliente))
                    cargas_data = cursor.fetchall()

                    for tipo_carga in cargas_data:
                        dataTemp = {
                            'codigo_carga': tipo_carga[0],
                            'carga': tipo_carga[1],
                        }

                        data.append(dataTemp)
                    
                    data_serializer = self.get_serializer( data=data, many=True  )

                    if data_serializer.is_valid():
                        return Response(data_serializer.data, status=status.HTTP_200_OK)
                    else:
                        return Response(data_serializer.errors, status= status.HTTP_400_BAD_REQUEST)
            else:
                return Response({
                    'error': 'Por favor ingrese el parametro requerido'
                }, status=status.HTTP_400_BAD_REQUEST)


        except ValueError:
            print(ValueError)