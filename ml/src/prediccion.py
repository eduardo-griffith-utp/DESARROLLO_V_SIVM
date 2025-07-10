import os
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import matplotlib.pyplot as plt
import json
import base64
from io import BytesIO

def load_saved_model(model_dir=None):
    """Carga el modelo y los nombres de clases"""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_dir = os.path.join(base_dir, 'models')
    model_path = os.path.join(model_dir, "best_model.h5")
    metadata_path = os.path.join(model_dir, "class_mapping.json")
    
    model = load_model(model_path)
    with open(metadata_path, 'r') as f:
        metadata = json.load(f)
    ##print("Salidas del modelo:", model.output_shape)    
    class_names = metadata["classes"]
    return model, class_names

def preprocess_base64_image(base64_string, target_size=(224, 224)):
    """Convierte imagen en base64 a imagen procesada por el modelo"""
    try:
        # Decodificar base64 a bytes
        image_data = base64.b64decode(base64_string)

        # Crear imagen desde BytesIO
        img = Image.open(BytesIO(image_data)).convert('RGB')

        # Redimensionar manteniendo relación de aspecto
        img.thumbnail(target_size, Image.Resampling.LANCZOS)

        # Crear nueva imagen del tamaño requerido
        new_img = Image.new('RGB', target_size, (255, 255, 255))
        new_img.paste(img, ((target_size[0]-img.size[0])//2,
                            (target_size[1]-img.size[1])//2))

        # Convertir a array y normalizar
        img_array = np.array(new_img) / 255.0
        return np.expand_dims(img_array, axis=0)

    except Exception as e:
        print(f"Error al procesar imagen base64: {str(e)}")
        raise

def predict_from_base64(model, class_names, base64_string):
    """Realiza predicción desde imagen base64 y devuelve un JSON"""
    try:
        processed_img = preprocess_base64_image(base64_string)

        predictions = model.predict(processed_img, verbose=0)
        predicted_class_idx = np.argmax(predictions[0])
        confidence = np.max(predictions[0])
        predicted_class = class_names[predicted_class_idx]
        sort_indices = np.argsort(predictions[0])[::-1][:5]

        resultado = [
                {
                    class_names[idx] :round(float(predictions[0][idx]), 4)
                }
                for idx in np.argsort(predictions[0])[::-1][:5]
            ]
        return resultado

    except Exception as e:
        print(f"Error durante la predicción desde base64: {str(e)}")
        raise

def preprocess_image(img_path, target_size=(224, 224)):
    """Preprocesa la imagen para el modelo"""
    try:
        # Cargar imagen y convertir a RGB
        img = Image.open(img_path).convert('RGB')
        
        # Redimensionar manteniendo relación de aspecto
        img.thumbnail(target_size, Image.Resampling.LANCZOS)
        
        # Crear imagen del tamaño exacto con fondo blanco
        new_img = Image.new('RGB', target_size, (255, 255, 255))
        new_img.paste(img, ((target_size[0]-img.size[0])//2, 
                          (target_size[1]-img.size[1])//2))
        
        # Convertir a array y normalizar
        img_array = np.array(new_img) / 255.0
        return np.expand_dims(img_array, axis=0)
    
    except Exception as e:
        print(f"Error procesando imagen: {str(e)}")
        raise

def predict_and_display(model, class_names, img_path):
    """Realiza la predicción y muestra los resultados"""
    try:
        # Preprocesar imagen
        processed_img = preprocess_image(img_path)
        
        # Realizar predicción
        predictions = model.predict(processed_img)
        predicted_class_idx = np.argmax(predictions[0])
        confidence = np.max(predictions[0])
        predicted_class = class_names[predicted_class_idx]
        
        # Mostrar comparación de imágenes
        plt.figure(figsize=(12, 6))
        
        # Imagen original
        plt.subplot(1, 2, 1)
        original_img = Image.open(img_path)
        plt.imshow(original_img)
        plt.title(f"Original\nTamaño: {original_img.size}")
        plt.axis('off')
        
        # Imagen preprocesada
        plt.subplot(1, 2, 2)
        plt.imshow(processed_img[0])  # Mostrar primera (y única) imagen del batch
        plt.title(f"Preprocesada (128×128)\nPredicción: {predicted_class} ({confidence:.2%})")
        plt.axis('off')
        
        plt.tight_layout()
        plt.show()
        
        # Mostrar resultados detallados en consola
        print("\nRESULTADOS DE CLASIFICACIÓN")
        print("="*40)
        print(f"Clase predicha: {predicted_class} (Confianza: {confidence:.2%})")
        print(f"Índice de clase: {predicted_class_idx}")
        
        # Mostrar top 5 predicciones
        print("\nTOP 5 PREDICCIONES:")
        sorted_indices = np.argsort(predictions[0])[::-1]  # Orden descendente
        for i, idx in enumerate(sorted_indices[:5]):
            print(f"{i+1}. {class_names[idx]}: {predictions[0][idx]:.2%}")
        return predicted_class
            
    except Exception as e:
        print(f"\nERROR durante la predicción: {str(e)}")
        

if __name__ == "__main__":
    try:
        # Cargar modelo
        print("Cargando modelo...")
        model, class_names = load_saved_model()
        print(f"Modelo cargado. Clases disponibles: {class_names}")
        
        # Leer archivo base64
        base64_file_path = input("\nIntroduce la ruta del archivo con la imagen en base64: ").strip('"')

        if not os.path.exists(base64_file_path):
            raise FileNotFoundError(f"No se encontró el archivo: {base64_file_path}")

        with open(base64_file_path, "r") as f:
            base64_str = f.read().strip()

        # Limpiar encabezado si lo tiene
        if base64_str.startswith("data:image"):
            base64_str = base64_str.split(",")[1]

        print("\nProcesando imagen...")

        # Preprocesar imagen
        processed_img = preprocess_base64_image(base64_str)

        # Realizar predicción
        predictions = model.predict(processed_img)
        predicted_class_idx = np.argmax(predictions[0])
        confidence = np.max(predictions[0])
        predicted_class = class_names[predicted_class_idx]

        # Mostrar comparación de imágenes
        from io import BytesIO
        import base64
        img = Image.open(BytesIO(base64.b64decode(base64_str)))

        plt.figure(figsize=(12, 6))

        # Imagen original
        plt.subplot(1, 2, 1)
        plt.imshow(img)
        plt.title(f"Original\nTamaño: {img.size}")
        plt.axis('off')

        # Imagen preprocesada
        plt.subplot(1, 2, 2)
        plt.imshow(processed_img[0])
        plt.title(f"Preprocesada (224×224)\nPredicción: {predicted_class} ({confidence:.2%})")
        plt.axis('off')

        plt.tight_layout()
        plt.show()

        # Mostrar resultados detallados en consola
        print("\nRESULTADOS DE CLASIFICACIÓN")
        print("="*40)
        print(f"Clase predicha: {predicted_class} (Confianza: {confidence:.2%})")
        print(f"Índice de clase: {predicted_class_idx}")

        print("\nTOP 5 PREDICCIONES:")
        sorted_indices = np.argsort(predictions[0])[::-1]
        for i, idx in enumerate(sorted_indices[:5]):
            print(f"{i+1}. {class_names[idx]}: {predictions[0][idx]:.2%}")

        # Crear JSON con el resultado
        resultado = {
            "clase_predicha": predicted_class
        }

        ##resultado_json = json.dumps(resultado, ensure_ascii=False)
        ##print("\nResultado en formato JSON:")
        ##print(resultado_json)

        # Guardar el resultado en un archivo JSON
        with open("resultado.json", "w", encoding="utf-8") as f:
            json.dump(resultado, f, ensure_ascii=False, indent=4)
        print("\nEl resultado ha sido guardado en 'resultado.json'.")

    except Exception as e:
        print(f"\nError general: {str(e)}")
