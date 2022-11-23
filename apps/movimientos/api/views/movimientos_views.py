from apps.movimientos.api.serializers.movimiento_serializers import *
from django.db import connection, connections
from rest_framework import viewsets, status
from rest_framework.response import Response

class MovimientosViewSet(viewsets.GenericViewSet):

    serializer_class = MovimientosListSerializer

    def list(self, request):
        data = []
        conexion = connection.cursor();

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
            "1500", "1501", "1502", "1503", "1504", "1505", "1506", "1512", "1513", "2016", 
            "2213", "2511", "2681", "2702", "2853", "2928", "3049", "3131", "3134", "3136", 
            "3152", "3179", "3180", "3187", "3189", "3190", "3191", "3192", "3193", "3194", 
            "3244", "3245", "3246", "3247", "3248", "3251", "3253", "3270", "3292", "3399", 
            "3443", "3449", "3450", "3455", "3457", "3487", "3488", "3507", "3584", "3603", 
            "3604", "3610", "3687", "3720", "3722"
        ]

        try:

            params = self.request.query_params.dict()

            if params.keys().__contains__('tipoMovimiento') & params.keys().__contains__('idServicio') & params.keys().__contains__('tipoPersonal'):
                tipoMovimiento = params['tipoMovimiento']
                idServicio     = params['idServicio']
                tipoPersonal   = params['tipoPersonal']

                if(params['idServicio'] in serviciosHayduk):
                    conexion = connections['bd_hayduk'].cursor()

                if(params['idServicio'] in serviciosTasa):
                    conexion = connections['bd_tasa'].cursor()

                with conexion as cursor:
                    cursor.execute( "EXEC [dbo].[AppCA_ListadoMovimientosPeople] {0}, {1}, {2} , {3}".format( idServicio, tipoPersonal, "''", tipoMovimiento ) )
                    movimientos_data = cursor.fetchall()

                    for movimiento in movimientos_data:
                        dataTemp = {
                            'cod_movimiento': movimiento[0],
                            'nombres': movimiento[1],
                            'dni': movimiento[2],
                            'sexo': movimiento[3],
                            'cargo': movimiento[4],
                            'empresa': movimiento[5],
                            'fecha_movimiento': movimiento[6],
                            'fecha_salida': '' if movimiento[7] is None else movimiento[7],
                            'tipo_ingreso': movimiento[8],
                            'tipo_personal': movimiento[9],
                            'imagen': movimiento[10]
                        }
                        data.append(dataTemp)
                    movimientos_serializer = self.get_serializer( data=data, many=True )
                    if movimientos_serializer.is_valid():
                        return Response(movimientos_serializer.data, status=status.HTTP_200_OK)
                    else:
                        return Response(movimientos_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response({
                    'error': 'Por favor ingresar los 3 parametros requeridos'
                }, status=status.HTTP_400_BAD_REQUEST)

        finally:
            pass

    def create(self, request):

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

        if  request.data['codigo_servicio'] in serviciosHayduk:

            with connections['bd_hayduk'].cursor() as cursor:
                cursor.execute( 
                    "DECLARE @result1 SMALLINT, @result2 NUMERIC(18,0);"
                    "EXEC [dbo].[APPS_People_Crear_Movimiento] {0}, {1}, {2}, {3}, {4}, {5}, {6}, '00', '{7}',"
                    "@estado_transaccion=@result1 OUTPUT, @codigo_movimiento_creado=@result2 OUTPUT;  "
                    "SELECT @result1 as estado_transaccion, @result2 as cod_mov_peatonal "
                    .format(
                        request.data['codigo_personal'],    request.data['codigo_servicio'], request.data['codigo_tipo_movimiento'],
                        request.data['codigo_tipo_motivo'], request.data['codigo_empresa'],  request.data['autorizado_por'],
                        request.data['codigo_area'],  request.data['creado_por']
                    )
                )

                response = cursor.fetchone()

                if response:
                    return Response({
                        'message': 'movimiento creado satisfactoriamente',
                        'codigo_transaccion': response[0],
                        'id_movimiento': int(response[1])
                    }, status=status.HTTP_201_CREATED)
                else:
                    return Response({
                        'message': 'hubo un error al momento de crear un movimiento'
                    }, status=status.HTTP_400_BAD_REQUEST)

        else:

            if request.data['codigo_servicio'] in serviciosTasa:

                with connections['bd_tasa'].cursor() as cursor:
                    cursor.execute(
                        "DECLARE @result1 SMALLINT, @result2 NUMERIC(18,0);"
                        "EXEC [dbo].[APPS_People_Crear_Movimiento] {0}, {1}, {2}, {3}, {4}, {5}, {6}, '00', '{7}',"
                        "@estado_transaccion=@result1 OUTPUT, @codigo_movimiento_creado=@result2 OUTPUT;  "
                        "SELECT @result1 as estado_transaccion, @result2 as cod_mov_peatonal "
                        .format(
                            request.data['codigo_personal'],    request.data['codigo_servicio'], request.data['codigo_tipo_movimiento'],
                            request.data['codigo_tipo_motivo'], request.data['codigo_empresa'],  request.data['autorizado_por'],
                            request.data['codigo_area'],  request.data['creado_por']
                        )
                    )

                    response = cursor.fetchone()
                    print(response)


                    if response:
                        return Response({
                            'message': 'movimiento creado satisfactoriamente',
                            'codigo_transaccion': response[0],
                            'id_movimiento': int(response[1])
                        }, status=status.HTTP_201_CREATED)
                    else:
                        return Response({
                            'message': 'hubo un error al momento de crear un movimiento'
                        }, status=status.HTTP_400_BAD_REQUEST)

            else:

                with connection.cursor() as cursor:
                    cursor.execute(
                        "DECLARE @result SMALLINT, @result1 SMALLINT, @result2 NUMERIC(18,0);"
                        "EXECUTE @result = [dbo].[APPS_CREAR_MOVIMIENTO_QA]"
                        " 0, {0}, {1}, {2}, {3}, {4}, 0, 0, {5}, \" \", '', 0, '', 0,'N', '{6}', 1, -1, '', '', '', {7}, '00', 0, '', " 
                        "@estado_transaccion=@result1 OUTPUT, @codigo_movimiento_creado=@result2 OUTPUT;  "
                        "SELECT @result1 as estado_transaccion, @result2 as cod_mov_peatonal ".format(
                            request.data['codigo_personal'],    request.data['codigo_servicio'], request.data['codigo_tipo_movimiento'],
                            request.data['codigo_tipo_motivo'], request.data['codigo_empresa'],  request.data['autorizado_por'],
                            request.data['creado_por'],         request.data['codigo_area'],
                        )   
                    )

                    response = cursor.fetchone()

                    if response:
                        return Response({
                            'message': 'movimiento creado satisfactoriamente',
                            'codigo_transaccion': response[0],
                            'id_movimiento': int(response[1])
                        }, status=status.HTTP_201_CREATED)
                    else:
                        return Response({
                            'message': 'hubo un error al momento de crear un movimiento'
                        }, status=status.HTTP_400_BAD_REQUEST)

class UltimoMovimientoViewSet(viewsets.GenericViewSet):

    def list(self, request):

        conexion = connection.cursor();

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
            "1500", "1501", "1502", "1503", "1504", "1505", "1506", "1512", "1513", "2016", 
            "2213", "2511", "2681", "2702", "2853", "2928", "3049", "3131", "3134", "3136", 
            "3152", "3179", "3180", "3187", "3189", "3190", "3191", "3192", "3193", "3194", 
            "3244", "3245", "3246", "3247", "3248", "3251", "3253", "3270", "3292", "3399", 
            "3443", "3449", "3450", "3455", "3457", "3487", "3488", "3507", "3584", "3603", 
            "3604", "3610", "3687", "3720", "3722"
        ]

        try:
            params = self.request.query_params.dict()
            if params.keys().__contains__('codServicio') & params.keys().__contains__('codPersonal'):
                codServicio  = params['codServicio']
                codPersonal  = params['codPersonal']

                if(codServicio in serviciosHayduk):
                    print('CAMBIANDO EL CURSOR A LA BD DE HAYDUK')
                    conexion = connections['bd_hayduk'].cursor()

                if(codServicio in serviciosTasa):
                    print('CAMBIANDO EL CURSOR A LA BD DE TASA')
                    conexion = connections['bd_tasa'].cursor()

                with conexion as cursor:
                    cursor.execute ( "EXEC [dbo].[APPS_OBTENER_DATOS_ULTIMO_MOVIMIENTO] {0}, {1}".format(codServicio, codPersonal))
                    codigo_movimiento = cursor.fetchone();
                    # print(codigo_movimiento)
                    if codigo_movimiento:
                        return Response({
                            'codigo_movimiento': int(codigo_movimiento[0])
                        }, status=status.HTTP_201_CREATED)
                    else:
                        return Response({
                            'message': 'hubo un error al momento de obtener el ultimo movimiento'
                        }, status=status.HTTP_400_BAD_REQUEST)
        
        finally:
            pass
