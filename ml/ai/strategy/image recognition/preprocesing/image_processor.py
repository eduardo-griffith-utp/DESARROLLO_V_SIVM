import cv2 
import numpy as np 

 class ImageProcessor: 
"""Clase para el preprocesamiento de imágenes antes del reconocim
 def __init__(self, target_size=(224, 224), normalize=True): 
""" 
        Inicializa el procesador de imágenes. 
        Args: 
            target_size (tuple): Tamaño objetivo para redimensionar l
            normalize (bool): Si es True, normaliza los valores de pí
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
raise ValueError(f"No se pudo cargar la imagen: {image_pa
 return image 
Page 3 of 11
def preprocess(self, image): 
""" 
        Preprocesa una imagen para el reconocimiento. 
        Args: 
            image (numpy.ndarray): Imagen de entrada en formato BGR. 
        Returns: 
            numpy.ndarray: Imagen preprocesada. 
        """ 
# Convertir a RGB (OpenCV carga en BGR) 
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
# Redimensionar 
        resized = cv2.resize(image_rgb, self.target_size) 
# Normalizar si es necesario 
if self.normalize: 
            resized = resized / 255.0 
return resized 
def process_for_model(self, image_path): 
""" 
        Carga y preprocesa una imagen para enviarla al modelo. 
        Args: 
            image_path (str): Ruta a la imagen. 
        Returns: 
            tuple: (imagen original, imagen preprocesada) 
        """ 
        original = self.load_image(image_path) 
        processed = self.preprocess(original) 
# Expandir dimensiones para el modelo (batch de 1) 
        model_input = np.expand_dims(processed, axis=0)
 return original, model_input