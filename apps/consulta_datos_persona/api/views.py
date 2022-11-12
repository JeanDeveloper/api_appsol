from apps.consulta_datos_persona.api.serializers import *
from django.db import connection, connections
from rest_framework import viewsets, status
from rest_framework.response import Response

class ConsultaDatosPersonaViewSet(viewsets.GenericViewSet):
    serializer_class = ConsultaDatosPersonaSerializer

    def list( self, request):

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

        conexion = connection.cursor()

        try:
            params = self.request.query_params.dict()
            if params.keys().__contains__('codServicio') & params.keys().__contains__('codPersonal') & params.keys().__contains__('tipoMaster'):
                    codServicio = params['codServicio']
                    codPersona  = params['codPersonal']
                    tipoMaster  = params['tipoMaster']

                    if codServicio in serviciosHayduk:
                        #print('entra a la bd de hayduk')
                        conexion = connections['bd_hayduk'].cursor()

                    if codServicio in serviciosTasa:
                        #print('entra a la bd de tasa')

                        conexion = connections['bd_tasa'].cursor()

                    with conexion as cursor:
                        cursor.execute(" EXEC [People_Verificar_Ingreso_Persona] {0}, {1}, {2}".format(codServicio, codPersona, tipoMaster))
                        verificacion = cursor.fetchone()

                        data = {
                            'valor': verificacion[0],
                            'mensaje': verificacion[1],
                            'cod_autorizacion': verificacion[2],
                            'cod_motivo': verificacion[3],
                            'cod_autorizante': verificacion[4],
                            'cod_area': verificacion[5],
                            'emo_fv': verificacion[6],
                            'sctr_pension_fv': verificacion[7],
                            'sctr_salud_fv': verificacion[8],
                            'fi_autorizacion': verificacion[9],
                            'fv_autorizacion': verificacion[10],
                        } 


                        verificacion_data = self.get_serializer(data=data)

                        if verificacion_data.is_valid():
                            return Response(verificacion_data.data, status=status.HTTP_200_OK)
                        else:
                            return Response(verificacion_data.errors, status=status.HTTP_400_BAD_REQUEST)
            
            else:

                return Response({
                    'error': 'Por favor ingresar los 3 parametros requeridos'
                }, status=status.HTTP_400_BAD_REQUEST)

        finally:
            pass