from apps.usuario.api.serializers import UsuarioPermisosSerializer
from django.db import connections
from rest_framework import viewsets, status
from rest_framework.response import Response

class UsuarioPermisosViewSet(viewsets.GenericViewSet):

    serializer_class = UsuarioPermisosSerializer

    def list(self, request):
        try:
            dataArray = []

            params = self.request.query_params.dict()
            
            if params.keys().__contains__('codTipoUsuario'):
                codTipoUsuario = params['codTipoUsuario']
                
                with connections['test_solmar'].cursor() as cursor:
                    cursor.execute("EXEC [dbo].[APPS_LISTAR_PERMISOS_X_TIPO_USUARIO] {0}".format(codTipoUsuario))
                    permisos_usuario = cursor.fetchall()
                    # print(permisos_usuario)

                    for permiso in permisos_usuario:
                        dataTemp = {
                            'codigo_relacion': permiso[0],
                            'codigo_accion'  : permiso[1],
                            'codigo_alcance' : permiso[2]
                        }
                        dataArray.append(dataTemp)

                    permisos_serializer = self.get_serializer( data=dataArray, many=True )

                    if permisos_serializer.is_valid():
                        return Response(permisos_serializer.data, status=status.HTTP_200_OK)
                    else:
                        return Response(permisos_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({
                    'error': 'Por favor ingresar el parametro requerido'
                }, status=status.HTTP_400_BAD_REQUEST)

        finally:
            pass

