import os
import tensorflow as tf

class BaseModel:
    """Clase base para modelos de reconocimiento de imágenes."""

    def __init__(self, model_path=None):
        """
        Inicializa el modelo base.

        Args:
        model_path (str, optional): Ruta al modelo preentrenado.
        """
        self.model = None
        self.model_path = model_path

    def build(self):
        """
        Construye la arquitectura del modelo.
        Debe ser implementado por las clases hijas.
        """
        raise NotImplementedError("Las clases hijas deben implementar este método.")

    def load_weights(self, weights_path):
        """
        Carga pesos desde un archivo.

        Args:
        weights_path (str): Ruta al archivo de pesos.
        """
        if self.model is None:
            raise ValueError("El modelo debe ser construido antes de cargar los pesos.")

        if not os.path.exists(weights_path):
            raise FileNotFoundError(f"No se encontró el archivo de pesos: {weights_path}")

        self.model.load_weights(weights_path)
        print(f"Pesos cargados desde: {weights_path}")

    def save_weights(self, weights_path):
        """
        Guarda los pesos del modelo en un archivo.

        Args:
        weights_path (str): Ruta donde guardar los pesos.
        """
        if self.model is None:
            raise ValueError("No hay un modelo para guardar.")

        os.makedirs(os.path.dirname(weights_path), exist_ok=True)
        self.model.save_weights(weights_path)
        print(f"Pesos guardados en: {weights_path}")

    def predict(self, input_data):
        """
        Realiza una predicción con el modelo.

        Args:
        input_data (numpy.ndarray): Datos de entrada para el modelo.

        Returns:
        numpy.ndarray: Predicciones del modelo.
        """
        if self.model is None:
            raise ValueError("El modelo debe ser construido antes de hacer una predicción.")

        return self.model.predict(input_data)


