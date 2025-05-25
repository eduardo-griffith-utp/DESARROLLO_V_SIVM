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

Este directorio será utilizado exclusivamente por el equipo de IA para entrenar el modelo de recognition. 


- Directorio base: `training_data/` 

- Subcarpetas para un objeto o cosa, identificadas con un código único: 

training_data/ ├── ejemplo_gato/ │ ├── image1.jpg │ ├── image2.jpg ├── ejemplo_perro/ ├── image1.jpg ├── image2.jpg 


#### **Convenciones de Nomenclatura**: 

- Carpetas: `item` (item se refiere a cualquier objeto (animal, lugar, objeto, etc)y solo es una representacion, por ejemplo : mesa, gallo, perro, silla, entre otros). 

- Archivos: `image.jpg` (se refiere a las imagenes del objeto, animal o lugares). 


### **Recursos Multimedia Adicionales** 

Este directorio estará destinado a almacenar recursos adicionales relacionados con cada ítem para enriquecer la experiencia del usuario en la aplicación móvil. 

- Directorio base: `multimedia_resources/` 

- Subcarpetas organizadas por tipo de recurso dentro de cada ítem: 

├── training_data/ 

│   ├── ejemplo-perro/ 

│   │   ├── image1.jpg 

│   │   ├── image2.jpg 

│   ├── ejemplo2_gato/ 

│       ├── image1.jpg 

│       ├── image2.jpg 

├── multimedia_resources/ 

    ├── ejemplo_perro/ 

    │   ├── images/ 

    │   │   ├── detail1.jpg 

    │   │   ├── detail2.jpg 

    │   ├── videos/ 

    │   │   ├── demo1.mp4 

    │   ├── audio/ 

    │   │   ├── description.mp3 

    │   ├── text/ 

    │       ├── description.txt 

    │       ├── details.md 

    ├── ejemplo_gato/ 

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