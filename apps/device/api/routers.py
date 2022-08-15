from apps.device.api.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', RegistrarDispositivoViewSet, basename='dispositivos')
router.register('estado', ConsultarEstadoViewSet, basename='estado_dispositivo')
urlpatterns = router.urls