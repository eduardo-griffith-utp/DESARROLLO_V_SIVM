  
## Propuesta de Integración del Componente de Control de Contenido

### Objetivo

Establecer una propuesta clara para que el equipo de desarrollo backend integre un componente que permita la detección automática de contenido explícito (NSFW) en las imágenes capturadas por los usuarios, como parte del flujo general del sistema.

---

### Componente seleccionado: Clarifai – Modelo NSFW (`nsfw-v1.0`)

Se ha seleccionado el proveedor **Clarifai**, que ofrece un modelo preentrenado llamado `nsfw-v1.0` especializado en identificar imágenes que contienen contenido sexual, sugestivo o inapropiado.

#### Motivos de la selección:
- No requiere tarjeta de crédito.
- Plan gratuito amplio (30,000 operaciones/mes).
- API bien documentada.
- Respuesta estructurada con niveles de confianza.
- Facilidad de integración mediante SDK (Node.js, Python, etc.).

---

### Propuesta de integración técnica

#### Arquitectura:

El componente se incorpora en el **módulo de Reconocimiento de Contenido**:
# Flujo de integración del componente Clarifai (NSFW)


### Flujo general

1. El cliente envía la imagen al backend mediante `POST /api/v1/images/capture`.
2. El backend almacena la imagen (base64 o temporalmente).
3. El módulo de Reconocimiento de Contenido la envía a Clarifai utilizando el modelo `nsfw-v1.0`.
4. Clarifai responde con etiquetas como: `nsfw`, `safe`, `suggestive`, y sus respectivos niveles de confianza.
5. El módulo Resultado Explícito interpreta la respuesta.
6. El resultado final se envía al cliente con una estructura como:

**json**:
´´´json
{
  "image_id": "img_002",
  "nsfw": true,
  "confianza": 0.91,
  "etiquetas": ["nsfw", "explicit"]
}

***Recomendaciones para el Equipo de Backend**
**Instalación y autenticación**
Instalar el SDK oficial de Clarifai para Node.js:

**en bash**

npm install clarifai

**Crear un archivo .env en el backend y definir la clave:**


CLARIFAI_API_KEY= la key 


Importar y usar la clave desde el código usando dotenv.

interpretacion:

Si nsfw > 0.85 → Marcar imagen como inapropiada

Si safe > 0.95 → Marcar imagen como segura



respuesta esperada desde Clarifai

json

[
  { "name": "nsfw", "value": 0.91 },
  { "name": "explicit", "value": 0.76 },
  { "name": "safe", "value": 0.04 }
]


