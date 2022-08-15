from django.db import connection
from rest_framework.response import Response
from apps.personal.api.serializers import *
from rest_framework import viewsets, status


class PersonalViewSet(viewsets.GenericViewSet):

    def create(self, request):

        serializer = PersonalSerializer(data=request.data)

        if serializer.is_valid():

            with connection.cursor() as cursor:

                cursor.execute("DECLARE @result1 SMALLINT,  @result2 NUMERIC(18,0),  @result VARCHAR(500);"
                                "EXECUTE @result = [dbo].[USP_SICOS_2018_INSERTAR_MODIFICAR_PERSONAL_UNIFICACION_2021]"
                                " {0}, {1}, {2}, {3}, {4}, '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '', {12}, {13}, {14}, '{15}', '', '', 0,"
                                "@estado_transaccion=@result1 OUTPUT, @codigo_personal_creado=@result2 OUTPUT "
                                "select @result1 as estado,  @result2 as personal_maestros".format(
                                request.data['codigo_personal'], request.data['codigo_tipo_personal'], request.data['codigo_empresa'],
                                request.data['codigo_tipo_documento'], request.data['codigo_cargo'],
                                request.data['nombre1'], request.data['nombre2'],
                                request.data['apellido1'], request.data['apellido2'],
                                request.data['doc_personal'], request.data['sexo'],
                                request.data['creado_por'], request.data['es_autorizante'],
                                request.data['habilitado'], request.data['tiene_foto'],
                                request.data['codigo_cliente_control']
                ))

                result_data = cursor.fetchone()
                print(result_data)

                if result_data[0] == 1:

                    return Response({

                        'message': 'El personal fue creado satisfactoriamente',
                        'personal_maestro': int(result_data[1])

                    }, status=status.HTTP_201_CREATED)

                elif result_data[0] == -2:

                    return Response({

                        'message': 'El documento ya se encuentra registrado',
                        'personal_maestro': -1

                    }, status=status.HTTP_403_FORBIDDEN)
                else:
                    return Response({

                        'message': 'El documento ya se encuentra registrado',
                        'personal_maestro': -1

                    }, status=status.HTTP_403_FORBIDDEN)

        else:

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)