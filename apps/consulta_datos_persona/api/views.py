from django.shortcuts import render
from rest_framework import viewsets, status
from apps.consulta_datos_persona.api.serializers import *
from django.db import connection
from rest_framework.response import Response


class ConsultaDatosPersonaViewSet(viewsets.GenericViewSet):
    serializer_class = ConsultaDatosPersonaSerializer

    def list( self, request):
        try:

            params = self.request.query_params.dict()

            if params.keys().__contains__('codServicio') & params.keys().__contains__('codPersonal') & params.keys().__contains__('tipoMaster'):
                    codServicio = params['codServicio']
                    codPersona  = params['codPersonal']
                    tipoMaster  = params['tipoMaster']

                    with connection.cursor() as cursor:
                        cursor.execute(" EXEC [People_Verificar_Ingreso_Persona] {0}, {1}, {2}"
                        .format(codServicio, codPersona, tipoMaster))

                        verificacion = cursor.fetchone()
                        print(verificacion)

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


                        verifiacion_data = self.get_serializer(data=data)

                        if verifiacion_data.is_valid():
                            return Response(verifiacion_data.data, status=status.HTTP_200_OK)
                        else:
                            return Response(verifiacion_data.errors, status=status.HTTP_400_BAD_REQUEST)
            
            else:

                return Response({
                    'error': 'Por favor ingresar los 3 parametros requeridos'
                }, status=status.HTTP_400_BAD_REQUEST)

        finally:
            pass