import os
from pathlib import Path

# 1. Configuración de rutas base
BASE_DIR = Path(__file__).resolve().parent.parent  # Ajusta según tu estructura

# 2. Seguridad (¡CAMBIAR EN PRODUCCIÓN!)
SECRET_KEY = 'tu-clave-secreta-aqui'  # Genera una nueva con: django.core.management.utils.get_random_secret_key()

# 3. Modo debug (cambiar a False en producción)
DEBUG = True

# 4. Hosts permitidos (para desarrollo usa '*')
ALLOWED_HOSTS = ['*']  # En producción especifica dominios reales

# 5. Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',          # Para Django REST Framework
    'core',                   # Tu app personalizada
]

# 6. Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 7. Configuración de URLs
ROOT_URLCONF = 'api_project.urls'

# 8. Configuración de templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 9. Configuración de base de datos (SQLite por defecto)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 10. Configuración de autenticación
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 11. Internacionalización
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 12. Archivos estáticos
STATIC_URL = 'static/'

# 13. Configuración DRF (Django REST Framework)
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',  # Para desarrollo
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ]
}

# Configuración para JWT (opcional)
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
}