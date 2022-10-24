from rest_framework.routers import DefaultRouter
from apps.movimientos.api.views.movimientos_views import *

router = DefaultRouter()

router.register(r'', MovimientosViewSet, basename='movimientos')
router.register('obtener_ultimo_movimiento', UltimoMovimientoViewSet, basename = 'ultimo_movimiento')
urlpatterns = router.urls
