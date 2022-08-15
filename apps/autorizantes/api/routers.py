from rest_framework.routers import DefaultRouter
from apps.autorizantes.api.views import AutorizantesViewSet

router = DefaultRouter()
router.register('', AutorizantesViewSet, basename='autorizantes')
urlpatterns = router.urls
