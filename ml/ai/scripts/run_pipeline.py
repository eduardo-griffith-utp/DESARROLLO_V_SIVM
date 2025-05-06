import os
import sys
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from image_recognition.utils.file_utils import create_train_val_split
from tensorflow import keras
import tensorflow as tf
from keras.src.legacy.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from keras import layers, models
import matplotlib.pyplot as plt

# Rutas
BASE_DIR = r"C:\Users\ROG M16\Desktop\UTP\DESARROLLO_V_SIVM\ml\ai"
RAW_IMAGES = os.path.join(BASE_DIR, "image_recognition", "utils", "datos", "train")
SPLIT_DIR = os.path.join(BASE_DIR, "image_recognition", "utils", "datos", "split")

# 1. Dividir imágenes (solo la primera vez)
if not os.path.exists(os.path.join(SPLIT_DIR, "train")):
    print("Dividiendo imágenes...")
    create_train_val_split(image_dir=RAW_IMAGES, output_dir=SPLIT_DIR, val_ratio=0.2, copy=True)

# 2. Preparar generadores
train_dir = os.path.join(SPLIT_DIR, "train")
val_dir = os.path.join(SPLIT_DIR, "val")

img_size = (224, 224)
batch_size = 16

train_datagen = ImageDataGenerator(rescale=1.0 / 255)
val_datagen = ImageDataGenerator(rescale=1.0 / 255)

train_gen = train_datagen.flow_from_directory(
    train_dir, target_size=img_size, batch_size=batch_size, class_mode="categorical"
)
val_gen = val_datagen.flow_from_directory(
    val_dir, target_size=img_size, batch_size=batch_size, class_mode="categorical"
)

# 3. Construir modelo
base_model = MobileNetV2(weights="imagenet", include_top=False, input_shape=(224, 224, 3))
base_model.trainable = False

model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation="relu"),
    layers.Dense(train_gen.num_classes, activation="softmax")
])

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

# 4. Entrenar modelo
history = model.fit(train_gen, validation_data=val_gen, epochs=5)

# 5. Graficar resultados
plt.plot(history.history["accuracy"], label="Train Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.xlabel("Épocas")
plt.ylabel("Precisión")
plt.legend()
plt.title("Precisión del modelo")
plt.show()
