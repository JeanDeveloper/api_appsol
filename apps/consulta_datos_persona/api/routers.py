from rest_framework.routers import DefaultRouter
from apps.consulta_datos_persona.api.views import * 


router = DefaultRouter()
router.register('', ConsultaDatosPersonaViewSet, basename = 'consulta-datos')
urlpatterns = router.urls