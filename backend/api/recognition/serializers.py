from rest_framework import serializers
from .models import Example
class CapturedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapturedImage
        fields = ['id', 'image', 'created_at']

    def validate_image(self, img):
        if img.size > 5*1024*1024:
            raise ValidationError("La imagen no puede superar 5 MB")
        if img.image.width < 100 or img.image.height < 100:
            raise ValidationError("Resolución mínima 100×100 píxeles")
        return img