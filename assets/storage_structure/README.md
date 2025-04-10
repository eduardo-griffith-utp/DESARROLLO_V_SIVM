# Diseño de la Estructura de Almacenamiento 

 

Este documento describe el diseño de una estructura eficiente para organizar las imágenes de entrenamiento del modelo de IA y los recursos multimedia adicionales. La propuesta está enfocada en facilitar tanto el trabajo del equipo de IA como la integración con la API para la aplicación móvil. 

 

--- 

 

## **Objetivos**

 

1. **Facilitar el Entrenamiento del Modelo**: 

   - Garantizar una organización clara de las imágenes. 

   - Proveer una estructura escalable que soporte hasta 100 ítems con 1-5 imágenes por ítem. 

 _________________________________________________________________________________________________________________

2. **Optimizar el Almacenamiento de Recursos Multimedia**: 

   - Organizar recursos adicionales (imágenes, videos, audios, textos) asociados a los ítems. 

   - Establecer convenciones de nomenclatura consistentes para evitar errores y facilitar la recuperación. 

 __________________________________________________________________________________________________________________

3. **Soporte a la Escalabilidad y Mantenimiento**: 

   - Diseñar una estructura que permita el crecimiento del sistema. 

   - Incorporar opciones como metadatos para mejorar la gestión. 

_____________________________________________________________________________________________________________________

## **Estructura de Carpetas** 


### **Imágenes de Entrenamiento** 

Este directorio será utilizado exclusivamente por el equipo de IA para entrenar el modelo de reconocimiento. 


- Directorio base: `training_data/` 

- Subcarpetas para cada ítem, identificadas con un código único: 

training_data/ ├── item001/ │ ├── image001.jpg │ ├── image002.jpg ├── item002/ ├── image001.jpg ├── image002.jpg 


#### **Convenciones de Nomenclatura**: 

- Carpetas: `itemXXX` (donde `XXX` es un número único de tres dígitos, por ejemplo, `item001`). 

- Archivos: `imageNNN.jpg` (donde `NNN` es un número incremental, por ejemplo, `image001.jpg`). 


### **Recursos Multimedia Adicionales** 

Este directorio estará destinado a almacenar recursos adicionales relacionados con cada ítem para enriquecer la experiencia del usuario en la aplicación móvil. 

- Directorio base: `multimedia_resources/` 

- Subcarpetas organizadas por tipo de recurso dentro de cada ítem: 

├── training_data/ 

│   ├── item001/ 

│   │   ├── image001.jpg 

│   │   ├── image002.jpg 

│   ├── item002/ 

│       ├── image001.jpg 

│       ├── image002.jpg 

├── multimedia_resources/ 

    ├── item001/ 

    │   ├── images/ 

    │   │   ├── detail001.jpg 

    │   │   ├── detail002.jpg 

    │   ├── videos/ 

    │   │   ├── demo001.mp4 

    │   ├── audio/ 

    │   │   ├── description.mp3 

    │   ├── text/ 

    │       ├── description.txt 

    │       ├── details.md 

    ├── item002/ 

        ├── images/ 

        ├── videos/ 

        ├── audio/ 

        ├── text/ 


#### **Convenciones de Nomenclatura**: 

- Subcarpetas: 

- `images/` para imágenes adicionales. 

- `videos/` para videos demostrativos. 

- `audio/` para clips de audio relacionados. 

- `text/` para descripciones o documentos en texto. 

- Archivos: 

- Nombres descriptivos con identificadores numéricos, por ejemplo, `detail001.jpg`, `demo001.mp4`, `description.txt`. 

## **Guías de Uso** 

### **Para el Equipo de IA**: 

- Verificar que las imágenes estén correctamente etiquetadas según las convenciones antes de iniciar el entrenamiento. 

- Mantener las imágenes dentro de la carpeta `training_data/`. 


### **Para el Equipo API/Móvil**: 

- Asegurarse de que la recuperación de datos desde el sistema API utilice los nombres y rutas definidos en esta estructura. 

- Usar metadatos para describir los recursos, si es necesario. 


## **Aspectos Clave** 


1. **Escalabilidad**: 

 - Esta estructura es modular, por lo que pueden añadirse nuevos ítems creando más carpetas en `training_data/` y `multimedia_resources/`. 

 

2. **Uso de Metadatos**: 

 - Considerar un archivo JSON para describir los recursos asociados a cada ítem. Ejemplo: 

   ```json 

   { 

       "item_id": "item001", 

       "images": [ 

           "training_data/item001/image001.jpg", 

           "training_data/item001/image002.jpg" 

       ], 

       "multimedia": { 

           "images": [ 

               "multimedia_resources/item001/images/detail001.jpg", 

               "multimedia_resources/item001/images/detail002.jpg" 

           ], 

           "videos": ["multimedia_resources/item001/videos/demo001.mp4"], 

           "audio": ["multimedia_resources/item001/audio/description.mp3"], 

           "text": ["multimedia_resources/item001/text/description.txt"] 

       } 

   } 

   ``` 

 

3. **Optimización**: 

 - Comprimir archivos grandes (como videos o audios) para reducir el uso de almacenamiento y acelerar su recuperación. 

 

4. **Colaboración entre Equipos**: 

 - Mantener comunicación entre los equipos de IA y API para alinear necesidades y asegurar que la estructura cumple con los objetivos del sistema. 


## **Diagramas de Referencia** 

Para una mejor visualización de la estructura, aquí tienes un diagrama generado con Mermaid: 

 

```mermaid 

graph TD 

  root[storage-structure/] 

  training[training_data/] 

  multimedia[multimedia_resources/] 

  root --> training 

  root --> multimedia 

  training --> item001[item001/] 

  multimedia --> item001_multimedia[item001/] 

  item001_multimedia --> images[images/] 

  item001_multimedia --> videos[videos/] 

  item001_multimedia --> audio[audio/] 

  item001_multimedia --> text[text/] 