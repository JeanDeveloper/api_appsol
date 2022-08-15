from rest_framework.routers import DefaultRouter

from apps.areas.api.views import AreasListViewSet

router = DefaultRouter()
router.register('', AreasListViewSet, basename='areas')
urlpatterns = router.urls
