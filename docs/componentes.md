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
