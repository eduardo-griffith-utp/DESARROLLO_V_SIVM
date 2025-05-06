import tensorflow as tf
import os
import datetime

class Trainer:
    """Clase para entrenar modelos de deep learning."""
    
    def __init__(self, model, train_data, val_data, output_dir='./output'):
        """
        Inicializa el entrenador.
        
        Args:
            model: Modelo a entrenar
            train_data: Datos de entrenamiento
            val_data: Datos de validación
            output_dir (str): Directorio para guardar resultados
        """
        self.model = model
        self.train_data = train_data
        self.val_data = val_data
        self.output_dir = output_dir
        self.history = None
        
        # Crear directorios de salida
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(os.path.join(output_dir, 'checkpoints'), exist_ok=True)
        os.makedirs(os.path.join(output_dir, 'logs'), exist_ok=True)
        
    def get_callbacks(self):
        """Configura callbacks para el entrenamiento."""
        checkpoint_path = os.path.join(
            self.output_dir, 'checkpoints', 'model_{epoch:02d}_{val_accuracy:.4f}.h5'
        )
        
        callbacks = [
            # Guardar el mejor modelo
            tf.keras.callbacks.ModelCheckpoint(
                filepath=checkpoint_path,
                save_weights_only=True,
                monitor='val_accuracy',
                mode='max',
                save_best_only=True
            ),
            # Detener entrenamiento si no hay mejora
            tf.keras.callbacks.EarlyStopping(
                monitor='val_accuracy',
                patience=5,
                restore_best_weights=True
            ),
            # Reducir learning rate si no hay mejora
            tf.keras.callbacks.ReduceLROnPlateau(
                monitor='val_loss',
                factor=0.2,
                patience=3
            ),
            # TensorBoard para visualizar el progreso
            tf.keras.callbacks.TensorBoard(
                log_dir=os.path.join(self.output_dir, 'logs', datetime.datetime.now().strftime('%Y%m%d-%H%M%S'))
            )
        ]
        
        return callbacks
        
    def train(self, epochs=10, initial_epoch=0):
        """
        Entrena el modelo.
        
        Args:
            epochs (int): Número total de épocas
            initial_epoch (int): Época inicial (útil para reanudar)
            
        Returns:
            History: Historial de entrenamiento
        """
        callbacks = self.get_callbacks()
        
        self.history = self.model.fit(
            self.train_data,
            validation_data=self.val_data,
            epochs=epochs,
            initial_epoch=initial_epoch,
            callbacks=callbacks,
            verbose=1
        )
        
        # Guardar el modelo final
        final_model_path = os.path.join(self.output_dir, 'final_model.h5')
        self.model.save_weights(final_model_path)
        
        return self.history
