import tensorflow as tf
import cv2
import numpy as np

# Mostrar versiones
print(f"TensorFlow version: {tf.__version__}")
print(f"OpenCV version: {cv2.__version__}")

# Verificar GPUs disponibles
print(f"Num GPUs Available: {len(tf.config.list_physical_devices('GPU'))}")

# Crear imagen de prueba con OpenCV
img = np.zeros((224, 224, 3), dtype=np.uint8)
img = cv2.circle(img, (112, 112), 50, (0, 255, 0), 2)
print("Imagen de prueba creada correctamente")

# Crear modelo simple con TensorFlow
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(224, 224, 3)),
    tf.keras.layers.Conv2D(8, 3, activation='relu'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(10, activation='softmax')
])
print("Modelo básico creado correctamente")
print("Verificación completada con éxito")


mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

model.evaluate(x_test,  y_test, verbose=2)