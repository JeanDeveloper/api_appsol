from rest_framework.routers import DefaultRouter
from apps.personal.api.views import *

router = DefaultRouter()
router.register('', PersonalViewSet, basename='personal')
router.register(r'tipos', TipoPersonalViewSet, basename = 'tipos-personal' )
urlpatterns = router.urls
