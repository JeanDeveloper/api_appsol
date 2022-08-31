from apps.autorizantes.api.serializers import AutorizantesSerializer
from django.db import connection, connections
from rest_framework import viewsets, status
from rest_framework.response import Response


class AutorizantesViewSet(viewsets.GenericViewSet):
    serializer_class = AutorizantesSerializer

    def list(self, request):

        data = []
        conexion = connection.cursor()
        serviciosHayduk = [
                        "1065", "1302", "1329", "1394", "1396", "1397", "1400", "1401", "1621", "2420",
                        "2668", "2760", "2768", "2769", "2770", "2771", "2772", "3116", "3117", "3118",
                        "3119", "3120", "3121", "3122", "3130", "3174", "3269", "3295", "3296", "3311",
                        "3336", "3349", "3350", "3357", "3364", "3398", "3400", "3439", "3441", "3444",
                        "3446", "3456", "3459", "3467", "3471", "3480", "3481", "3498", "3499", "3500",
                        "3501", "3504", "3506", "3509", "3512", "3536", "3552", "3553", "3558", "3608",
                        "3611", "3612", "3622", "3630", "3644", "3645", "3655", "3656", "3658", "3659",
                        "3667", "3678", "3716"]

        params = self.request.query_params.dict()

        if params:

            if params['idServicio'] and params['tipoPersonal']:

                idServicio = params['idServicio']
                tipoPersonal = params['tipoPersonal']

                if idServicio == '' or tipoPersonal == '':
                    return Response({
                        'error': 'hay algun campo requerido que se encuentra vacio'
                    }, status=status.HTTP_400_BAD_REQUEST)

                else:


                    if(params['idServicio'] in serviciosHayduk):
                        print('CAMBIANDO EL CURSOR A LA BD DE HAYDUK')
                        conexion = connections['bd_hayduk'].cursor()
                    

                    with conexion as cursor:

                        cursor.execute('EXEC [dbo].[AppCa_LISTAR_AUTORIZANTES] {0}, {1}'.format(idServicio, tipoPersonal))
                        autorizantes_data = cursor.fetchall()

                        if autorizantes_data:

                            for autorizante in autorizantes_data:
                                dataTemp = {
                                    'codigo': autorizante[0],
                                    'cod_personal': autorizante[1],
                                    'nombre_personal': autorizante[2],
                                    'dni_personal': autorizante[3]
                                }

                                data.append(dataTemp)

                            autorizantes_serializer = self.get_serializer(data=data, many=True)

                            if autorizantes_serializer.is_valid():
                                return Response(autorizantes_serializer.data, status=status.HTTP_200_OK)

                            else:
                                return Response(autorizantes_serializer.errors,
                                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
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
