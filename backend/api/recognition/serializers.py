import base64
import six # Utilizado para compatibilidad Python 2/3, aunque en Python 3 puro six es menos común
import uuid

from django.core.files.base import ContentFile
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import ImagenReconocida # Asegúrate de que esta importación sea correcta

# ==============================================================================
# Campo personalizado para manejar imágenes Base64
# ==============================================================================
class Base64ImageField(serializers.ImageField):
    """
    A Django REST Framework field that handles base64 encoded image uploads.
    It expects a Base64 string (optionally with the "data:image/jpeg;base64," prefix).
    """
    def to_internal_value(self, data):
        # Check if the data is already a file (e.g., not Base64, but a normal FileField)
        if isinstance(data, (str, six.text_type)):
            # Allow the prefix 'data:image/png;base64,' or 'data:image/jpeg;base64,' etc.
            if 'data:' in data and ';base64,' in data:
                header, base64_data = data.split(';base64,')
            else:
                base64_data = data

            try:
                decoded_file = base64.b64decode(base64_data)
            except TypeError:
                # Catch invalid Base64 strings
                raise ValidationError("Invalid Base64 image string.")
            except Exception as e:
                # Catch other decoding errors
                raise ValidationError(f"Error decoding Base64 image: {e}")

            # Determine file name and MIME type (optionally from the header)
            file_name = str(uuid.uuid4()) # Generate a unique file name
            file_extension = 'jpg' # Default extension

            if 'data:' in data and ';base64,' in data:
                # Try to extract the extension from the MIME type
                try:
                    mime_type = header.split(':')[1]
                    if 'jpeg' in mime_type or 'jpg' in mime_type:
                        file_extension = 'jpg'
                    elif 'png' in mime_type:
                        file_extension = 'png'
                    elif 'gif' in mime_type:
                        file_extension = 'gif'
                    elif 'webp' in mime_type:
                        file_extension = 'webp'
                    # Add more types if needed
                except IndexError:
                    pass # If header parsing fails, use the default 'jpg'

            complete_file_name = f"{file_name}.{file_extension}"
            
            # Create a ContentFile object that Django can use
            data = ContentFile(decoded_file, name=complete_file_name)

        # Call the original ImageField's to_internal_value for further validation
        # (e.g., ensuring it's a valid image format, not just a file)
        return super().to_internal_value(data)

# ==============================================================================
# Serializer for ImagenReconocida
# ==============================================================================
class CapturedImageSerializer(serializers.ModelSerializer):
    # Use our custom Base64ImageField for the 'imagen' field
    # use_url=True ensures that the full URL is displayed in the output
    imagen = Base64ImageField(use_url=True) 

    class Meta:
        model = ImagenReconocida
        fields = ['id', 'imagen', 'fecha_subida', 'usuario']

    # The 'validate_imagen' method of the serializer remains valid
    # because Base64ImageField returns a ContentFile, which the underlying
    # ImageField in the super() call can handle.
    def validate_imagen(self, img):
        # Size validation: 5 MB
        if img.size > 5 * 1024 * 1024:
            raise ValidationError("La imagen no puede superar 5 MB.")
        
        # Minimum resolution validation: 100x100 pixels
        # The 'image' attribute is attached to the ContentFile by the underlying
        # ImageField (from super().to_internal_value) after it processes it.
        if hasattr(img, 'image') and (img.image.width < 100 or img.image.height < 100):
            raise ValidationError("La resolución mínima de la imagen es 100x100 píxeles.")
        
        return img
