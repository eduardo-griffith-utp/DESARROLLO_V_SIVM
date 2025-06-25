from django.urls import path
from . import views # La importación de las vistas es relativa a este archivo

urlpatterns = [
    # Image Endpoints (URLs completas serán /api/v1/recognition/images/...)
    path('images/capture/', views.capture_images, name='capture-images'),
    path('images/<str:image_id>/analysis/', views.get_image_analysis, name='image-analysis'),

    # Multimedia Endpoints (URLs completas serán /api/v1/recognition/multimedia/...)
    path('multimedia/by-tag/<str:tag>/', views.get_multimedia_by_tag, name='multimedia-by-tag'),

    # History Endpoints (URLs completas serán /api/v1/recognition/history/...)
    path('history/', views.get_history, name='history'),

    path('items/', views.get_items, name='items-list'),
    path('items/<int:item_id>/', views.get_item_detail, name='item-detail'),
]
