from rest_framework.routers import DefaultRouter
from apps.fotos_acceso.api.views import  *


router = DefaultRouter()
router.register(r'', FotosAccesoViewSet, basename='fotos-acceso')
router.register('copiar_foto', CopiarFotoViewSet, basename= 'copiar-foto')
urlpatterns = router.urls