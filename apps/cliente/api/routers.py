from apps.cliente.api.serializers import *
from apps.cliente.api.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ClientesViewSet, basename='clientes')
router.register(r'servicios', ServiciosXClienteViewSet, basename='servicios_x_cliente')
urlpatterns = router.urls
