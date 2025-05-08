from django.urls import path
from . import views

urlpatterns = [
    # Endpoints de imágenes
    path('imagenes/capturar/', views.capturar_imagen, name='capturar_imagen'),
    path('imagenes/<str:id_imagen>/analisis/', views.obtener_analisis_imagen, name='analisis-imagen'),
    
    # Endpoints de Multimedia
    path('multimedia/por-etiqueta/<str:etiqueta>/', views.obtener_multimedia_por_etiqueta, name='multimedia-por-etiqueta'),
    
    # Endpoints de historial
    path('historial/', views.obtener_historial, name='historial'),
    
    # Endpoints de items
    path('items/', views.obtener_items, name='items'),
    path('items/<str:id_item>/', views.obtener_detalle_item, name='detalle-item'),
    
]