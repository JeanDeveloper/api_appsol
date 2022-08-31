from apps.cargos.api.serializers import CargosSerializer
from django.db import connection
from rest_framework import viewsets, status
from rest_framework.response import Response


class CargosViewSet(viewsets.GenericViewSet):
    serializer_class = CargosSerializer

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
                        "3667", "3678", "3716"]


        try:
            params = self.request.query_params.dict()

            if params.keys().__contains__('cargo') & params.keys().__contains__('codCliente'):
                cargo = params['cargo']
                codCliente = params['codCliente']

                with connection.cursor() as cursor:
                    cursor.execute(" EXEC [dbo].[USP_SICOS_2019_BUSCAR_CARGOS_DEALER_S_COMBO_UNIFICACION] '', {0}".format(codCliente))

                    cargos_data = cursor.fetchall()

                    for cargo in cargos_data:
                        dataTemp = {
                            'codigo': cargo[0],
                            'cargo': cargo[1]
                        }
                        data.append(dataTemp)

                    cargos_serializer = self.get_serializer(data=data, many=True)

                    if cargos_serializer.is_valid():
                        return Response(cargos_serializer.data, status=status.HTTP_200_OK)
                    else:
                        return Response(cargos_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:

                return Response({
                    'error': 'Por favor ingresar los 2 parametros requeridos'
                }, status=status.HTTP_400_BAD_REQUEST)

        finally:
            pass


