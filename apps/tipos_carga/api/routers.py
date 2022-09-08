from apps.tipos_carga.api.views import TiposCargaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', TiposCargaViewSet, basename='tipos_carga')
urlpatterns = router.urls