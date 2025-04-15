Backend del Sistema de Identificación Visual Multimedia (SIVM)
Esta carpeta contiene la API y servicios del servidor para el proyecto SIVM, responsable del procesamiento de solicitudes, lógica de negocio e integración con otros servicios.
Tecnologías Utilizadas
 
- Framework: Django (con Django REST Framework)
- Lenguaje: Python
- Base de Datos: PostgreSQL (sugerido por compatibilidad y escalabilidad con Django)
- Autenticación: JWT (JSON Web Tokens)
- Validación: Serializadores de Django REST Framework
- Documentación API: OpenAPI/Swagger (a través de `drf-yasg` o `django-rest-swagger`)
- Pruebas: Pytest / Django TestCase
 
Configuración del Entorno
Requisitos Previos
 
- Python 3.10 o superior
- vpip
- Git
- PostgreSQL
- Cuenta en Render (https://render.com) para despliegue
 
Instalación
 
# Clonar el repositorio
git clone https://github.com/tu_usuario/sivm-backend.git
cd sivm-backend
 
# Crear entorno virtual
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
 
# Instalar dependencias
pip install -r requirements.txt
 
# Configurar variables de entorno (.env)
cp .env.example .env  # Completa las variables necesarias
 
# Migraciones iniciales
python manage.py migrate
 
# Crear superusuario
python manage.py createsuperuser
 
Ejecución
python manage.py runserver
API Endpoints
Documentación de la API
 
La documentación completa de la API estará disponible en:
 
http://localhost:8000/swagger/  (Desarrollo local)
https://sivm-backend.onrender.com/swagger/ (Producción en Render)
 
Principales Endpoints
Gestión de Imágenes
 
- GET /api/images/ – Listar imágenes
- POST /api/images/ – Subir imagen
- GET /api/images/{id}/ – Obtener detalles de imagen
- DELETE /api/images/{id}/ – Eliminar imagen
 
Categorías y Metadatos
 
- GET /api/categories/ – Listar categorías
- POST /api/categories/ – Crear categoría
- GET /api/categories/{id}/ – Detalle de categoría
 
Integración con Servicios Externos
Servicio de Reconocimiento de Imágenes
 
- POST /api/recognition/ – Enviar imagen para reconocimiento visual
- Integra con un modelo de IA para identificar contenido en la imagen
 
Almacenamiento de Archivos
Las imágenes y archivos multimedia son almacenados usando Media Storage de Django, con opción de escalar a servicios como AWS S3 o Cloudinary.
Convenciones de Código
 
- Código en inglés
- Uso de PEP8 para estilo de Python
- Documentación de funciones con docstrings
- Uso de `black` para formateo automático
 
Seguridad
 
- Autenticación con JWT (sin manejo de sesiones en servidor)
- Protección contra:
  - SQL Injection
  - Cross-Site Scripting (XSS)
  - Cross-Site Request Forgery (CSRF)
- Uso de permisos personalizados en la API
 
Despliegue en la Nube
Plataforma: Render
 
¿Qué es Render?
Es un servicio en la nube que permite desplegar aplicaciones backend, frontend y bases de datos sin configurar servidores manualmente. Soporta tecnologías como Django, Flask, Node.js, Ruby, Go, etc.
 
Ventajas:
- Despliegue automático desde GitHub
- HTTPS incluido
- Escalado automático
- Facilidad de configuración