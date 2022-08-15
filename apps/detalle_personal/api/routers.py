from rest_framework.routers import DefaultRouter
from apps.detalle_personal.api.views import DetallePersonaViewSet

router = DefaultRouter()
router.register('', DetallePersonaViewSet, basename='detalle_personal')
urlpatterns = router.urls
