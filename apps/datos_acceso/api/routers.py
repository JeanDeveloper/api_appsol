from rest_framework.routers import DefaultRouter
from apps.datos_acceso.api.views import DatosAccesoViewSet


router = DefaultRouter()
router.register('', DatosAccesoViewSet, basename='datos_acceso')
urlpatterns = router.urls
