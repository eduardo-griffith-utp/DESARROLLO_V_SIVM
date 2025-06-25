from django.db import models
from django.contrib.auth import get_user_model # Mejor usar get_user_model() para mayor flexibilidad

User = get_user_model() # Obtiene el modelo de usuario activo (Django's default o custom)

class Example(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ImagenReconocida(models.Model):
    # Hacemos el campo 'usuario' opcional (nullable) para permitir cargas de usuarios no autenticados.
    # Cuando el usuario asociado se elimina, el campo 'usuario' de esta instancia se establece en NULL.
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    # El campo 'imagen' ya está bien configurado para ser opcional.
    imagen = models.ImageField(upload_to='image/', null=True, blank=True)
    
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Mejora la representación de cadena para manejar el caso de usuario nulo
        user_display = self.usuario.username if self.usuario else 'Anónimo'
        image_name_display = self.imagen.name if self.imagen else 'Sin imagen'
        return f"Imagen de {user_display} - {image_name_display} ({self.fecha_subida.strftime('%Y-%m-%d %H:%M')})"

