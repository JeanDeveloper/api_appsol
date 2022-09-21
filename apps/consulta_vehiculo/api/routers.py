from rest_framework.routers import DefaultRouter
from apps.consulta_vehiculo.api.views import *

router = DefaultRouter()

# router.register(r'', ConsultaVehiculoViewSet, basename= 'consulta-vehiculo')

router.register(r'consulta', ConsultaVehiculoViewSet, basename= 'consultar-vehiculo')

router.register(r'verificacion', VerificarVehiculoViewSet, basename= 'verificar-vehiculo')

urlpatterns = router.urls 
