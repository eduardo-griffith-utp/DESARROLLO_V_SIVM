##import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras import layers, models
from base_model import BaseModel





class ImageClassifier(BaseModel):
    """Modelo de clasificación de imágenes basado en MobileNetV2."""
    
    def __init__(self, num_classes, input_shape=(224, 224, 3), model_path=None):    
        """
        Inicializa el clasificador de imágenes.
        
        Args:
            num_classes (int): Número de clases para clasificación
            input_shape (tuple): Forma de entrada de las imágenes
            model_path (str, optional): Ruta al modelo preentrenado
        """
        super().__init__(model_path)
        self.num_classes = num_classes
        self.input_shape = input_shape
        
    def build(self):
        """Construye la arquitectura del modelo usando MobileNetV2 como base."""
        # Cargar base preentrenada
        base_model = MobileNetV2(
            input_shape=self.input_shape,
            include_top=False,
            weights='imagenet'
        )
        
        # Congelar capas del modelo base (transfer learning)
        base_model.trainable = False
        
        # Construir modelo completo
        inputs = layers.Input(shape=self.input_shape)
        x = base_model(inputs, training=False)
        x = layers.GlobalAveragePooling2D()(x)
        x = layers.Dense(256, activation='relu')(x)
        x = layers.Dropout(0.5)(x)
        outputs = layers.Dense(self.num_classes, activation='softmax')(x)
        
        self.model = models.Model(inputs, outputs)
        self.model.compile(
            optimizer='adam',
        loss='categorical_crossentropy',
            metrics=['accuracy']
        )
        
        return self.model
    

    class ImageClassifierInference:
        """Clase para realizar inferencia con un modelo entrenado."""
    
    def __init__(self, model_path, class_names, image_processor):
        """
        Inicializa el sistema de inferencia.
        
        Args:
            model_path (str): Ruta al modelo entrenado
            class_names (list): Lista de nombres de clases
            image_processor (ImageProcessor): Procesador de imágenes
        """
        self.classifier = ImageClassifier(num_classes=len(class_names))
        self.classifier.build()
        self.classifier.load_weights(model_path)
        self.class_names = class_names
        self.processor = image_processor
        
    def classify_image(self, image_path, top_k=5):
        """
        Clasifica una imagen y devuelve las mejores predicciones.
        
        Args:
            image_path (str): Ruta a la imagen
            top_k (int): Número de mejores predicciones a devolver
            
        Returns:
            list: Lista de tuplas (clase, confianza)
        """
        # Cargar y preprocesar imagen
        original, processed = self.processor.process_for_model(image_path)
        
        # Realizar predicción
        predictions = self.classifier.predict(processed)[0]
        
        # Obtener las top_k predicciones
        top_indices = predictions.argsort()[-top_k:][::-1]
        top_predictions = [
            (self.class_names[idx], float(predictions[idx]))
            for idx in top_indices
        ]
        return top_predictions, original