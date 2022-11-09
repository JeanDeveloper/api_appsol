from apps.datos_acceso.api.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', DatosAccesoViewSet, basename='datos_acceso'),
router.register('salida', DatosAccesoSalidaViewSet, basename='datos_acceso_salida'),

urlpatterns = router.urls
