from rest_framework.routers import SimpleRouter
from .views import CapturedImageViewSet

router = SimpleRouter()
# Ruta: POST /api/v1/images/capture/
router.register(r'api/v1/images', CapturedImageViewSet, basename='capturedimage')

urlpatterns = router.urls