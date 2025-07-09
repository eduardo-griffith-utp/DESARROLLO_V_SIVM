from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated # Se mantiene el import por si se usa en otro lugar, aunque no se usará en estas vistas
from rest_framework.response import Response
from rest_framework import status
# IMPORTANTE: Cambiamos MultiPartParser y FormParser a JSONParser
from rest_framework.parsers import JSONParser 
from ml.src.predict_b64 import predict_imagen_api

from django.utils import timezone
import uuid
import re
import os
from django.conf import settings # Ensure settings is configured correctly
from django.forms import ValidationError as DjangoValidationError

# Import your model and serializer
from .models import ImagenReconocida # Assuming this model name is retained
from .serializers import CapturedImageSerializer # Ensure the path is correct

# ======================
# CLASSES AND HELPERS
# ======================
class SecurityValidationError(Exception):
    """Custom exception for validation errors"""
    def __init__(self, code, message, details=""):
        self.code = code
        self.message = message
        self.details = details

def error_response(code, message, details="", status_code=status.HTTP_400_BAD_REQUEST):
    """Standardized format for error responses"""
    return Response(
        {
            "status": "error",
            "error": {
                "code": code,
                "message": message,
                "details": details
            }
        },
        status=status_code
    )

# ======================
# DUMMY DATA (SIMULATES DB)
# These data structures are here to simulate a database.
# ======================
ITEMS_DB = {
    1: { "id": 1, "name": "Fruit", "description": "Edible fruits", "examples": ["apple", "banana", "orange"], "related_tags": ["food", "healthy"], "creation_date": "2025-01-10" },
    2: { "id": 2, "name": "Electronics", "description": "Electronic devices", "examples": ["television", "cellphone", "laptop"], "related_tags": ["technology", "gadgets"], "creation_date": "2025-01-15" },
    3: { "id": 3, "name": "Vehicles", "description": "Means of transportation", "examples": ["car", "motorcycle", "bicycle"], "related_tags": ["transportation", "mobility"], "creation_date": "2025-02-01" },
    4: { "id": 4, "name": "Food", "description": "Edible product", "examples": ["hamburger", "hot dog", "chicken"], "related_tags": ["combo", "buffet"], "creation_date": "2025-02-01" }
}

MULTIMEDIA_DB = {
    'nature': [ { "id": "mult_001", "type": "image", "url": "/media/nature/forest.jpg", "tags": ["nature", "forest"] } ],
    'Material': [ { "id": "mult_001", "type": "image", "url": "/media/material/iron.jpg", "tags": ["material", "iron"] } ],
    'technology': [ { "id": "mult_002", "type": "video", "url": "/media/technology/ai.mp4", "tags": ["tech", "ai"] } ]
}

HISTORY_DB = [
    { "id": "hist_001", "image_id": "img_001", "user": "default_user", "date": "2025-04-16T10:15:00Z", "description": "Banana on table", "tags": ["fruit", "food"] }
]

# ======================
# IMAGE ENDPOINTS
# ======================
@api_view(['POST'])
@permission_classes([]) # Explícitamente pública
# CAMBIO CLAVE: Usar JSONParser para aceptar cuerpos JSON
@parser_classes([JSONParser]) 
def capture_images(request):
    """
    [POST] /api/v1/recognition/images/capture/
    Captures and validates MULTIPLE images received as Base64 strings in a JSON body. No authentication required.
    """
    # INICIALIZACIÓN DE current_user antes del try
    current_user = request.user 
    
    try:
        # CAMBIO CLAVE: Obtener las imágenes Base64 del cuerpo JSON (request.data)
        # Esperamos una lista de cadenas Base64 bajo la clave 'images'
        base64_images = request.data.get('images', [])

        if not base64_images:
            return error_response(
                code="MISSING_IMAGE_DATA",
                message="The 'images' field (list of Base64 strings) is required in the JSON body.",
                status_code=status.HTTP_400_BAD_REQUEST
            )
        ## cambio de nombre del arreglo
        resultado = []
        errors = []

        # Iterar sobre cada cadena Base64 recibida
        for base64_image_string in base64_images:
            ''' 
            9/7/25 adicion del metodo importado para predecir con el modelo generado con tensorflow, A.S.
            '''
            prediccion = predict_imagen_api(base64_image_string)
            resultado.append({
                "prediction": prediccion,
                "status": "success"
            })
    except Exception as e:
           errors.apend({
               "image_prefix": base64_image_string[:50],
               "error": str(e)
           })

           return Response({
               "resultado": resultado,
               "error":errors
           },status=status.HTTP_200_OK)
    
    except Exception as e:
           return Response({
               "errro": str(e)
           },status=status.HTTP_500_INTERNAL_SERVER_ERROR
           )
           ''' serializer_data = {'imagen': base64_image_string} 
            
            serializer = CapturedImageSerializer(data=serializer_data, context={'request': request})
            
            if serializer.is_valid():
                # Guardamos la imagen. Si 'current_user' es AnonymousUser,
                # y el campo 'usuario' del modelo es null=True (como lo corregimos en models.py),
                # se guardará como NULL en la DB.
                obj = serializer.save(usuario=current_user if current_user.is_authenticated else None)
                uploaded_objects_data.append(serializer.data)
            else:
                # Capturar errores de validación para cada imagen.
                # Mostrar un fragmento de la cadena Base64 para ayudar en la depuración.
                errors.append({
                    "original_data_prefix": (base64_image_string[:50] + "...") if len(base64_image_string) > 50 else base64_image_string,
                    "errors": serializer.errors
                })

        if uploaded_objects_data:
            response_data = {
                "status": "success",
                "data": uploaded_objects_data
            }
            if errors:
                response_data["warnings"] = errors
                response_data["message"] = "Some images were uploaded, but others had validation errors."
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                response_data["message"] = "All images were uploaded and processed successfully."
                return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            # Si no se subió ninguna imagen exitosamente (solo hubo errores de validación para todas)
            return error_response(
                code="IMAGE_VALIDATION_ERROR",
                message="None of the provided images could be processed due to validation errors.",
                details=errors,
                status_code=status.HTTP_400_BAD_REQUEST
            )

    except Exception as e:
        # Asegúrate de que current_user siempre esté definido antes de usarlo en detalles.
        # En este punto, 'current_user' ya está definido fuera del try, por lo que no debería haber NameError.
        return error_response(
            code="GENERAL_CAPTURE_ERROR",
            message="An unexpected error occurred while processing the images",
            details=str(e) if settings.DEBUG else "",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        '''
@api_view(['GET'])
@permission_classes([]) # Explícitamente pública
def get_image_analysis(request, image_id):
    """
    [GET] /api/v1/recognition/images/<image_id>/analysis/
    Gets the analysis of a specific image. No authentication required.
    """
    try:
        if not re.match(r'^img_[a-f0-9]{8}$', image_id):
            return error_response(
                code="INVALID_IMAGE_ID",
                message="Invalid image ID format.",
                status_code=status.HTTP_400_BAD_REQUEST
            )
        return Response({
            "status": "success", "image_id": image_id, "analysis": {
                "objects": [{"label": "person", "confidence": 0.92}, {"label": "car", "confidence": 0.85}],
                "generated_description": "A person next to a car in an urban setting."
            }
        })
    except Exception as e:
        return error_response(code="ANALYSIS_ERROR", message="Failed to analyze the image", details=str(e) if settings.DEBUG else "", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ======================
# MULTIMEDIA ENDPOINTS
# ======================
@api_view(['GET'])
@permission_classes([]) # Explícitamente pública
def get_multimedia_by_tag(request, tag):
    """
    [GET] /api/v1/recognition/multimedia/by-tag/<tag>/
    Gets multimedia resources filtered by tag. No authentication required.
    """
    try:
        clean_tag = re.sub(r'[^\w-]', '', tag).lower()[:50]
        if not clean_tag:
            return error_response(code="INVALID_TAG", message="The tag contains invalid characters or is empty.", details="Only letters, numbers, hyphens, and underscores are allowed", status_code=status.HTTP_400_BAD_REQUEST)
        results = []
        for db_tag, items in MULTIMEDIA_DB.items():
            if clean_tag in db_tag: results.extend(items)
        return Response({"status": "success", "searched_tag": clean_tag, "count": len(results), "results": results})
    except Exception as e:
        return error_response(code="MULTIMEDIA_SEARCH_ERROR", message="Failed to search multimedia resources by tag", details=str(e) if settings.DEBUG else "", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# ======================
# ITEMS ENDPOINTS
# ======================
@api_view(['GET'])
@permission_classes([]) # Explícitamente pública
def get_items(request):
    """
    [GET] /api/v1/recognition/items/
    Gets the complete list of recognizable categories/items. No authentication required.
    """
    try:
        search_query = request.query_params.get('search', '').lower()
        limit_str = request.query_params.get('limit', '10')
        if not limit_str.isdigit():
            return error_response(code="INVALID_PARAMETER", message="The 'limit' parameter must be an integer.", status_code=status.HTTP_400_BAD_REQUEST)
        limit = min(int(limit_str), 50)
        results = [ {**item} for item in ITEMS_DB.values() if search_query in item['name'].lower() ]
        return Response({"status": "success", "total_count": len(results), "results": results[:limit]})
    except Exception as e:
        return error_response(code="GET_ITEMS_ERROR", message="Failed to retrieve the list of items", details=str(e) if settings.DEBUG else "", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([]) # Explícitamente pública
def get_item_detail(request, item_id):
    """
    [GET] /api/v1/recognition/items/<int:item_id>/
    Gets specific details of an item/category. No authentication required.
    """
    try:
        if not str(item_id).isdigit():
             return error_response(code="INVALID_ITEM_ID", message="The item ID must be a number.", status_code=status.HTTP_400_BAD_REQUEST)
        item_id = int(item_id)
        if item_id not in ITEMS_DB:
            return error_response(code="ITEM_NOT_FOUND", message="Item not found in the database.", status_code=status.HTTP_404_NOT_FOUND)
        response_data = {
            "status": "success", "item": ITEMS_DB[item_id], "statistics": {
                "usages": 15 * item_id, "accuracy": max(0.01, 0.9 - (item_id * 0.01))
            }
        }
        return Response(response_data)
    except Exception as e:
        return error_response(code="GET_ITEM_DETAIL_ERROR", message="Failed to retrieve item details", details=str(e) if settings.DEBUG else "", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([]) # Explícitamente pública
def get_history(request):
    """
    [GET] /api/v1/recognition/history/
    Gets the user's recognition history. Accessible without authentication.
    If authenticated, filters by user. If anonymous, shows global history (or empty).
    Optional Parameters:
        ?limit=int (default: 10, max: 50)
        ?from_date=YYYY-MM-DD (filter by date)
    """
    try:
        limit_str = request.query_params.get('limit', '10')
        if not limit_str.isdigit():
            return error_response(code="INVALID_PARAMETER", message="The 'limit' parameter must be an integer.", status_code=status.HTTP_400_BAD_REQUEST)
        limit = min(int(limit_str), 50)
        from_date_str = request.query_params.get('from_date')
        from_date = None
        if from_date_str:
            try:
                from_date = timezone.datetime.strptime(from_date_str, '%Y-%m-%d').isoformat() + 'Z'
            except ValueError:
                return error_response(code="INVALID_DATE_FORMAT", message="The 'from_date' format must beンダー-MM-DD.", status_code=status.HTTP_400_BAD_REQUEST)
        
        if request.user.is_authenticated:
            current_username = request.user.username
            results = [item for item in HISTORY_DB if item['user'] == current_username and (not from_date or item['date'] >= from_date)]
        else:
            results = [item for item in HISTORY_DB if (not from_date or item['date'] >= from_date)]
        
        sorted_history = sorted(results, key=lambda x: x['date'], reverse=True)[:limit]
        return Response({"status": "success", "count": len(sorted_history), "data": sorted_history})
    except Exception as e:
        return error_response(code="GET_HISTORY_ERROR", message="Failed to retrieve recognition history", details=str(e) if settings.DEBUG else "", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

