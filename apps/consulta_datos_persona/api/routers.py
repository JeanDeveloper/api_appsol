from apps.consulta_datos_persona.api.views import * 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ConsultaDatosPersonaViewSet, basename = 'consulta-datos')
urlpatterns = router.urls



