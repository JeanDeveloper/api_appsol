from apps.consulta_datos_persona.api.serializers import *
from django.db import connection, connections
from django.shortcuts import render
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
                        "3667", "3678", "3716"]

        conexion = connection.cursor()

        try:

            params = self.request.query_params.dict()

            if params.keys().__contains__('codServicio') & params.keys().__contains__('codPersonal') & params.keys().__contains__('tipoMaster'):
                    codServicio = params['codServicio']
                    codPersona  = params['codPersonal']
                    tipoMaster  = params['tipoMaster']

                    if codServicio in serviciosHayduk:
                        conexion = connections['bd_hayduk'].cursor()


                    with conexion as cursor:
                        cursor.execute(" EXEC [People_Verificar_Ingreso_Persona] {0}, {1}, {2}"
                        .format(codServicio, codPersona, tipoMaster))

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