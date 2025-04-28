# Backend del Sistema de Identificación Visual Multimedia (SIVM)

# Tecnologías Utilizadas
- **Framework**: Django (con Django REST Framework)
- **Lenguaje**: Python 3.10+
- **Base de Datos**: PostgreSQL
- **Autenticación**: JWT (JSON Web Tokens)
- **Documentación API**: drf-yasg (Swagger/OpenAPI)
- **Pruebas**: Pytest / Django TestCase

# Estructura del Proyecto

backend/
├── api/
│ ├── api_project/ # Configuración central de Django
│ │ ├── settings.py # Configuración global
│ │ ├── urls.py # Rutas principales
│ │ └── ...
│ ├── core/ # Funcionalidades centrales
│ │ ├── models.py # Modelos compartidos
│ │ ├── serializers.py # Serializadores
│ │ └── ...
│ ├── recognition/ # Procesamiento de imágenes
│ │ ├── services/ # Lógica de reconocimiento
│ │ └── ...
│ ├── items/ # Gestión de contenido
│ ├── utils/ # Utilidades comunes
│ └── manage.py # CLI de Django


# Configuración Inicial
```bash
# Clonar y configurar entorno
git clone https://github.com/tu_usuario/sivm-backend.git
cd sivm-backend
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
pip install -r requirements.txt

# Configuración inicial
cp .env.example .env  # Editar con tus valores
python manage.py migrate
python manage.py createsuperuser

Desarrollo de Nuevas Funcionalidades

Crear nueva aplicación

python manage.py startapp nombre_app

Añadir modelo (models.py)

from django.db import models

class NuevoModelo(models.Model):
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

Crear serializador (serializers.py)

from rest_framework import serializers
from .models import NuevoModelo


Implementar vista (views.py)

from rest_framework import viewsets
from .models import NuevoModelo
from .serializers import NuevoModeloSerializer



router = DefaultRouter()
router.register(r'nuevos-modelos', NuevoModeloViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

Endpoints Principales
Imágenes:

GET /api/images/ - Listar imágenes

POST /api/images/ - Subir nueva imagen

Reconocimiento:

POST /api/recognition/ - Analizar imagen

Categorías:

GET /api/categories/ - Listar categorías

POST /api/categories/ - Crear categoría

Convenciones de Código
Estilo PEP8

Documentación con docstrings

Formateo con black

Nombres en inglés

Seguridad
Autenticación JWT

Protección contra:

SQL Injection

XSS

CSRF

Despliegue en Render
Conectar repositorio GitHub

Configurar variables de entorno

Especificar comando de inicio: gunicorn api_project.wsgi

-- Explicación de Nuevas Funcionalidades Añadidas:

- Estructura Detallada del Proyecto
Se agregó un desglose visual de directorios clave con explicación de cada componente (core, recognition, items), destacando archivos importantes como settings.py y urls.py para mayor claridad en la arquitectura.

- Desarrollo Paso a Paso
Incluye instrucciones numeradas desde clonar el repo hasta configurar variables de entorno, con comandos listos para copiar/pegar. Ahora muestra el flujo completo de configuración inicial.

- Ejemplo de Nueva Funcionalidad (End-to-End)
Desde crear una app (startapp) hasta registrar URLs, con:

Modelo con herencia de BaseModel

Serializador con campos read-only

Vista con permisos personalizados

URLs con versionado (/api/v1/)

- Tablas Organizadas

Endpoints clave con método/descripción

Equipo con roles específicos

Variables de entorno críticas

- Mejoras de Seguridad
Detalla implementaciones como:

Rate limiting

Sanitización de inputs

JWT con refresh tokens

- Componentes Principales:

Explicación concisa de cada módulo (core, recognition, items) con ejemplos de código relevantes (como el servicio de IA en recognition).

- Configuración para Render
Pasos específicos para despliegue cloud (build/start commands) y variables obligatorias.

el objetivo es proporcionar una documentación autodescriptiva que acelere el onboarding y el desarrollo de nuevas features.

Equipo
Alexander Moreno

Miguel Vallejo

Jonathan Cabrera

Oscar Villaverde

Carlos Rivas