from apps.consulta_vehiculo.api.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'consulta', ConsultaVehiculoViewSet, basename= 'consultar-vehiculo')
router.register(r'verificacion', VerificarVehiculoViewSet, basename= 'verificar-vehiculo')
urlpatterns = router.urls