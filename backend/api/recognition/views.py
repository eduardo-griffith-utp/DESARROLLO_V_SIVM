from rest_framework import status, viewsets
from rest_framework.decorators import api_view, parser_classes, action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .serializers import CapturedImageSerializer
from .models import CapturedImage

# Opción 1: API function-based con parsers
@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def capture_image(request):
    serializer = CapturedImageSerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        return Response({
            "status": "success",
            "data": {
                "image_id": instance.id,
                "timestamp": instance.created_at.isoformat(),
                "image_url": request.build_absolute_uri(instance.image.url)
            },
            "message": "Imagen guardada correctamente"
        }, status=status.HTTP_201_CREATED)

    return Response({
        "status": "error",
        "errors": serializer.errors,
        "message": "Error al procesar la imagen"
    }, status=status.HTTP_400_BAD_REQUEST)


class CapturedImageViewSet(viewsets.ViewSet):
    parser_classes = [MultiPartParser, FormParser]

    @action(detail=False, methods=['post'])
    def capture(self, request):
        return capture_image(request)