import os
import glob
import random
import shutil

def list_image_files(directory, extensions=('jpg', 'jpeg', 'png')):
    """
    Lista todos los archivos de imagen en un directorio.

    Args:
        directory (str): Directorio a explorar.
        extensions (tuple): Extensiones de archivo a incluir.

    Returns:
        list: Lista de rutas a archivos de imagen.
    """
    files = []
    for ext in extensions:
        pattern = os.path.join(directory, f"*.{ext}")
        files.extend(glob.glob(pattern))
    # También buscar en mayúsculas
    for ext in extensions:
        pattern = os.path.join(directory, f"*.{ext.upper()}")
        files.extend(glob.glob(pattern))
    return sorted(files)

def create_train_val_split(image_dir, output_dir, val_ratio=0.2, copy=False):
    """
    Crea una división entre entrenamiento y validación.

    Args:
        image_dir (str): Directorio con las imágenes originales.
        output_dir (str): Directorio donde crear la estructura train/val.
        val_ratio (float): Proporción para validación (0.0-1.0).
        copy (bool): Si es True, copia los archivos en lugar de moverlos.

    Returns:
        tuple: (Número de imágenes de entrenamiento, número de imágenes de validación)
    """
    # Crear directorios si no existen
    train_dir = os.path.join(output_dir, 'train')
    val_dir = os.path.join(output_dir, 'val')
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)

    # Obtener lista de categorías (subdirectorios)
    categories = [d for d in os.listdir(image_dir)
                  if os.path.isdir(os.path.join(image_dir, d))]

    train_count = 0
    val_count = 0

    for category in categories:
        # Crear directorios para esta categoría
        os.makedirs(os.path.join(train_dir, category), exist_ok=True)
        os.makedirs(os.path.join(val_dir, category), exist_ok=True)

        # Listar imágenes de esta categoría
        category_dir = os.path.join(image_dir, category)
        images = list_image_files(category_dir)

        # Mezclar aleatoriamente
        random.shuffle(images)

        # Dividir en train/val
        split_idx = int(len(images) * (1 - val_ratio))
        train_images = images[:split_idx]
        val_images = images[split_idx:]

        # Mover/copiar a destino
        for img in train_images:
            dst = os.path.join(train_dir, category, os.path.basename(img))
            if copy:
                shutil.copy2(img, dst)
            else:
                shutil.move(img, dst)
            train_count += 1

        for img in val_images:
            dst = os.path.join(val_dir, category, os.path.basename(img))
            if copy:
                shutil.copy2(img, dst)
            else:
                shutil.move(img, dst)
            val_count += 1

    print(f"División completada: {train_count} imágenes de entrenamiento, {val_count} imágenes de validación.")
    return train_count, val_count
