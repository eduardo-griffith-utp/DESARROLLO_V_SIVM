import os
import numpy as np
from tensorflow.keras.callbacks import ModelCheckpoint
from data_loading import ImageDatasetLoader
from model import CNNModel
import json
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
import collections

class Trainer:
    def __init__(self, data_dir="data/raw", model_dir="models"):
        """
        Args:
            data_dir: Ruta a los datos de entrenamiento (opcional).
            model_dir: Carpeta para guardar modelos (opcional).
            """
        self.data_dir = data_dir
        self.model_dir = model_dir
        os.makedirs(model_dir, exist_ok=True)  # Crea carpeta si no existe

    def train(self, epochs=10, batch_size=32):
        """Entrena el modelo y guarda checkpoints."""
        try:
            # 1. Carga de datos
            logger.info("Cargando datos...")
            loader = ImageDatasetLoader(self.data_dir)
            X, y = loader.load_data()
            
            # 2. Guardar class_mapping.json PRIMERO
            class_mapping_path = os.path.join(self.model_dir, 'class_mapping.json')
            logger.info(f"Guardando mapeo de clases en {class_mapping_path}")
            loader.save_class_mapping(class_mapping_path)
            
            # ificar que se creó
            if not os.path.exists(class_mapping_path):
                raise RuntimeError("No se generó class_mapping.json")
        
            # Construye modelo
            cnn_model = CNNModel(
                input_shape=X[0].shape,
                num_classes=len(loader.classes),
                class_names=loader.classes
            )
            model = cnn_model.build_model()

            # Callback para guardar el mejor modelo
            checkpoint_path = os.path.join(self.model_dir, "best_model.h5")
            checkpoint = ModelCheckpoint(
                checkpoint_path,
                monitor='val_accuracy',
                save_best_only=True,
                mode='max',
                save_format='h5'
            )
            print("Distribución de clases:", collections.Counter(y))
            # Entrenamiento
            history = model.fit(
                X, y,
                epochs=epochs,
                batch_size=batch_size,
                validation_split=0.2,
                callbacks=[checkpoint]
            )
            class_names = loader.classes
            
            # Guardar las clases
            CNNModel.save_model(model, checkpoint_path, class_names)
        
            return history, class_names
        except Exception as e:
            logger.error(f"Error durante el entrenamiento: {str(e)}")
            raise
"""    
if __name__ == "__main__":
    # Ejemplo de uso con parámetros personalizables
    trainer = Trainer(
        data_dir="data/raw",  
        model_dir="models"    
    )
    history, class_names = trainer.train(
        epochs=10,            
        batch_size=32         
    )
    print("Clases aprendidas:", class_names)
"""
if __name__ == "__main__":
    # Ejemplo de uso
    trainer = Trainer(data_dir="data/raw")
    history, class_names = trainer.train(epochs=22)
    print("Clases aprendidas:", class_names)