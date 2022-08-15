from rest_framework.routers import DefaultRouter
from apps.movimientos.api.views.movimientos_views import *

router = DefaultRouter()

router.register(r'', MovimientosViewSet, basename='movimientos')



urlpatterns = router.urls
