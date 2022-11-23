from apps.datos_acceso.api.serializers import *
from django.db import connection, connections
from rest_framework import viewsets, status
from rest_framework.response import Response

class DatosAccesoViewSet(viewsets.GenericViewSet):

    serializer_class = DatosAccesoSerializer

    def create( self, request ):

        try:

            conectionCursor = connection.cursor();

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

            if request.data['cod_servicio'] in serviciosHayduk:
                # print(' se cambio a hayduk')
                conectionCursor = connections['bd_hayduk'].cursor()

            if request.data['cod_servicio'] in serviciosTasa:
                # print(' se cambio a tasa')
                conectionCursor = connections['bd_tasa'].cursor()

            with conectionCursor as cursor:

                cursor.execute(
                    "DECLARE @result INT;"
                    "EXEC [dbo].[APPS_REGISTRAR_DATOS_ACCESO] {0}, '{1}', '{2}', {3}, @codigo_dato_acceso_creado = @result OUTPUT;"
                    "SELECT @result as codigo_dato_acceso".format(
                        request.data['cod_mov_peatonal'], request.data['descripcion'], 
                        request.data['creado_por'], request.data['cod_tipo_dato_acceso']
                    )   
                )

                response = cursor.fetchone()

                if response: 
                    return Response({
                        'codigo_dato_acceso' : response[0] 
                    }, status=status.HTTP_201_CREATED)

        finally:
            pass

    def list(self, request):

        data = []
        params = self.request.query_params.dict()

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

            conectionCursor = connection.cursor();

            if params:

                if params['tipo_movimiento'] and params['codigo_servicio'] and params['documento']:

                    if params['codigo_servicio'] in serviciosHayduk:
                        conectionCursor = connections['bd_hayduk'].cursor()

                    if params['codigo_servicio'] in serviciosTasa:
                        conectionCursor = connections['bd_tasa'].cursor()

                    with conectionCursor as cursor:

                        cursor.execute('EXEC [dbo].[APPS_OBTENER_DATOS_ACCESO] {0}, {1}, {2}'.format(
                            params['tipo_movimiento'], params['codigo_servicio'], params['documento']
                        ))

                        datos_acceso = cursor.fetchall()

                        for dato_acceso in datos_acceso:

                            dataTemp = {
                                'codigo_dato_acceso'    : dato_acceso[0],
                                'codigo_mov_peatonal'   : dato_acceso[1],
                                'descripcion'           : dato_acceso[2],
                                'fecha_creacion'        : dato_acceso[3],
                                'creado_por'            : dato_acceso[4],
                                'cod_tipo_dato_acceso'  : dato_acceso[5],
                                'pathImage'             : dato_acceso[6]
                            }

                            data.append(dataTemp)

                        datos_acceso_serializer = self.get_serializer( data = data, many = True)

                        if datos_acceso_serializer.is_valid():
                            return Response(datos_acceso_serializer.data, status=status.HTTP_200_OK )
                        else:
                            return Response(datos_acceso_serializer.errors, status=status.HTTP_400_BAD_REQUEST )

                else:
                    return Response({
                        'error': 'Ingrese los parametros requeridos'
                    }, status=status.HTTP_400_BAD_REQUEST)
        finally:
            pass


class DatosAccesoSalidaViewSet(viewsets.GenericViewSet):

    serializer_class = DatosAccesoSalidaSerializer

    def list(self, request):

        params = self.request.query_params.dict()

        if params.keys().__contains__('') & params.keys().__contains__('documento'):
            codServicio = params['codServicio']
            documento   = params['documento']

            with connection.cursor() as cursor:
                cursor.execute("EXEC [dbo].[APPS_OBTENER_DATOS_ACCESO_ULTIMO_MOVIMIENTO] {0}, {1} ".format(codServicio, documento))
                datos_acceso_salida = cursor.fetchone()

                print(datos_acceso_salida)

                data = {
                    'cod_mov'          : '' if datos_acceso_salida == None else datos_acceso_salida[0],
                    'cod_datos_acceso' : 0  if datos_acceso_salida == None else datos_acceso_salida[1],
                    'guia_mov'         : '' if datos_acceso_salida == None else datos_acceso_salida[2],
                    'url_guia_mov'     : '' if datos_acceso_salida == None else datos_acceso_salida[3],
                    'material_mov'     : '' if datos_acceso_salida == None else datos_acceso_salida[4],
                    'url_material_mov' : '' if datos_acceso_salida == None else datos_acceso_salida[5],
                }

                datos_acceso_serializer = self.get_serializer(data=data)

                if(datos_acceso_serializer.is_valid()):
                    return Response(datos_acceso_serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(datos_acceso_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({
                'error': 'Por favor ingrese los parametros requeridos'
            }, status=status.HTTP_400_BAD_REQUEST )
