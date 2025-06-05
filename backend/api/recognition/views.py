from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import uuid
import re

# ======================
# Helpers 
# ======================
class SecurityValidationError(Exception):
    """Excepción personalizada para errores de validación"""
    pass

def error_response(codigo, mensaje, detalles="", status_code=status.HTTP_400_BAD_REQUEST):
    """Formato estandarizado para respuestas de error"""
    return Response(
        {
            "estado": "error",
            "error": {
                "codigo": codigo,  # Ej: "IMAGEN_NO_VALIDA"
                "mensaje": mensaje, # Ej: "La imagen proporcionada no es válida"
                "detalles": detalles
            }
        },
        status=status_code
    )

# ======================
# Image Endpoints
# ======================
@api_view(['POST'])
def capture_image(request):
    """
    [POST] /api/v1/images/capture/
    Captura y valida imágenes.
    """
    try:
        if 'image' not in request.data:
            return error_response(
                codigo="IMAGEN_FALTANTE",
                mensaje="El campo 'imagen' es requerido"
            )

        return Response({
            "estado": "éxito",
            "datos": {
                "image_id": f"img_{uuid.uuid4().hex[:8]}",
                "timestamp": timezone.now().isoformat()
            }
        })

    except Exception as e:
        return error_response(
            codigo="ERROR_CAPTURA",
            mensaje="Fallo al capturar la imagen",
            detalles=str(e),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET'])
def get_image_analysis(request, image_id):
    """
    [GET] /api/v1/images/{image_id}/analysis/
    Valida ID y devuelve análisis.
    """
    try:
        if not re.match(r'^img_[a-f0-9]{8}$', image_id):
            return error_response(
                codigo="ID_IMAGEN_INVALIDO",
                mensaje="Formato de ID de imagen inválido"
            )

        return Response({
            "estado": "éxito",
            "image_id": image_id,
            "analisis": {
                "objetos": [
                    {"etiqueta": "persona", "confianza": 0.92}
                ]
            }
        })

    except Exception as e:
        return error_response(
            codigo="ERROR_ANALISIS",
            mensaje="Error en el análisis de la imagen",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

# ======================
# Multimedia Endpoints
# ======================
@api_view(['GET'])
def get_multimedia_by_tag(request, tag):
    """
    [GET] /api/v1/multimedia/by-tag/{tag}/
    Busca multimedia por etiqueta.
    """
    try:
        clean_tag = re.sub(r'[^\w-]', '', tag).lower()[:50]
        if not clean_tag:
            return error_response(
                codigo="ETIQUETA_INVALIDA",
                mensaje="La etiqueta contiene caracteres no permitidos"
            )

        # Lógica de búsqueda simulada
        resultados = []
        for tag_db, items in MULTIMEDIA_DB.items():
            if clean_tag in tag_db:
                resultados.extend(items)

        return Response({
            "estado": "éxito",
            "etiqueta": clean_tag,
            "cantidad": len(resultados),
            "resultados": resultados
        })

    except Exception as e:
        return error_response(
            codigo="ERROR_BUSQUEDA",
            mensaje="Error al buscar multimedia",
            detalles=str(e),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )