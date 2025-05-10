from django.contrib import admin
from django.urls import path
from core.views import HelloWorldView
from core.views import home  # Importa la nueva vista

urlpatterns = [
    path('', home),  # Ruta raiz
    path('admin/', admin.site.urls),
    path('api/hello/', HelloWorldView.as_view()),
]