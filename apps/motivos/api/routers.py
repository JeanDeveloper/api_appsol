from rest_framework.routers import DefaultRouter
from apps.motivos.api.views import MotivosListViewSet

router = DefaultRouter()
router.register('', MotivosListViewSet, basename='motivos')
urlpatterns = router.urls
