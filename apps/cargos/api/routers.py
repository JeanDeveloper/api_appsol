from rest_framework.routers import DefaultRouter
from apps.cargos.api.views import *

router = DefaultRouter()
router.register('', CargosViewSet, basename='cargos')
urlpatterns = router.urls
