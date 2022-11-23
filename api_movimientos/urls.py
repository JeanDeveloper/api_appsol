from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

#CODIGO DEL JWT
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )


# VARIABLE CREADA PARA EL SWAGGER
schema_view = get_schema_view(

    openapi.Info(
        title="Documentacion API",
        default_version='v0.1',
        description="Documentacion para la API de Movimientos",
        terms_of_service="https://www.facebook.com/jecachusa",
        contact=openapi.Contact(email="jecachusa.1996@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),

    public=True,
    permission_classes=[permissions.AllowAny],

)

urlpatterns = [
    path('admin/', admin.site.urls),

    # URL APP PEOPLE
    path('solgis/people/areas/',include('apps.areas.api.routers')), #MULTICONTROL, HAYDUK Y TASA
    path('solgis/people/movimientos/', include('apps.movimientos.api.routers')), #MULTICONTROL, HAYDUK Y TASA
    path('solgis/people/autorizantes/', include('apps.autorizantes.api.routers')), #MULTICONTROL, HAYDUK Y TASA
    path('solgis/people/motivos/', include('apps.motivos.api.routers')), #MULTICONTROL, HAYDUK Y TASA
    path('solgis/people/detalle-personal/', include('apps.detalle_personal.api.routers')), #MULTICONTROL, HAYUK Y TASA
    path('solgis/people/empresas/', include('apps.empresas.api.routers')), #MULTICONTROL, HAYDUK Y TASA
    path('solgis/people/cargos/', include('apps.cargos.api.routers')), #MULTICONTROL, HAYDUK Y TASA
    path('solgis/people/consulta-datos-persona/', include('apps.consulta_datos_persona.api.routers')), #MULTICONTROL, HAYDUK Y TASA.
    path('solgis/people/personal/', include('apps.personal.api.routers')),#MULTICONTROL, HAYDUK Y TASA
    path('solgis/people/datos_acceso/', include('apps.datos_acceso.api.routers')), #MULTICONTROL, HAYDUK Y TASA
    path('solgis/people/fotos_acceso/', include('apps.fotos_acceso.api.routers')), #MULTICONTROL, HAYDUK Y TASA

    # URL APP CARGO
    path('solgis/cargo/movimientos/', include('apps.movimientos_cargo.api.routers')),
    path('solgis/cargo/carga/', include('apps.tipos_carga.api.routers')),
    path('solgis/cargo/vehiculo/', include('apps.consulta_vehiculo.api.routers')),

    #URLS GENERALES
    path('solgis/autenticacion/', include('apps.autenticacion.api.routers')),
    path('solgis/dispositivo/', include('apps.device.api.routers')),
    path('solgis/usuario/', include('apps.usuario.api.routers')),

    # URLS THIRD
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

# SE ADICIONÓ EL METODO PARA SWAGGER
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]



# Usuario
#     Agente      dni
#     Supervisor  dni
#     Cliente
#     Administrador