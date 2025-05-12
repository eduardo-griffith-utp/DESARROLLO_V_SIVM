
##  Tecnologías Utilizadas

| Componente       | Tecnología                  |
|------------------|-----------------------------|
| Framework        | Django REST Framework       |
| Lenguaje         | Python                      |
| Autenticación    | JWT (JSON WEB TOKENS)       |
| Documentación    | Swagger (drf-yasg)          |

## ⚡ Quick Start

```bash
# Clonar y configurar
git clone https://github.com/eduardo-griffith-utp/DESARROLLO_V_SIVM.git
cd backend/
python -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar .env
cp .env.example .env

# Base de datos
python manage.py migrate
python manage.py runserver
```

## 🏗️ Estructura del Proyecto
```
└── backend
    └── api
        └── api_project
            └── __init__.py
            └── __pycache__
                └── __init__.cpython-311.pyc
                └── settings.cpython-311.pyc
                └── urls.cpython-311.pyc
            └── asgi.py
            └── settings.py
            └── urls.py
            └── wsgi.py
        └── core
            └── __init__.py
            └── __pycache__
                └── apps.cpython-311.pyc
                └── models.cpython-311.pyc
                └── serializers.cpython-311.pyc
                └── views.cpython-311.pyc
            └── .gitignore
            └── admin.py
            └── apps.py
            └── migrations
                └── __init__.py
                └── __pycache__
                    └── __init__.cpython-311.pyc
                    └── 0001_initial.cpython-311.pyc
                └── 0001_initial.py
            └── models.py
            └── permissions.py
            └── requirements.txt
            └── serializers.py
            └── tests
                └── __init__.py
                └── test_models.py
                └── test_views.py
            └── urls.py
            └── views.py
        └── db.sqlite3
        └── items
            └── __init__.py
            └── admin.py
            └── apps.py
            └── migrations
            └── models.py
            └── serializers.py
            └── tests
            └── urls.py
            └── views.py
        └── manage.py
        └── media
            └── uploads
                └── items
        └── recognition
            └── __init__.py
            └── admin.py
            └── apps.py
            └── migrations
            └── models.py
            └── serializers.py
            └── services
                └── __init__.py
                └── recognition_services.py
            └── tests
            └── urls.py
            └── views.py
        └── requirements.txt
        └── static
        └── utils
            └── __init__.py
            └── constans.py
            └── helpers.py
    └── README.md
```

## 📡 Endpoints Principales

```POST /api/auth/login/
Content-Type: application/json
{"username": "user", "password": "pass"}
```

### Autenticación
```http
POST /api/auth/login/
Content-Type: application/json
{"username": "user", "password": "pass"}
```

### Imágenes
| Método | Ruta               | Descripción           |
|--------|--------------------|-----------------------|
| POST   | `/api/images/`     | Subir imagen         |
| GET    | `/api/images/{id}/`| Detalles de imagen   |

## 🛠️ Crear Nueva Función

1. Generar app:
```bash
python manage.py startapp nueva_funcion

## 🧪 Pruebas con Postman
```
## 📤 Autenticación
Obtener token:

POST http://127.0.0.1:8000/api/token/
Content-Type: application/json

{
  "username": "tu_usuario",
  "password": "tu_contraseña"
}
Usar token:

En los headers de las peticiones protegidas, agrega:

Authorization: Bearer TU_ACCESS_TOKEN
## 📸 Endpoint: Captura de Imagen

POST http://127.0.0.1:8000/api/v1/reconocimiento/imagenes/capturar/
Authorization: Bearer <token>
# Respuesta esperada:

{
  "estado": "éxito",
  "datos": {
    "id_imagen": "img_xxxx",
    "fecha": "2025-05-12T..."
  }
}
## 🔍 Endpoint: Análisis de Imagen

GET http://127.0.0.1:8000/api/v1/reconocimiento/imagenes/<id_imagen>/analisis/
Authorization: Bearer <token>
Devuelve análisis de la imagen capturada.

## 🎥 Endpoint: Multimedia por Etiqueta

GET http://127.0.0.1:8000/api/v1/reconocimiento/multimedia/por-etiqueta/<etiqueta>/
Ejemplo:

GET /api/v1/reconocimiento/multimedia/por-etiqueta/tecnologia/
No requiere autenticación

# Respuesta esperada:

{
  "estado": "éxito",
  "etiqueta": "tecnologia",
  "cantidad": 2,
  "resultados": [
    {
      "id": 1,
      "nombre": "foto_tecnologia.jpg",
      "url": "/media/items/foto_tecnologia.jpg"
    }
  ]
}
## 🧾 Endpoint: Listado de Items

GET http://127.0.0.1:8000/api/v1/items/
Authorization: Bearer <token>
# Respuesta esperada:

{
  "estado": "éxito",
  "cantidad": 3,
  "resultados": [
    {
      "id": 1,
      "nombre": "Fruta",
      "descripcion": "Frutas comestibles",
      "ejemplos": ["manzana", "banana", "naranja"],
      "tags_relacionados": ["comida", "saludable"],
      "fecha_creacion": "2025-01-10"
    },
    {
      "id": 2,
      "nombre": "Electrónica",
      "descripcion": "Dispositivos electrónicos",
      "ejemplos": ["televisor", "celular", "laptop"],
      "tags_relacionados": ["tecnología", "gadgets"],
      "fecha_creacion": "2025-01-15"
    },
    {
      "id": 3,
      "nombre": "Vehículos",
      "descripcion": "Medios de transporte",
      "ejemplos": ["automóvil", "motocicleta", "bicicleta"],
      "tags_relacionados": ["transporte", "movilidad"],
      "fecha_creacion": "2025-02-01"
    }
  ]
}
## 🕓 Endpoint: Historial de Imágenes

GET http://127.0.0.1:8000/api/v1/reconocimiento/imagenes/historial/
Authorization: Bearer <token>
# Respuesta esperada (vacía):

{
  "estado": "éxito",
  "datos": []
}
```
```

2. Modelo básico:
```python
# models.py
from django.db import models
class Example(models.Model):
 name = models.CharField(max_length=100)
 description = models.TextField(blank=True, null=True)
 created_at = models.DateTimeField(auto_now_add=True)

 def __str__(self):
    return self.name
```

## 🔒 Seguridad
- Autenticación JWT
- Rate limiting (100 req/hora)
- CORS restringido

## 🌐 Despliegue en Render
1. Conectar repositorio GitHub
2. Configurar variables:
```plaintext
DATABASE_URL=postgres://user:pass@host:5432/db
SECRET_KEY=tu-clave-secreta
```

## 👥 Equipo
- **Alexander Moreno**
- **Miguel Vallejo**
- **Jonathan Cabrera**
- **Carlos Rivas**
- **Oscar Villaverde**
