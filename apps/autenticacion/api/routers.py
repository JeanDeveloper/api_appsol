from rest_framework.routers import DefaultRouter
from apps.autenticacion.api.views import AutenticacionViewSet

router = DefaultRouter()
router.register(r'', AutenticacionViewSet, basename='autenticacion')

urlpatterns = router.urls