from rest_framework.routers import DefaultRouter
from apps.usuario.api.views import UsuarioPermisosViewSet

router = DefaultRouter()
# router.register(r'', UsuarioPermisosViewSet, basename='usuario')
router.register(r'permisos', UsuarioPermisosViewSet, basename='permisos')
urlpatterns = router.urls
