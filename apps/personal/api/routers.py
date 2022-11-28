from rest_framework.routers import DefaultRouter
from apps.personal.api.views import *

router = DefaultRouter()
router.register('', PersonalViewSet, basename='personal')
router.register(r'tipos', TipoPersonalViewSet, basename = 'tipos-personal' )
router.register(r'validar', ValidacionPersonalViewSet, basename =  'validar-personal')
router.register(r'habilitar', HabilitarPersonalViewSet, basename= 'habilitar-personal')


urlpatterns = router.urls
