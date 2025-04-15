from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HelloWorldSerializer

class HelloWorldView(APIView):
    def get(self, request):
        serializer = HelloWorldSerializer(data={'mensaje': 'Hola mundo'})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
    
    from django.http import HttpResponse

def home(request):
    return HttpResponse("¡Bienvenido a mi API Django! Visita /api/hello/")