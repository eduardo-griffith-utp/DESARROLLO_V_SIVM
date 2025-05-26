# Componentes del Sistema – API de Reconocimiento de Imágenes

## 1. Cliente

**Función Principal:**  
Interfaz de interacción para el usuario. Permite capturar imágenes, enviarlas al servicio y mostrar los resultados del análisis.

**Límites de Responsabilidad:**  
- No procesa datos.  
- No almacena información persistente.  
- No accede directamente a la base de datos.

**Dependencias:**  
- Servicio: para enviar solicitudes y recibir resultados.

---

## 2. Servicio

**Función Principal:**  
Gestiona la lógica de negocio. Orquesta el flujo de datos entre Cliente, Base de Datos y los Módulos de Reconocimiento.

**Límites de Responsabilidad:**  
- No realiza análisis multimedia.  
- No contiene datos persistentes.  
- No genera la interfaz del usuario.

**Dependencias:**  
- Cliente: recibe solicitudes.  
- Base de Datos: lee y guarda información.  
- Reconocimiento de Contenido: solicita análisis.  
- Resultado Explícito: interpreta resultados del análisis.

---

## 3. Base de Datos (BD)

**Función Principal:**  
Almacena de forma estructurada y persistente toda la información del sistema, incluyendo imágenes, resultados y metadatos.

**Límites de Responsabilidad:**  
- No realiza análisis ni interpretación.  
- No interactúa con el cliente.

**Dependencias:**  
- Servicio: recibe instrucciones para leer y escribir.

---

## 4. Reconocimiento de Contenido

**Función Principal:**  
Analiza las imágenes (u otros datos multimedia) mediante algoritmos o servicios de IA para identificar su contenido.

**Límites de Responsabilidad:**  
- No guarda datos ni toma decisiones de negocio.  
- No tiene interacción directa con usuarios.

**Dependencias:**  
- Servicio: recibe datos a analizar.  
- Resultado Explícito: entrega resultados técnicos.

---

## 5. Resultado Explícito

**Función Principal:**  
Interpreta los resultados del análisis del módulo de reconocimiento, devolviendo etiquetas, niveles de riesgo o alertas NSFW.

**Límites de Responsabilidad:**  
- No realiza análisis directamente.  
- No almacena información.  
- No interactúa con el cliente.

**Dependencias:**  
- Reconocimiento de Contenido: recibe análisis.  
- Servicio: entrega los datos procesados finales.

---

## Definición/Selección de Componentes de Control de Contenido


---

### APIs Evaluadas

1. **Google Vision AI**
   - Ofrece la función SafeSearch para detectar contenido para adultos, violento o sugestivo.
   - Permite hasta 1,000 imágenes gratuitas por mes.
   - Requiere cuenta de Google Cloud y tarjeta de crédito.
   - Costo: $1.50 por cada 1,000 imágenes procesadas.
   - Ideal si ya se trabaja con GCP.

2. **Amazon Rekognition**
   - Detecta contenido sexual, violento o inapropiado en imágenes y videos.
   - Ofrece 5,000 imágenes y 60 minutos de video gratis por mes durante 12 meses.
   - Requiere cuenta de AWS y tarjeta de crédito.
   - Costo: $0.001 por imagen.
   - Muy económico y escalable.

3. **Azure AI Content Safety**
   - Detecta contenido sexual, de odio, violencia y autolesiones.
   - Incluye niveles de severidad.
   - Ofrece 5,000 transacciones gratuitas al mes.
   - Requiere cuenta de Microsoft Azure y tarjeta de crédito.
   - Costo: $1.50 por 1,000 imágenes.
   - Recomendado si se necesita evaluación más detallada.

4. **Clarifai**
   - Tiene modelos preentrenados para detectar contenido NSFW.
   - Ofrece un plan gratuito con 30,000 operaciones mensuales.
   - No requiere tarjeta de crédito para comenzar.
   - Ideal para prototipos, pruebas o entornos educativos sin presupuesto.

---

### Requisitos Técnicos Comparados

- Todas las APIs requieren crear una cuenta.
- Google, Amazon y Azure requieren tarjeta de crédito para habilitar el servicio.
- Clarifai no requiere tarjeta de crédito.
- Todas las APIs requieren configuración de claves o autenticación.
- Todas permiten escalabilidad y uso en tiempo real.

---


Se recomienda utilizar **Clarifai** como componente para el control de contenido en la arquitectura del sistema. Sus ventajas principales son:

- No requiere tarjeta de crédito.
- Plan gratuito amplio de 30,000 operaciones mensuales.
- Fácil de integrar y probar en entornos educativos o de laboratorio.

Como segunda opción, si se necesita detección más precisa con niveles de severidad, **Azure AI Content Safety** es una buena alternativa, aunque requiere tarjeta de crédito.

---


