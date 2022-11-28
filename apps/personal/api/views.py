from apps.personal.api.serializers import *
from django.db import connection, connections
from rest_framework import viewsets, status
from rest_framework.response import Response

class PersonalViewSet(viewsets.GenericViewSet):
    
    serializer_class = PersonalSerializer

    def create(self, request):

        if (request.data['codigo_cliente_control'] == '00005'):
            with connections['bd_hayduk']. cursor() as cursor:
                cursor.execute(
                    "DECLARE @result1 SMALLINT, @result2 NUMERIC(18,0), @result VARCHAR(500);"
                    "EXECUTE @result = [dbo].[USP_SICOS_2018_INSERTAR_MODIFICAR_PERSONAL]"
                    "{0}, {1}, {2}, {3}, {4}, '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '', {12}, {13}, {14}, "
                    "@estado_transaccion=@result1 OUTPUT, @codigo_personal_creado=@result2 OUTPUT "
                    "select @result1 as estado, @result2 as personal_maestros".format(
                        request.data['codigo_personal'], request.data['codigo_tipo_personal'], request.data['codigo_empresa'],
                        request.data['codigo_tipo_documento'], request.data['codigo_cargo'], request.data['nombre1'],
                        request.data['nombre2'], request.data['apellido1'], request.data['apellido2'], 
                        request.data['doc_personal'], request.data['sexo'], request.data['creado_por'],
                        request.data['es_autorizante'], request.data['habilitado'], request.data['tiene_foto']
                    )
                )

                personal_data = cursor.fetchone()

                if personal_data[0] == 1:
                    return Response({
                        'message': 'El personal fue creado satisfactoriamente',
                        'personal_maestro': int(personal_data[1])
                    }, status=status.HTTP_201_CREATED)

                elif personal_data[0] == -2:
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
            if (request.data['codigo_cliente_control'] == '00002'):
                with connections['bd_tasa']. cursor() as cursor:
                    cursor.execute(
                        "DECLARE @result1 SMALLINT, @result2 NUMERIC(18,0), @result VARCHAR(500);"
                        "EXECUTE @result = [dbo].[USP_SICOS_2018_INSERTAR_MODIFICAR_PERSONAL]"
                        "{0}, {1}, {2}, {3}, {4}, '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '', {12}, {13}, {14}, "
                        "@estado_transaccion=@result1 OUTPUT, @codigo_personal_creado=@result2 OUTPUT "
                        "select @result1 as estado, @result2 as personal_maestros".format(
                            request.data['codigo_personal'], request.data['codigo_tipo_personal'], request.data['codigo_empresa'],
                            request.data['codigo_tipo_documento'], request.data['codigo_cargo'], request.data['nombre1'],
                            request.data['nombre2'], request.data['apellido1'], request.data['apellido2'], 
                            request.data['doc_personal'], request.data['sexo'], request.data['creado_por'],
                            request.data['es_autorizante'], request.data['habilitado'], request.data['tiene_foto']
                        )
                    )

                    result_data = cursor.fetchone()

                    if result_data[0] == 1:

                        return Response({

                            'message': 'El personal fue creado satisfactoriamente',
                            'personal_maestro': int(result_data[1])

                        }, status=status.HTTP_201_CREATED)

                    elif result_data[0] == -2:

                        return Response(
                            {
                                'message': 'El documento ya se encuentra registrado',
                                'personal_maestro': -1
                            }, 
                        status = status.HTTP_403_FORBIDDEN
                        )

                    else:
                        return Response({
                            'message': 'El documento ya se encuentra registrado',
                            'personal_maestro': -1
                        }, status=status.HTTP_403_FORBIDDEN)

            else:
                with connection.cursor() as cursor:
                    cursor.execute("DECLARE @result1 SMALLINT,  @result2 NUMERIC(18,0),  @result VARCHAR(500);"
                        "EXECUTE @result = [dbo].[APPS_CREAR_MODIFICAR_PERSONAL]"
                        " {0}, {1}, {2}, {3}, {4}, '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '', {12}, {13}, {14}, '{15}', '0', '', 0,"
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
                        return Response(
                            {
                                'message': 'El documento ya se encuentra registrado',
                                'personal_maestro': -1
                            }, 
                        status = status.HTTP_403_FORBIDDEN
                        )
                    elif result_data[0] == -4:
                        return Response(
                            {
                                'message': 'El nombre completo ya se encuentra registrado',
                                'personal_maestro': -1
                            }, 
                        status = status.HTTP_403_FORBIDDEN
                        )
                    else:
                        return Response({
                            'message': 'El documento ya se encuentra registrado',
                            'personal_maestro': -1
                        }, status=status.HTTP_403_FORBIDDEN)


    def list(self, request):

        try:
            params = self.request.query_params.dict()

            if params.keys().__contains__('cod_personal') & params.keys().__contains__('codCliente'):

                codPersonal     = params['cod_personal']
                codCliente   = params['codCliente']

                with connection.cursor() as cursor:
                    cursor.execute( "EXEC [dbo].[APPS_LISTAR_PERSONAL_MODIFICAR_S_UNIFICACION] {0}, {1}".format( codPersonal, codCliente ) )

                    personal_data = cursor.fetchone()
                    print(personal_data)

                    dataTemp = {
                        'codigo_personal'      : personal_data[0],
                        'codigo_tipo_personal' : personal_data[1],
                        'codigo_empresa'       : personal_data[2],
                        'codigo_tipo_documento': personal_data[3],
                        'codigo_cargo'         : personal_data[4],
                        'codigo_area'          : personal_data[5],
                        'nombre1'              : personal_data[6],
                        'nombre2'              : '' if personal_data[7] is None else personal_data[7],
                        'apellido1'            : personal_data[8],
                        'apellido2'            : personal_data[9],
                        'doc_personal'         : personal_data[10],
                        'sexo'                 : personal_data[11],
                        'es_autorizante'       : personal_data[12],
                        'es_lista_negra'       : personal_data[13],
                        'tiene_foto'           : personal_data[14],
                        'imgPath'              : personal_data[15],
                        'brevete'              : personal_data[16],
                        'nombre_turno_personal': personal_data[17],
                        'f_nacimiento'         : personal_data[18],
                        'dosis_completa'       : personal_data[19],
                        'telefono'             : personal_data[20],
                    }

                personal_serializer = self.get_serializer( data=dataTemp )

                if personal_serializer.is_valid():
                    return Response(personal_serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(personal_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response({
                    'error': 'Por favor ingresar los parametros requeridos'
                }, status=status.HTTP_400_BAD_REQUEST)

        finally:
            pass


class TipoPersonalViewSet(viewsets.GenericViewSet):
    serializer_class = TiposPersonalSerializer

    def list(self, request):

        data = []

        try:
            params = self.request.query_params.dict()

            if params.keys().__contains__('codCliente'):
                codCliente = params['codCliente']

                with connection.cursor() as cursor:
                    # print('buscar en el multicontrol')
                    cursor.execute(" EXEC [USP_SICOS_2014_LISTAR_TIPOS_PERSONAL_S_UNIFICACION] '{0}' ".format(codCliente))
                    tipos_persona = cursor.fetchall()

                    for tiposPersona in tipos_persona:
                        dataTemp = {
                            'codigo': tiposPersona[0],
                            'personal' : tiposPersona[1]
                        }

                        data.append(dataTemp)
                    tipoPersona_serializer = self.get_serializer( data= data, many=True)

                    if tipoPersona_serializer.is_valid():
                        return Response(tipoPersona_serializer.data, status = status.HTTP_200_OK)
                    else:
                        return  Response(tipoPersona_serializer.errors, status= status.HTTP_400_BAD_REQUEST)
            else:
                return Response({
                    'error': 'Por favor ingrese el parametro requerido'
                }, status=status.HTTP_400_BAD_REQUEST)

        finally:
            pass

class ValidacionPersonalViewSet(viewsets.GenericViewSet):

    serializer_class = ValidacionPersonalSerializer

    def list(self, request):

        try:

            params = self.request.query_params.dict() 
            conexion = connection.cursor()

            if params.keys().__contains__('documento') and  params.keys().__contains__('codServicio') and params.keys().__contains__('codCliente'):
                documento   = params['documento']
                codCliente  = params['codCliente']
                codServicio = params['codServicio']

                print(codCliente, codServicio)

                if ( codCliente  == '00002' ):
                    print('se cambio a tasa')
                    conexion = connections['bd_tasa'].cursor()

                if (  codCliente == '00005' ):
                    print('se cambio a hayduk')
                    conexion = connections['bd_hayduk'].cursor()

                with conexion  as cursor:
                    cursor.execute( """ 
                        DECLARE @result INT, @result1 NUMERIC(18,0);
                        EXEC [dbo].[APPS_VALIDAR_PERSONAL_X_CLIENTE] '{0}',  {1}, {2}, @estado_transaccion = @result OUTPUT, @codigo_personal = @result1 OUTPUT
                        SELECT @result as estado_transaccion, @result1 as codigo_personal               
                    """.format(
                        documento, codServicio, codCliente
                    ))

                    response =  cursor.fetchone();

                    data = {
                        'estado_transaccion': response[0],
                        'cod_personal' : response[1]
                    }

                    response_serializer = self.get_serializer( data = data )

                    if response_serializer.is_valid():
                        return Response(response_serializer.data, status = status.HTTP_200_OK)
                    else:
                        return  Response(response_serializer.errors, status= status.HTTP_400_BAD_REQUEST)



            else:
                return Response({
                    'error': 'Por favor ingrese el parametro requerido'
                }, status=status.HTTP_400_BAD_REQUEST)

        finally:
            pass

class HabilitarPersonalViewSet(viewsets.GenericViewSet):

    def create(self, request):

        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                DECLARE @result1 SMALLINT;
                EXECUTE [dbo].[APPS_HABILITAR_PERSONAL_U_UNIFICACION] {0}, '{1}', '{2}', @estado_transaccion=@result1 OUTPUT
                SELECT @result1 as estado
                """.format(
                    request.data['codigo_personal'], request.data['creado_por'], request.data['codigo_cliente_control']
                ))

                result_data = cursor.fetchone()

                print(result_data)

                if result_data[0] == 0:
                    return Response({
                        'message': 'El personal no existe en la base de datos',
                    }, status=status.HTTP_200_OK)

                elif result_data[0] == 1:
                    return Response(
                        {
                            'message': 'La relacion  y el personal fueron habilitados exitosamente',
                        }, 
                    status = status.HTTP_200_OK
                    )
                elif result_data[0] == 2:
                    return Response(
                        {
                            'message': 'La relacion fue creado existosamente',
                        }, 
                    status = status.HTTP_201_CREATED
                    )

        finally:
            pass