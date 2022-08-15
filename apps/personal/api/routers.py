from rest_framework.routers import DefaultRouter
from apps.personal.api.views import *

router = DefaultRouter()
router.register('', PersonalViewSet, basename='personal')
urlpatterns = router.urls
