import pathlib
import cv2
import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
import tensorflow_datasets as tfds
from pathlib import Path
import math
import matplotlib.pyplot as plt

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
    
    def preprocess_image(self, image):
        image = cv2.resize(image, self.target_size)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        if self.normalize:
            image = image.astype('float32') / 255.0
        return image

    def load_and_preprocess(self, image_path):
        image = self.load_image(image_path)
        return self.preprocess_image(image)


data_dir = pathlib.Path(r'C:\Users\manue\Documents\GitHub\DESARROLLO_V_SIVM\ml\ai\image_recognition\utils\datos')


# Inicializar el procesador
processor = ImageProcessor()

# Recorrer carpetas e imágenes
image_data = []
labels = []

for image_path in data_dir.rglob("*"):
    if image_path.suffix.lower() in ['.jpg', '.jpeg', '.png']:
        try:
            image = processor.load_and_preprocess(str(image_path))
            
            # Etiqueta = nombre de la carpeta justo anterior a la imagen
            label = image_path.parent.name
            
            image_data.append(image)
            labels.append(label)
        except Exception as e:
            print(f"Error procesando {image_path}: {e}")

# `image_data` contiene las imágenes procesadas
# `labels` contiene las clases correspondientes
print(f"Se cargaron {len(image_data)} imágenes.")


image_count = len(list(data_dir.rglob('*.jpg')))
print(image_count)


crist = list(data_dir.glob('train/CRISTO REDENTOR/*'))  # No incluye subcarpetas
if crist:
    img = PIL.Image.open(str(crist[0]))
    img.show()  # Para mostrar la imagen
else:
    print("No se encontraron imágenes en 'train/CRISTO REDENTOR'")

crist = list(data_dir.glob('train/CRISTO REDENTOR/*'))  # No incluye subcarpetas
if crist:
    img = PIL.Image.open(str(crist[1]))
    img.show()  # Para mostrar la imagen
else:
    print("No se encontraron imágenes en 'train/CRISTO REDENTOR'")
    
data_dir = Path(r'C:\Users\manue\Documents\GitHub\DESARROLLO_V_SIVM\ml\ai\image_recognition\utils\datos\train')


batch_size = 32
img_height = 180
img_width = 180

train_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

val_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="validation",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

class_names = train_ds.class_names
print(class_names)

for images, labels in train_ds.take(1):
    print("Cantidad de imágenes en el batch:", images.shape[0])


for images, labels in train_ds.take(1):
    num_images = len(images)
    cols = 4  # Puedes ajustar esto según tu preferencia
    rows = math.ceil(num_images / cols)

    plt.figure(figsize=(cols * 3, rows * 3))

    for i in range(num_images):
        ax = plt.subplot(rows, cols, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(class_names[labels[i]])
        plt.axis("off")

    plt.tight_layout()
    plt.show()

for image_batch, labels_batch in train_ds:
  print(image_batch.shape)
  print(labels_batch.shape)
  break

normalization_layer = tf.keras.layers.Rescaling(1./255)

normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
image_batch, labels_batch = next(iter(normalized_ds))
first_image = image_batch[0]
# Notice the pixel values are now in `[0,1]`.
print(np.min(first_image), np.max(first_image))

AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

num_classes = len(class_names)

model = tf.keras.Sequential([
  tf.keras.layers.Rescaling(1./255),
  tf.keras.layers.Conv2D(32, 3, activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Conv2D(32, 3, activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Conv2D(32, 3, activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(num_classes)
])

model.compile(
  optimizer='adam',
  loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
  metrics=['accuracy'])

model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=3
)

list_ds = tf.data.Dataset.list_files(str(data_dir/'*/*'), shuffle=False)
list_ds = list_ds.shuffle(image_count, reshuffle_each_iteration=False)

for f in list_ds.take(len(class_names)):
  print(f.numpy())

class_names = np.array(sorted([item.name for item in data_dir.glob('*') if item.name != "LICENSE.txt"]))
print(class_names)

val_size = int(image_count * 0.2)
train_ds = list_ds.skip(val_size)
val_ds = list_ds.take(val_size)

print(tf.data.experimental.cardinality(train_ds).numpy())
print(tf.data.experimental.cardinality(val_ds).numpy())

def get_label(file_path):
  # Convert the path to a list of path components
  parts = tf.strings.split(file_path, os.path.sep)
  # The second to last is the class-directory
  one_hot = parts[-2] == class_names
  # Integer encode the label
  return tf.argmax(one_hot)

def decode_img(img):
  # Convert the compressed string to a 3D uint8 tensor
  img = tf.io.decode_jpeg(img, channels=3)
  # Resize the image to the desired size
  return tf.image.resize(img, [img_height, img_width])

def process_path(file_path):
  label = get_label(file_path)
  # Load the raw data from the file as a string
  img = tf.io.read_file(file_path)
  img = decode_img(img)
  return img, label

# Set `num_parallel_calls` so multiple images are loaded/processed in parallel.
train_ds = train_ds.map(process_path, num_parallel_calls=AUTOTUNE)
val_ds = val_ds.map(process_path, num_parallel_calls=AUTOTUNE)

for image, label in train_ds.take(1):
  print("Image shape: ", image.numpy().shape)
  print("Label: ", label.numpy())

def configure_for_performance(ds):
  ds = ds.cache()
  ds = ds.shuffle(buffer_size=1000)
  ds = ds.batch(batch_size)
  ds = ds.prefetch(buffer_size=AUTOTUNE)
  return ds

train_ds = configure_for_performance(train_ds)
val_ds = configure_for_performance(val_ds)

image_batch, label_batch = next(iter(train_ds))

plt.figure(figsize=(10, 10))
for i in range(9):
  ax = plt.subplot(3, 3, i + 1)
  plt.imshow(image_batch[i].numpy().astype("uint8"))
  label = label_batch[i]
  plt.title(class_names[label])
  plt.axis("off")

model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=3
)

