# backend/api/items/urls.py
from django.urls import path
from . import views # O importa tus vistas de items

urlpatterns = [
    path('', views.get_all_items, name='all-items'), # /api/v1/items/
    path('<int:item_id>/', views.get_single_item, name='single-item'), # /api/v1/items/123/
]