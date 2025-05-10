import cv2
import numpy as np

class ImageProcessor:
    def __init__(self, target_size=(224, 224), normalize=True):
        """
        Inicializa el procesador de imágenes.

        Args:
        target_size (tuple): Tamaño objetivo para redimensionar la imagen.
        normalize (bool): Si es True, normaliza los valores de píxeles.
        """
        self.target_size = target_size
        self.normalize = normalize

    def load_image(self, image_path):
        """
        Carga una imagen desde la ruta especificada.

        Args:
        image_path (str): Ruta a la imagen.

        Returns:
        numpy.ndarray: Imagen cargada en formato BGR.
        """
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"No se pudo cargar la imagen: {image_path}")
        return image
