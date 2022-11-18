from apps.areas.api.serializers import AreasListSerializer
from django.db import connection, connections
from rest_framework import viewsets, status
from rest_framework.response import Response

class AreasListViewSet(viewsets.GenericViewSet):
    serializer_class = AreasListSerializer

    def list(self, request):

        data = []

        serviciosHayduk = [
            "1065", "1302", "1329", "1394", "1396", "1397", "1400", "1401", "1621", "2420",
            "2668", "2760", "2768", "2769", "2770", "2771", "2772", "3116", "3117", "3118",
            "3119", "3120", "3121", "3122", "3130", "3174", "3269", "3295", "3296", "3311",
            "3336", "3349", "3350", "3357", "3364", "3398", "3400", "3439", "3441", "3444",
            "3446", "3456", "3459", "3467", "3471", "3480", "3481", "3498", "3499", "3500",
            "3501", "3504", "3506", "3509", "3512", "3536", "3552", "3553", "3558", "3608",
            "3611", "3612", "3622", "3630", "3644", "3645", "3655", "3656", "3658", "3659",
            "3667", "3678", "3716"
        ]

        serviciosTasa = [
            "1500", "1501", "1502", "1503", "1504", "1505", "1506", "1512", "1513", "2016", "2213", 
            "2511", "2681", "2702", "2853", "2928", "3049", "3131", "3134", "3136", "3152", "3179", 
            "3180", "3187", "3189", "3190", "3191", "3192", "3193", "3194", "3244", "3245", "3246", 
            "3247", "3248", "3251", "3253", "3270", "3292", "3399", "3443", "3449", "3450", "3455", 
            "3457", "3487", "3488", "3507", "3584", "3603", "3604", "3610", "3687", "3720", "3722"
        ]

        params = self.request.query_params.dict()

        if params:

            if params['idServicio'] and params['codCliente']:

                idServicio = params['idServicio']
                codCliente = params['codCliente']

                if idServicio == '' or codCliente == '':
                    return Response({
                        'error': 'hay algun campo requerido que se encuentra vacio'
                    }, status=status.HTTP_400_BAD_REQUEST)

                else:

                    if(params['idServicio'] in serviciosHayduk):
                        print('CAMBIANDO EL CURSOR A LA BD DE HAYDUK')

                        with connections['bd_hayduk'].cursor() as cursor:
                            cursor.execute("EXEC [dbo].[AppCA_LISTAR_AREAS] '', {0} ".format(idServicio))
                            areas_data = cursor.fetchall()

                            if areas_data:

                                for area in areas_data:
                                    dataTemp = {
                                        'codigo': area[0],
                                        'area': area[1],
                                    }
                                    data.append(dataTemp)

                                area_serializer = self.get_serializer(data=data, many=True)

                                if area_serializer.is_valid():
                                    return Response(area_serializer.data, status=status.HTTP_200_OK)

                                else:
                                    return Response(area_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                            else:
                                return Response({'message': 'no hay data en la consulta'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                    else:

                        if (params['idServicio'] in serviciosTasa ):
                            # print('CAMBIANDO EL CURSOR A LA BD DE TASA')

                            with connections['bd_tasa'].cursor() as cursor:
                                cursor.execute("EXEC [dbo].[AppCA_LISTAR_AREAS] '', {0}".format(idServicio))
                                areas_data = cursor.fetchall()
                                if areas_data:
                                    for area in areas_data:
                                        dataTemp = {
                                            'codigo': area[0],
                                            'area'  : area[1],
                                        }
                                        data.append(dataTemp)
                                    area_serializer = self.get_serializer(data=data, many=True)
                                    if area_serializer.is_valid():
                                        return Response(area_serializer.data, status=status.HTTP_200_OK)
                                    else:
                                        return Response(area_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                                else:
                                    return Response({'message': 'no hay data en la consulta'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                        else:

                            with connection.cursor() as cursor:
                                cursor.execute('EXEC [dbo].[AppCA_LISTAR_AREAS] {0}, {1}'.format(idServicio, codCliente))
                                areas_data = cursor.fetchall()
                                if areas_data:
                                    for area in areas_data:
                                        dataTemp = {
                                            'codigo': area[0],
                                            'area': area[1],
                                        }
                                        data.append(dataTemp)
                                    area_serializer = self.get_serializer(data=data, many=True)
                                    if area_serializer.is_valid():
                                        return Response(area_serializer.data, status=status.HTTP_200_OK)
                                    else:
                                        return Response(area_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                                else:
                                    return Response({'message': 'no hay data en la consulta'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            else:
                return Response({
                    'error': 'Se necesitan los dos parametros solicitados'
                }, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({
                'error': 'Por favor enviar los parametros requeridos'
            }, status=status.HTTP_400_BAD_REQUEST)
