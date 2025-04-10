from django.db import models

class DummyModel(models.Model):
    # Modelo temporal solo para generar migraciones
    name = models.CharField(max_length=100)
    
    class Meta:
        app_label = 'core'