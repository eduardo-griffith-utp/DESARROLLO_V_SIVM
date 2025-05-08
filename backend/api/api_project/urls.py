from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # API v1 - Endpoints principales
    path('api/v1/', include([
        path('', include('core.urls')),  # Ruta base de la API (ej: api/v1/)
        path('recognition/', include('recognition.urls')),  # Recognition
        path('core/', include('core.urls')),  # Core (si es necesario)
        path('items/', include('items.urls')),  # Items
    ])),
    
    # Autenticación JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# Servir archivos multimedia en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)