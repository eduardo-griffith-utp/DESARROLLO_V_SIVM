# El sistema de diseño (con enlaces a los archivos) 

## Sistema de Diseño VisioAI

Esta documentacion describe las pantallas y componentes clave del sistema de diseño de la aplicación **VisioAI**, incluyendo colores, tipografías, navegación, estados de los componentes y adaptaciones responsivas.

---
## Índice

1. [Pantalla de inicio / Splash](#pantalla-de-inicio--splash)
2. [Pantalla principal / Dashboard](#pantalla-principal--dashboard)
3. [Pantalla de captura de imagen](#pantalla-de-captura-de-imagen)
4. [Pantalla de resultados de identificación](#pantalla-de-resultados-de-identificación)
5. [Pantalla de resultado detallado (post-escaneo)](#pantalla-de-resultado-detallado-post-escaneo)
6. [Pantalla de historial](#pantalla-de-historial)
7. [Pantalla de configuración](#pantalla-de-configuración)


## Pantalla de inicio / Splash

**Imagen:** `frontend\design\Assets-Resources\Pantallas de alta fidelidad\1. Pantalla de Inicio splash.pdf`
**Imagen:** `frontend\design\Assets-Resources\Pantallas de alta fidelidad\1.1. Pantalla de Inicio splash barra carga.pdf`


### Elementos de interfaz finalizados:

* **Fondo:** `#FAFAFA` (blanco suave)
* **Logotipo:** Centrado
* **Texto del nombre:** `VisioAI` en Poppins Bold, `#212121`
* **Subtítulo:** “Identificación Visual de Materiales”, Poppins Regular, `#757575`
* **Indicador de carga:** barra horizontal inferior en gris claro
* **Distribución centrada verticalmente**

### Navegación:

* Pantalla no interactiva
* Redirige automáticamente al dashboard tras unos segundos

### Estados de componentes:

* Barra de carga: estática en wireframe, animada en diseño funcional

### Responsive Design:

* Optimizada para móviles y tablets
* Elementos centrados, con márgenes adaptados

---

## Pantalla principal / Dashboard

**Imagen:** `frontend\design\Assets-Resources\Pantallas de alta fidelidad\2. Pantalla principal.pdf`

### Elementos de interfaz finalizados:

* **Fondo:** `#FAFAFA`
* **Logo VisioAI:** centrado en la parte superior, texto 'VisioAI' (Poppins Bold, #212121)
* **Texto de bienvenida:**

  * Título: “¡Bienvenido!”, Poppins Bold, `#212121`
  * Subtítulo: “Identifica materiales mediante imágenes”, Poppins Regular, `#757575`
* **Botón principal "ESCANEAR":**

  * Fondo: `#000000`, texto blanco, ícono blanco
  * Border-radius: `1.23rem`, sombra suave
* **Navegación inferior:**

  * Íconos: Inicio, Escanear (activo), Historial, Ajustes
  * Ícono activo: `#E91E63`, inactivos: `#757575`

### Navegación:

* Botón “ESCANEAR” lleva a la pantalla de captura
* Menú inferior permite navegar a otras secciones

### Estados de componentes:

* Botón con estados: normal, presionado (`#1a1a1a`), deshabilitado (`#333333`)
* botón tiene ícono integrado

### Responsive Design:

* Layout adaptable a móviles y tablets
* Componentes táctiles accesibles

---

## Pantalla de captura de imagen

**Imagen:** `frontend\design\Assets-Resources\Pantallas de alta fidelidad\3. Pantalla de captura de imagen (para identificacion).pdf`

### Elementos de interfaz finalizados:

* Encabezado con ícono de cámara y título
* Vista previa de cámara
* Botón de captura (negro con borde magenta, ícono blanco)
* Botones: cambiar cámara (esquina superior derecha), ayuda (superior izquierda)
* Guías visuales para centrado
* Feedback de carga posterior a la captura

### Navegación:

* Tras capturar, redirige a pantalla de resultados
* Flecha para volver al dashboard

### Estados de componentes:

* Botón de captura: normal, presionado, deshabilitado
* Mensajes si la cámara no está disponible
* Animaciones suaves al cambiar de cámara

### Responsive Design:

* Diseño vertical para móviles
* En tablets: elementos redimensionados, márgenes amplios

---

## Pantalla de resultados de identificación
**Imagen:** `frontend\design\Assets-Resources\Pantallas de alta fidelidad\4. Pantalla de Resultados de identificacion.pdf`

### Elementos de interfaz finalizados:

* Encabezado: título y botón de retroceso
* Lista de resultados: miniatura, nombre, descripción, botón “Ver más”
* Botón "Capturar otra vez": negro con texto blanco, centrado
* Cards con sombra sutil y buen espaciado

### Navegación:

* "Capturar otra vez": redirige a captura
* Botón “Ver más”: muestra detalles adicionales

### Estados de componentes:

* Botón con estados: normal, hover, presionado, deshabilitado
* Estado vacío: mensaje informativo con botón para intentar nuevamente

### Responsive Design:

* Móviles: scroll vertical
* Tablets: grilla de 2 columnas

---

## Pantalla de resultado detallado (post-escaneo)

**Imagen:** `frontend\design\Assets-Resources\Pantallas de alta fidelidad\5. Pantalla de detalle del elemento identificado.pdf`

### Elementos de interfaz finalizados:

* Fondo: `#FAFAFA`
* Imagen centrada con fondo gris claro (`#F5F5F5`) y bordes redondeados suaves
* **Título:** “Mochila”, Poppins Bold, `#212121`
* **Descripción:** Texto justificado, `#424242`
* **Botón "Realizar otra vez":**

  * Fondo negro, texto blanco, border-radius `1.23rem`, sombra suave
* **Navegación inferior:** ícono de escanear activo

### Responsive Design:

* Todos los elementos escalables y con touch targets adecuados

---

## Pantalla de historial

**Imágenes:** `frontend\design\Assets-Resources\Pantallas de alta fidelidad\6.1. Pantalla de historial de identificaciones.pdf`
**Imágenes:** `frontend\design\Assets-Resources\Pantallas de alta fidelidad\6.2. Pantalla de historial de no identificaciones.pdf`

### Elementos de interfaz finalizados:

* Fondo: `#FAFAFA`
* Encabezado: “Historial”, Poppins Bold, `#212121`, alineado a la izquierda
* Filtros tipo “pill”:

  * Activo: fondo negro, texto blanco
  * Inactivo: borde gris claro, texto gris
* Lista: miniatura circular, título, fecha, descripción, separador
* Indicador de “no identificado”: punto rojo

### Navegación inferior:

* Ícono “Historial” activo (`#E91E63`)

---

## Pantalla de configuración

**Imágenes:** `frontend\design\Assets-Resources\Pantallas de alta fidelidad\7.1. Pantalla de Configuración.pdf`


**Imágenes:** `frontend\design\Assets-Resources\Pantallas de alta fidelidad\7.2. Pantalla de lenguajes.pdf`

**Imágenes:** `frontend\design\Assets-Resources\Pantallas de alta fidelidad\7.3. Pantalla de privacidad.pdf`

### Elementos de interfaz finalizados:

* Fondo: `#FAFAFA`
* Encabezado: “Configuración”, centrado, Poppins Bold
* Botón de regreso (ícono flecha a la izquierda)
* **Opciones de configuración:**

  * Fila individual con fondo blanco
  * Divisiones finas (`#E0E0E0`), íconos y textos alineados
  * Altura mínima: `3.5rem` para accesibilidad
  * los switches usan estilo verde brillante
---


### Elementos Visuales

Colores:

* Primarios: #E91E63 (magenta), #000000 (negro), #FAFAFA (fondo)

* Secundarios: #757575, #424242, #E0E0E0, #F5F5F5

* Estados:

  * Éxito: #4CAF50
  * Error: #F44336
  * Advertencia: #FF9800
  * Info: #2196F3

### Tipografía:

* Fuente: Poppins (Regular, Bold, Semibold)

* Tamaños:

  *  H1: 1.6–2rem

  * H2: 1.4–1.6rem

  * Párrafo: 1rem–1.23rem

  * Botón: 0.85–1rem

  * Interlineado: 1.4–1.6x

  * Tracking: 0.25–0.5 px

### Componentes UI:

* Botones: primarios (negro), secundarios (borde magenta)

* Inputs: idioma, switches, ayuda

* Tarjetas: resultados con imagen, sombra y padding

* Indicadores: barra de carga, feedback post-captura

* Navegación inferior: íconos con etiquetas

### Espaciado y Dimensiones:

* Espaciado base: múltiplos de 4px (4, 8, 16, 24, 32)

* Margen general: 16–24px

* Padding interno: 12–16px

* Botón mínimo: 48px altura

* Miniaturas: 40–50px
---

# La estructura de navegación 

https://github.com/eduardo-griffith-utp/DESARROLLO_V_SIVM/blob/b5abdbe5c404bd75f74fd48f28136752b4a4773c/frontend/design/Assets-Resources/Estructura%20de%20Navegacion/Flujo%20Visual%20de%20la%20estructura%20de%20navegacion.png

---
# Decisiones de diseño importantes 

- Decisiones de diseño importantes para las pantallas de VisioAI 


- Diseño simple y fácil de usar: 

Queríamos que la aplicación fuera clara desde el primer momento. Por eso, cada pantalla muestra solo lo necesario, con un estilo limpio, sin cosas que distraigan. Así, el usuario puede enfocarse en lo que realmente importa: identificar elementos con la cámara. 

 
- Colores que guían al usuario 

Usamos colores bien pensados: 

El rosa fuerte (#E91E63) destaca lo más importante: botones, iconos activos, acciones clave. 

El morado (#9C27B0) acompaña sin quitar protagonismo. 

Grises para los textos, con buen contraste para que se lean bien. 

Esto ayuda a que el usuario sepa rápidamente qué puede tocar y qué está viendo. 

- Navegación que se entiende sola: 

Agregamos una barra con íconos y nombres en la parte de abajo, para que el usuario sepa dónde está y cómo moverse sin perderse. El icono que esté activo cambia de color para que sea muy evidente en qué parte de la app está. 

- Cada pantalla tiene un propósito 

No quisimos hacer pantallas confusas. Cada una tiene una función clara: 

Capturar imagen 

Ver resultados 

Revisar detalles 

Ver historial, etc. 

Esto evita confusión y ayuda a que la persona complete lo que vino a hacer sin dar vueltas innecesarias. 

- Botones grandes y fáciles de tocar: 

Todos los botones son cómodos para usar con el dedo. Además, cambian de apariencia cuando están activos, deshabilitados o presionados, para que el usuario siempre sepa si están disponibles o no. 

- Se adapta a diferentes pantallas: 

La app está pensada para que funcione bien tanto en celulares como en tablets. Todo se ajusta para que no se vea apretado ni desordenado, sin importar el tamaño de la pantalla. 

Flujo natural entre pantallas: Después de tomar una foto, se ve el resultado. Si no es lo que se esperaba, se puede volver a capturar fácilmente. Todo fluye sin interrupciones, para que el usuario no se pierda y pueda usar la app sin complicaciones. 

---
# Enlaces al prototipo interactivo 

https://www.figma.com/proto/uWHAEIvNdkl8BlV4baSFiU/Untitled--Copia-?page-id=2081%3A6&node-id=2081-616&p=f&viewport=295%2C192%2C0.62&t=kFbBVrV403VuWTNe-1&scaling=min-zoom&content-scaling=fixed&starting-point-node-id=2081%3A616