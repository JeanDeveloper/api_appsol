from rest_framework.routers import DefaultRouter
from apps.empresas.api.views import *

router = DefaultRouter()
router.register('', EmpresasViewSet, basename='empresas')
urlpatterns = router.urls
