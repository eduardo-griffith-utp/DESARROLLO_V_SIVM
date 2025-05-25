from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
import uuid
import re
import os
from django.conf import settings

# ======================
# CLASES Y HELPERS
# ======================
class ErrorValidacionSeguridad(Exception):
    """Excepción personalizada para errores de validación"""
    def __init__(self, codigo, mensaje, detalles=""):
        self.codigo = codigo
        self.mensaje = mensaje
        self.detalles = detalles

def respuesta_error(codigo, mensaje, detalles="", codigo_estado=status.HTTP_400_BAD_REQUEST):
    """Formato estandarizado para respuestas de error"""
    return Response(
        {
            "estado": "error",
            "error": {
                "codigo": codigo,
                "mensaje": mensaje,
                "detalles": detalles
            }
        },
        status=codigo_estado
    )

# ======================
# DATOS DUMMY (SIMULAN DB)
# ======================
ITEMS_DB = {
    1: {
        "id": 1,
        "nombre": "Fruta",
        "descripcion": "Frutas comestibles",
        "ejemplos": ["manzana", "banana", "naranja"],
        "tags_relacionados": ["comida", "saludable"],
        "fecha_creacion": "2025-01-10"
    },
    2: {
        "id": 2,
        "nombre": "Electrónica",
        "descripcion": "Dispositivos electrónicos",
        "ejemplos": ["televisor", "celular", "laptop"],
        "tags_relacionados": ["tecnología", "gadgets"],
        "fecha_creacion": "2025-01-15"
    },
    3: {
        "id": 3,
        "nombre": "Vehículos",
        "descripcion": "Medios de transporte",
        "ejemplos": ["automóvil", "motocicleta", "bicicleta"],
        "tags_relacionados": ["transporte", "movilidad"],
        "fecha_creacion": "2025-02-01"
    }
}

MULTIMEDIA_DB = {
    'naturaleza': [
        {
            "id": "mult_001",
            "tipo": "imagen",
            "url": "/media/naturaleza/bosque.jpg",
            "etiquetas": ["naturaleza", "bosque"]
        }
    ],
    'tecnologia': [
        {
            "id": "mult_002",
            "tipo": "video",
            "url": "/media/tecnologia/ia.mp4",
            "etiquetas": ["tech", "ia"]
        }
    ]
}

HISTORIAL_DB = [
    {
        "id": "hist_001",
        "id_imagen": "img_001",
        "usuario": "default_user",
        "fecha": "2025-04-16T10:15:00Z",
        "descripcion": "Banana sobre mesa",
        "etiquetas": ["fruta", "comida"]
    }
]

# ======================
# ENDPOINTS DE IMÁGENES
# ======================
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def capturar_imagen(request):
    """
    [POST] /api/v1/recognition/imagenes/capturar/
    Captura y valida imágenes con autenticación JWT.
    """
    try:
        if 'imagen' not in request.data:
            return respuesta_error(
                codigo="IMAGEN_FALTANTE",
                mensaje="El campo 'imagen' es requerido"
            )

        # Lógica de procesamiento de imagen aquí...
        return Response({
            "estado": "éxito",
            "datos": {
                "id_imagen": f"img_{uuid.uuid4().hex[:8]}",
                "fecha": timezone.now().isoformat()
            }
        })

    except Exception as e:
        return respuesta_error(
            codigo="ERROR_CAPTURA",
            mensaje="Fallo al capturar imagen",
            detalles=str(e) if settings.DEBUG else "",
            codigo_estado=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def obtener_analisis_imagen(request, id_imagen):
    """
    [GET] /api/v1/recognition/imagenes/<id_imagen>/analisis/
    Obtiene el análisis de una imagen específica.
    """
    try:
        if not re.match(r'^img_[a-f0-9]{8}$', id_imagen):
            return respuesta_error(
                codigo="ID_IMAGEN_INVALIDO",
                mensaje="Formato de ID de imagen inválido"
            )

        # Lógica de análisis aquí...
        return Response({
            "estado": "éxito",
            "id_imagen": id_imagen,
            "analisis": {
                "objetos": [
                    {"etiqueta": "persona", "confianza": 0.92}
                ]
            }
        })

    except Exception as e:
        return respuesta_error(
            codigo="ERROR_ANALISIS",
            mensaje="Fallo en el análisis",
            codigo_estado=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

# ======================
# ENDPOINTS DE MULTIMEDIA
# ======================
@api_view(['GET'])
def obtener_multimedia_por_etiqueta(request, etiqueta):
    """
    [GET] /api/v1/recognition/multimedia/por-etiqueta/<etiqueta>/
    Obtiene recursos multimedia filtrados por etiqueta.
    
    Parámetros:
        etiqueta (str): Nombre de etiqueta (solo alfanumérico, max 50 chars)
    
    Respuestas:
        200: Éxito (incluso sin resultados)
        400: Formato de etiqueta inválido
    """
    try:
        # Sanitizar etiqueta (solo alfanumérico y guiones)
        etiqueta_limpia = re.sub(r'[^\w-]', '', etiqueta).lower()[:50]
        if not etiqueta_limpia:
            return respuesta_error(
                codigo="ETIQUETA_INVALIDA",
                mensaje="La etiqueta contiene caracteres inválidos",
                detalles="Solo letras, números, guiones y guiones bajos permitidos"
            )

        # Buscar coincidencias (insensible a mayúsculas)
        resultados = []
        for etiqueta_db, items in MULTIMEDIA_DB.items():
            if etiqueta_limpia in etiqueta_db:
                resultados.extend(items)

        return Response({
            "estado": "éxito",
            "etiqueta": etiqueta_limpia,
            "cantidad": len(resultados),
            "resultados": resultados
        })

    except Exception as e:
        return respuesta_error(
            codigo="ERROR_BUSQUEDA",
            mensaje="Fallo al buscar por etiqueta",
            detalles=str(e) if settings.DEBUG else "",
            codigo_estado=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

# ======================
# ENDPOINTS DE ITEMS
# ======================
@api_view(['GET'])
def obtener_items(request):
    """
    [GET] /api/v1/recognition/items/
    
    Obtiene el listado completo de categorías/ítems reconocibles.
    
    Parámetros opcionales:
        ?busqueda=texto (filtra por nombre)
        ?limite=int (default: 10, max: 50)
    """
    try:
        # 1. Procesar parámetros
        busqueda = request.query_params.get('busqueda', '').lower()
        limite = min(int(request.query_params.get('limite', 10)), 50)
        
        # 2. Filtrar items
        resultados = [
            {**item} for item in ITEMS_DB.values() 
            if busqueda in item['nombre'].lower()
        ]
        
        # 3. Formatear respuesta
        return Response({
            "estado": "éxito",
            "cantidad": len(resultados),
            "resultados": resultados[:limite]
        })
    
    except ValueError:
        return respuesta_error(
            codigo="PARAMETRO_INVALIDO",
            mensaje="Parámetro 'limite' debe ser número"
        )

@api_view(['GET'])
def obtener_detalle_item(request, item_id):
    """
    [GET] /api/v1/recognition/items/<int:item_id>/
    
    Obtiene detalles específicos de un ítem/categoría.
    """
    try:
        item_id = int(item_id)
        if item_id not in ITEMS_DB:
            return respuesta_error(
                codigo="ITEM_NO_ENCONTRADO",
                mensaje="Ítem no encontrado",
                codigo_estado=status.HTTP_404_NOT_FOUND
            )
        
        # Datos extendidos (simular estadísticas)
        respuesta = {
            "estado": "éxito",
            "item": ITEMS_DB[item_id],
            "estadisticas": {
                "usos": 15 * item_id,  # Simular datos
                "precision": 0.9 - (item_id * 0.01)
            }
        }
        
        return Response(respuesta)
    
    except ValueError:
        return respuesta_error(
            codigo="ID_INVALIDO",
            mensaje="ID debe ser numérico"
        )

# ======================
# ENDPOINTS DE HISTORIAL
# ======================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def obtener_historial(request):
    """
    [GET] /api/v1/recognition/historial/
    
    Obtiene el historial de recognitions del usuario.
    Parámetros opcionales:
        ?limite=int (default: 10, max: 50)
        ?desde=YYYY-MM-DD (filtrar por fecha)
    """
    try:
        # Lógica de paginación y filtrado
        limite = min(int(request.query_params.get('limite', 10)), 50)
        desde_fecha = request.query_params.get('desde')
        
        # Filtrar y ordenar
        resultados = [item for item in HISTORIAL_DB 
                     if item['usuario'] == request.user.username and
                     (not desde_fecha or item['fecha'] >= desde_fecha)]
        
        return Response({
            "estado": "éxito",
            "datos": sorted(resultados, key=lambda x: x['fecha'], reverse=True)[:limite]
        })
    
    except ValueError:
        return respuesta_error(
            codigo="PARAMETRO_INVALIDO",
            mensaje="Parámetro 'limite' debe ser número"
        )
    except Exception as e:
        return respuesta_error(
            codigo="ERROR_SERVIDOR",
            mensaje="Error en el servidor",
            detalles=str(e) if settings.DEBUG else "",
            codigo_estado=status.HTTP_500_INTERNAL_SERVER_ERROR
        )