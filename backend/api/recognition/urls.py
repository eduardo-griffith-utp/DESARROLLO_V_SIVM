from django.urls import path
from . import views

urlpatterns = [
    # Image Endpoints
    path('api/v1/images/capture/', views.capture_image, name='capture-image'),
    path('api/v1/images/<str:image_id>/analysis/', views.get_image_analysis, name='image-analysis'),

    # Multimedia Endpoints
    path('api/v1/multimedia/by-tag/<str:tag>/', views.get_multimedia_by_tag, name='multimedia-by-tag'),

    # History Endpoints
    path('api/v1/history/', views.get_history, name='history'),

    # Items Endpoints
    path('api/v1/items/', views.get_items, name='items-list'),
    path('api/v1/items/<int:item_id>/', views.get_item_detail, name='item-detail'),
]