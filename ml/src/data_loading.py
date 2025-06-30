import os
import numpy as np
from PIL import Image
import json

class ImageDatasetLoader:
    def __init__(self, data_dir, img_size=(224, 224)):
        """
        Args:
            data_dir: Ruta a la carpeta con subcarpetas por clase (ej: 'data/raw').
            img_size: Tamaño de redimensionamiento (alto, ancho).
        """
        self.data_dir = data_dir
        self.img_size = img_size
        self._init_classes()  # Inicializa la estructura de clases

    def _init_classes(self):
        """Inicializa la estructura de mapeo de clases."""
        self.classes = sorted(
            [d for d in os.listdir(self.data_dir) 
             if os.path.isdir(os.path.join(self.data_dir, d))]
        )
        self.class_to_idx = {cls_name: idx for idx, cls_name in enumerate(self.classes)}
        self.idx_to_class = {idx: cls_name for cls_name, idx in self.class_to_idx.items()}

    def load_data(self):
        """Carga imágenes y etiquetas desde subcarpetas.
        
        Returns:
            tuple: (imágenes, etiquetas) donde:
                - imágenes: array numpy de shape (n_samples, height, width, channels)
                - etiquetas: array numpy de shape (n_samples,)
        """
        images, labels = [], []
        
        for class_name, class_idx in self.class_to_idx.items():
            class_dir = os.path.join(self.data_dir, class_name)
            
            for img_file in os.listdir(class_dir):
                if img_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    img_path = os.path.join(class_dir, img_file)
                    try:
                        img = Image.open(img_path).convert('RGB').resize(self.img_size)
                        img_array = (np.array(img) / 127.5) - 1.0  # Normaliza a [0, 1]
                        images.append(img_array)
                        labels.append(class_idx)
                    except Exception as e:
                        print(f"Error al cargar {img_path}: {e}")

        return np.array(images), np.array(labels)

    def get_class_names(self):
        """Devuelve la lista de nombres de clases en el orden correcto.
        
        Returns:
            list: Lista de nombres de clases ordenadas.
        """
        return self.classes

    def save_class_mapping(self, file_path):
        """Guarda el mapeo de clases a un archivo JSON.
        
        Args:
            file_path: Ruta donde guardar el mapeo.
        """
        with open(file_path, 'w') as f:
            json.dump({
                'class_to_idx': self.class_to_idx,
                'idx_to_class': self.idx_to_class,
                'classes': self.classes
            }, f, indent=4)

    @classmethod
    def load_class_mapping(cls, file_path):
        """Carga un mapeo de clases desde archivo.
        
        Args:
            file_path: Ruta al archivo JSON con el mapeo.
            
        Returns:
            dict: Diccionario con la estructura del mapeo.
        """
        with open(file_path, 'r') as f:
            return json.load(f)