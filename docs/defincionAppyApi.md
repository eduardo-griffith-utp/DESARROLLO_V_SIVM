Estas son las definiciones necesarias que por el momento tenemos en la APP y API.

Definiciones necesarias para la API (Backend)

1. Endpoints de la API
POST /upload: Recibe una imagen cargada desde la app.

POST /capture: Recibe una imagen capturada desde la cámara.

GET /analysis/{image_id}: Devuelve el resultado del análisis (etiquetas, descripciones, etc.).

GET /multimedia/{tag}: Devuelve recursos multimedia relacionados a una etiqueta.

POST /auth/login: Autenticación de usuarios.

POST /auth/register: Registro de usuarios.


2. Estructura de la Base de Datos
Usuarios: ID, nombre, correo, contraseña encriptada, rol.

Imágenes: ID, usuario_id, ruta_archivo, fecha_subida.

Etiquetas: ID, nombre.

Análisis: ID, imagen_id, etiqueta_id, precisión, descripción.

Recursos Multimedia: ID, tipo (texto, imagen, audio), etiqueta_id, contenido, URL.


3. Servicios Internos
Servicio de reconocimiento de imágenes: puede integrarse con una API externa (como Google Vision o una red neuronal propia).

Servicio de autenticación y permisos: control de acceso a funciones específicas.

Almacenamiento multimedia: integración con disco local, Firebase Storage, Amazon S3 u otro sistema.

Definiciones necesarias para la App Móvil
1. Pantallas Clave
Pantalla de inicio de sesión / registro

Pantalla principal: opción de capturar o subir imagen.

Pantalla de resultados: visualización de elementos identificados.

Pantalla de multimedia: muestra texto, imágenes o audio relacionados con lo identificado.

Historial de imágenes analizadas (opcional).

2. Permisos del dispositivo
Acceso a cámara.

Acceso a galería (almacenamiento).

Acceso a internet.

(Opcional) Permisos de audio si se va a reproducir contenido auditivo.

3. Conexión con la API
Usar métodos fetch, axios o similar para interactuar con la API backend.

Manejo de JWT o tokens para autenticación.

Validaciones al subir o capturar imágenes.

4. Librerías recomendadas
Para cámara: react-native-camera / expo-camera (si usas React Native).

Para cargar imágenes: react-native-image-picker.

Para reproducir audio: react-native-sound o expo-av.

Para gestión de estado: Redux, Context API o MobX.




# Sistema de Identificación Visual Multimedia (SIVM) – API Backend

---

## 🔌 Endpoints RESTful

### 📂 Carga y captura de imágenes

**POST /api/images/upload**  
_Carga una imagen desde galería o dispositivo._
```http
Body: multipart/form-data (campo "image")
```

**POST /api/images/capture**  
_Recibe una imagen capturada desde la cámara._  
```http
Body: multipart/form-data (campo "image")
```

---

### 🔍 Análisis e identificación

**GET /api/analysis/{image_id}**  
_Devuelve el resultado del análisis de una imagen._

**GET /api/multimedia/{tag}**  
_Devuelve contenido multimedia relacionado con una etiqueta._

---

### 🔐 Autenticación y usuarios

**POST /api/auth/login**  
_Inicia sesión de usuario._
```json
{
  "email": "usuario@ejemplo.com",
  "password": "123456"
}
```

**POST /api/auth/register**  
_Registra un nuevo usuario._
```json
{
  "name": "Juan Pérez",
  "email": "juan@ejemplo.com",
  "password": "123456"
}
```

---

## 🧱 Estructura de la Base de Datos (MySQL)

### 🧑‍💼 Tabla: Usuarios
```sql
CREATE TABLE Usuarios (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100),
  email VARCHAR(100) UNIQUE,
  contraseña VARCHAR(255),
  rol ENUM('admin', 'usuario'),
  creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 🖼️ Tabla: Imágenes
```sql
CREATE TABLE Imagenes (
  id INT PRIMARY KEY AUTO_INCREMENT,
  usuario_id INT,
  ruta_imagen TEXT,
  fecha_subida TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (usuario_id) REFERENCES Usuarios(id)
);
```

### 🏷️ Tabla: Etiquetas
```sql
CREATE TABLE Etiquetas (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100)
);
```

### 🧪 Tabla: Análisis
```sql
CREATE TABLE Analisis (
  id INT PRIMARY KEY AUTO_INCREMENT,
  imagen_id INT,
  etiqueta_id INT,
  precision DECIMAL(5,2),
  descripcion TEXT,
  FOREIGN KEY (imagen_id) REFERENCES Imagenes(id),
  FOREIGN KEY (etiqueta_id) REFERENCES Etiquetas(id)
);
```

### 📚 Tabla: Recursos Multimedia
```sql
CREATE TABLE RecursosMultimedia (
  id INT PRIMARY KEY AUTO_INCREMENT,
  etiqueta_id INT,
  tipo ENUM('texto', 'imagen', 'audio'),
  contenido TEXT,
  url TEXT,
  FOREIGN KEY (etiqueta_id) REFERENCES Etiquetas(id)
);
```

---

## ⚙️ Servicios Internos

### 1. 📸 Servicio de Reconocimiento de Imagen (Google Cloud Vision)

```js
// recognitionService.js
const vision = require('@google-cloud/vision');

async function analizarImagen(ruta) {
  const client = new vision.ImageAnnotatorClient();
  const [result] = await client.labelDetection(ruta);
  const labels = result.labelAnnotations;

  return labels.map(label => ({
    nombre: label.description,
    precision: label.score
  }));
}

module.exports = { analizarImagen };
```

---

### 2. 🔐 Servicio de Autenticación (con JWT y bcrypt)

```js
// authService.js
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');

async function login(email, password, db) {
  const usuario = await db.getUsuarioPorEmail(email);
  if (!usuario || !(await bcrypt.compare(password, usuario.contraseña))) {
    throw new Error('Credenciales inválidas');
  }

  const token = jwt.sign({ id: usuario.id, rol: usuario.rol }, 'SECRET_KEY', {
    expiresIn: '2h'
  });

  return { token, usuario };
}

module.exports = { login };
```

---

### 3. 🗂 Servicio de Almacenamiento de Archivos

```js
// storageService.js
const fs = require('fs');
const path = require('path');

function guardarArchivo(file) {
  const rutaDestino = path.join(__dirname, '../uploads', file.originalname);
  fs.writeFileSync(rutaDestino, file.buffer);
  return rutaDestino;
}

module.exports = { guardarArchivo };
```

---

