from django.apps import AppConfig

class RecognitionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recognition'  # Nombre de la app (debe coincidir con la carpeta)
    label = 'recognition'  # Opcional: etiqueta única