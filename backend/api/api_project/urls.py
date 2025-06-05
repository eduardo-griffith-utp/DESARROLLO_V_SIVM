from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # API v1 - Endpoints públicos
    path('api/v1/', include([
        path('recognition/', include('recognition.urls')),  # Endpoints de reconocimiento
        path('items/', include('items.urls')),             # Endpoints de ítems
        path('', include('core.urls')),                    # Endpoints principales (si los hay)
    ])),
]

# Servir archivos multimedia en desarrollo (opcional)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)