from apps.movimientos_cargo.api.views import MovimientosCargoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', MovimientosCargoViewSet, basename='movimientos_cargo')
urlpatterns = router.urls
