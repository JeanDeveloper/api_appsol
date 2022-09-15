from apps.datos_acceso.api.views import DatosAccesoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', DatosAccesoViewSet, basename='datos_acceso')
urlpatterns = router.urls
