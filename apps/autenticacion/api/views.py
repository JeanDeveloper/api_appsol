from apps.autenticacion.api.serializers import *
from django.db import connections
from rest_framework import viewsets, status
from rest_framework.response import Response

class AutenticacionViewSet(viewsets.GenericViewSet):
    serializer_class = AutenticacionDNISerializer

    def list(self, request):
        try:
            params = self.request.query_params.dict()

            if params.keys().__contains__('dni'):
                dni = params['dni']
                with connections['test_solmar'].cursor() as cursor:
                    cursor.execute( "EXEC [dbo].[APPS_VERIFICAR_DNI_PERSONAL_SOLMAR] '{0}'".format(dni))
                    auth_dni = cursor.fetchone()
                    print(auth_dni)

                    if len(auth_dni) == 1:
                        return Response({
                            'message': auth_dni 
                        }, status = status.HTTP_400_BAD_REQUEST)

                    else:

                        data = {
                            'codigo_personal'   : auth_dni[0],
                            'dni'               : auth_dni[1], 
                            'p_nombre'          : auth_dni[2],
                            's_nombre'          : auth_dni[3],
                            'p_apellido'        : auth_dni[4],
                            's_apellido'        : auth_dni[5],
                            'cargo'             : auth_dni[6],
                            'cod_tipo_usuario'  : int(auth_dni[7]),
                        }

                        auth_serializer = self.get_serializer(data= data)

                        if auth_serializer.is_valid():
                            return Response(auth_serializer.data, status= status.HTTP_200_OK)
                        else:
                            return Response(auth_serializer.errors, status= status.HTTP_400_BAD_REQUEST)

            else:

                return Response({
                    'error': 'No se encontro el parametro solicitado'
                }, status= status.HTTP_400_BAD_REQUEST)

        finally:
            pass