## Identificacion de todas las rutas de APIs necesarias ##
 
## [POST] /api/v1/images/capture ##
 - **Descripción:** Recibe una imagen capturada desde la cámara del dispositivo para ser procesada.
 
 **Cuerpo de la solicitud (Request body):**
 
  {
  "image": "base64 string de la imagen"
 
 
 Respuesta exitosa: 200 OK
 {
  "status": "success",
  "data": {
    "image_id": "img_001",
    "timestamp": "2025-04-16T10:15:00Z"
  },
  "message": "Imagen recibida y procesada correctamente"
}
  }
 
 
 **Posibles errores:**
 **- 400 Bad Request:** Solicitud mal formada.
 **- 404 Not Found:** Recurso no encontrado.
 **- 500 Internal Server Error:** Error del servidor.
 
----------------------
 
## [GET] /api/v1/images/{image_id}/analysis ##
 **Descripción:** Devuelve el análisis de una imagen específica.
 
 
 
 **Parámetros de ruta:**
 - image_id: ID de la imagen a analiza.
 
 **Respuesta exitosa:** 200 OK
 
 Estructura de la API - Documentación Técnica
 {
  "status": "success",
  "data": {
    "image_id": "img_001",
    "tags": ["fruta", "banana", "comida"],
    "confidence_scores": {
      "fruta": 0.95,
      "banana": 0.88
    }
  },
  "message": "Análisis completado"
}
 
Respuesta en Proceso – 202 Accepted

{
  "status": "processing",
  "data": {
    "image_id": "img_001"
  },
  "message": "El análisis de la imagen está en proceso. Intente nuevamente más tarde."
}


 **Posibles errores:**
 - 400 Bad Request: Solicitud mal formada
 - 404 Not Found: Recurso no encontrado
 - 500 Internal Server Error: Error del servido
 
 ------------------
 
## [GET] /api/v1/multimedia/by-tag/{tag} ##
 
 **Descripción:** Devuelve recursos multimedia asociados a una etiqueta.
 

 **Parámetros de ruta:**
 - tag: Nombre de la etiqueta
 
 **Respuesta exitosa:** 200 OK
 
 {
  "status": "success",
  "data": [
    {
      "type": "image",
      "url": "https://example.com/images/banana.jpg"
    },
    {
      "type": "video",
      "url": "https://example.com/videos/banana.mp4"
    }
  ],
  "message": "Multimedia encontrado para la etiqueta"
}
 
 
 **Posibles errores:**
 - 400 Bad Request: Solicitud mal formada.
 - 404 Not Found: Recurso no encontrado.
 - 500 Internal Server Error: Error del servido.
 
 ---------
 
## [GET] /api/v1/history ##
 **Descripción:** Devuelve el historial de imágenes reconocidas.
 
 **Respuesta exitosa:** 200 OK
 
 {
  "status": "success",
  "data": {
    "Fruta": [
      {
        "image_id": "img_001",
        "timestamp": "2025-04-16T10:15:00Z",
        "description": "Una banana amarilla sobre una mesa de madera."
      },
      {
        "image_id": "img_003",
        "timestamp": "2025-04-14T14:20:00Z",
        "description": "Una manzana roja."
      }
    ],
    "Electrónica": [
      {
        "image_id": "img_002",
        "timestamp": "2025-04-15T09:45:00Z",
        "description": "Un televisor en una sala de estar."
      }
    ]
  },
  "message": "Historial del usuario agrupado por categoría"
}
 
 **Posibles errores:**
 - 400 Bad Request: Solicitud mal formada.
 - 404 Not Found: Recurso no encontrado.
 - 500 Internal Server Error: Error del servidor.
 
-----------
 
 ## [GET] /api/v1/items ##
 
 **Descripción:** Devuelve una lista de categorías o ítems reconocibles.
 
 **Respuesta exitosa:** 200 Ok
 
{
  "status": "success",
  "data": [
    {
      "id": 1,
      "name": "Fruta",
      "description": "Categoría, incluye frutas como manzanas, peras y plátanos."
    },
    {
      "id": 2,
      "name": "Electrónica",
      "description": "Dispositivos electrónicos, celulares, computadoras y televisores."
    }
  ],
  "message": "Ítems listados exitosamente"
}
 
 
 **Posibles errores:**
 - 400 Bad Request: Solicitud mal formada.
 - 404 Not Found: Recurso no encontrado.
 - 500 Internal Server Error: Error del servidor.
 
 ## [GET] /api/v1/items/{item_id} ##
 **Descripción:** Devuelve información detallada sobre un ítem específico.
 
 
 
 **Parámetros de ruta:**
 
 - item_id: ID del ítem
 **Respuesta exitosa:** 200 OK
 {
  "status": "success",
  "data": {
    "id": 1,
    "name": "Fruta",
    "description": "Incluye frutas comestibles como manzanas, plátanos, peras, etc.",
    "related_tags": ["manzana", "banana", "pera"]
  },
  "message": "Ítem recuperado correctamente"
}
 
 
 **Posibles errores:**
 - 400 Bad Request: Solicitud mal formada.
 - 404 Not Found: Recurso no encontrado.
 - 500 Internal Server Error: Error del servidor.
 
-------------------------------------
 
 ## Ejemplo de respuesta estructurada con vínculos (hypermedia)
 
  **Este es un ejemplo de una respuesta enriquecida con vínculos a otros recursos relacionados:**
 {
  "id": 123,
  "title": "What is REST",
  "content": "REST is an architectural style for building web services...",
  "published_at": "2023-11-04T14:30:00Z",
  "author": {
    "id": 456,
    "name": "John Doe",
    "profile_url": "https://example.com/authors/456"
  },
  "comments": {
    "count": 5,
    "comments_url": "https://example.com/posts/123/comments"
  },
  "self": {
    "link": "https://example.com/posts/123"
  }
 }
 
------------------
 
## Consideraciones de diseño ##
 
- **Nomenclatura:**
 
  - Todos los endpoints inician con el prefijo común `/api/` para mantener consistencia y claridad.

  - Se utilizan nombres de rutas en minúsculas, descriptivos y específicos del recurso o funcionalidad.
 
- ** Estructura Jerárquica:**
 
  - Las rutas reflejan una estructura lógica agrupada por funcionalidades (ej. `capture`, `analysis`, `multimedia`, `text`, `audio`).

  - Las rutas con parámetros dinámicos están claramente identificadas (ej. `{image_id}`, `{tag}`).
 
- **Principios de restsful**
 
  - Para los principios de restful se recomiendo utilizar los siguiente:
    - GET: Se usa para leer.
    - POST: Se utiliza para crear.
  - Se anexa un ejemplo en caso tal los endpoint de text y audio esten fuertemente ligados a una imagen:
    - GET /api/images/{image_id}/text.
    - GET /api/images/{image_id}/audio.
 
- **Versiones**
 
  - Para las versiones de la api se recomienda utilizar v como la variable de version e ir incrementando en 1 para las difernetes versiones v1, v2, v3, v4, etc... un ejemplo seria: /api/v1//images.
 