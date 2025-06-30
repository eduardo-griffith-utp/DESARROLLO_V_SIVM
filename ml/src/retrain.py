import os
import numpy as np
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from tensorflow.keras.models import load_model
from data_loading import ImageDatasetLoader

class Retrainer:
    def __init__(self, data_dir, model_path="models/best_model.h5"):
        """
        Args:
            data_dir: Ruta a los datos de reentrenamiento.
            model_path: Ruta al modelo preentrenado (.h5).
        """
        self.data_dir = data_dir
        self.model_path = model_path
        os.makedirs(os.path.dirname(model_path), exist_ok=True)  # Asegura que la carpeta exista

    def load_model(self):
        """Carga el modelo preentrenado con verificación de errores."""
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"¡Archivo {self.model_path} no encontrado!")
        return load_model(self.model_path)

    def retrain(self, epochs=10, batch_size=32, validation_split=0.2):
        """Reentrena el modelo y guarda una nueva versión mejorada."""
        # 1. Cargar datos
        loader = ImageDatasetLoader(self.data_dir)
        X, y = loader.load_data()
        
        # 2. Cargar modelo preentrenado
        model = self.load_model()
        print("Modelo cargado. Resumen:")
        model.summary()

        # 3. Callbacks
        checkpoint = ModelCheckpoint(
            self.model_path,  # sobrescribe solo si mejora
            monitor="val_accuracy",
            save_best_only=True,
            mode="max",
            verbose=1
        )
        early_stop = EarlyStopping(
            monitor="val_loss",
            patience=3,  # Detener si no mejora en 3 épocas
            restore_best_weights=True
        )

        # 4. Reentrenamiento
        print(f"\n Reentrenando por {epochs} épocas...")
        history = model.fit(
            X, y,
            epochs=epochs,
            batch_size=batch_size,
            validation_split=validation_split,
            callbacks=[checkpoint, early_stop]
        )
        
        return history

# --- Uso ---
if __name__ == "__main__":
    retrainer = Retrainer(
        data_dir="data/raw",          # Carpeta con nuevas imágenes
        model_path="models/best_model.h5"  # Modelo a mejorar
    )
    retrainer.retrain(epochs=15)