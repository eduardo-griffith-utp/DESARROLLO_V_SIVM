from rest_framework import serializers
from rest_framework.exceptions import ValidationError 
from .models import ImagenReconocida 

class CapturedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenReconocida
        fields = ['id', 'imagen', 'fecha_subida', 'usuario']

    def validate_imagen(self, img):
        # Validación de tamaño: 5 MB
        if img.size > 5 * 1024 * 1024:
            raise ValidationError("La imagen no puede superar 5 MB.")

        # Validación de resolución mínima: 100x100 píxeles
        # 'hasattr(img, 'image')' verifica si el objeto 'img' tiene el atributo 'image' (propio de ImageField)
        if hasattr(img, 'image') and (img.image.width < 100 or img.image.height < 100):
            raise ValidationError("La resolución mínima de la imagen es 100x100 píxeles.")

        return img