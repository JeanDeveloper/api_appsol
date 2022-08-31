from apps.empresas.api.serializers import *
from django.db import connection
from rest_framework import viewsets, status
from rest_framework.response import Response


class EmpresasViewSet(viewsets.GenericViewSet):
    serializer_class = EmpresasSerializer

    def list(self, request):
        data = []

        try:
            params = self.request.query_params.dict()

            if params.keys().__contains__('codEmpresa') & params.keys().__contains__('nombreEmpresa'):
                codEmpresa = params['codEmpresa']
                nombreEmpresa = params['nombreEmpresa']

                with connection.cursor() as cursor:

                    cursor.execute(" EXEC [dbo].[USP_SICOS_2019_BUSCAR_EMPRESAS_S_COMBO_UNIFICACION] '{0}', '-1', '{1}' ".format(nombreEmpresa, codEmpresa))
                    empresas_data = cursor.fetchall()
                    print(empresas_data)

                    for empresa in empresas_data:
                        dataTemp = {
                            'codigo': empresa[0],
                            'empresa': empresa[1],
                        }

                        data.append(dataTemp)

                    empresas_serializer = self.get_serializer(data=data, many=True)

                    if empresas_serializer.is_valid():
                        return Response(empresas_serializer.data, status=status.HTTP_200_OK)
                    else:
                        return Response(empresas_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response({
                    'error': 'Por favor ingresar los 2 parametros requeridos'
                }, status=status.HTTP_400_BAD_REQUEST)

        finally:
            pass
