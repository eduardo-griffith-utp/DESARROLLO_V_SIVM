# Base de Datos del Sistema de Identificación Visual Multimedia (SIVM)

Esta carpeta contiene los scripts, migraciones y documentación relacionada con la base de datos del proyecto SIVM, responsable del almacenamiento persistente de información y referencias a contenido multimedia.


## ⚠️ Nota importante:

*Este esquema no es definitivo. Es solo un ejemplo base que servirá como punto de partida, y será modificado y adaptado a medida que el desarrollo del proyecto avance.*

## Tecnologías Utilizadas

- **Sistema de Base de Datos:** MariaDB
- **ORM/ODM:** SQLAlchemy (usado para la conexión desde Python)
- **Herramientas de Migración:** Scripts SQL generados en DBeaver
- **Herramientas de Backup:** Funcionalidades de exportación de MariaDB y Digital Ocean
- **Versionado de Esquema:** Manual a través de scripts SQL y gestión en DBeaver

## Modelo de Datos

### Entidades Principales

#### Imágenes
id_imagen (PK)
ruta_imagen (texto o URL)
fecha_subida (datetime)

#### Resultados de Análisis
- id_resultado (PK)
- id_imagen (FK → Imágenes)
- etiquetas_detectadas (texto o JSON)
- fecha_analisis (datetime)

#### Contenido Multimedia
- id_contenido (PK)
- tipo_contenido (audio, video, etc.)
- descripcion
- ruta_archivo
- id_imagen (FK → Imágenes)

#### Usuarios (GENERICO)
- id_usuario (PK) → e.g. 1
- nombre_usuario → "anonimo"

### Historial de Consultas
- id_consulta (PK)
- id_imagen (FK → Imágenes)
- fecha_consulta (datetime)
- contador (int) → Representa cuántas veces se ha consultado esa imagen.

### Relaciones

- Cada imagen puede tener varios resultados de análisis y consultas.
- Cada consulta está asociada a una imagen.
- El historial de consultas permite contar y registrar cuándo se hace cada consulta.
- Cada contenido multimedia se asocia a una imagen o directo al resultado.
- Todas las acciones podrían relacionarse con un usuario genérico.

## Configuración del Entorno

### Requisitos Previos
- Python 3.10 o superior
- MariaDB instalado localmente o acceso a instancia remota (por ejemplo, en Digital Ocean)
- DBeaver (opcional, para diseño y ejecución visual de consultas SQL)
- Entorno virtual Python (recomendado)
- Conexión a la base de datos mediante mysql-connector-python o SQLAlchemy
- Acceso a variables de entorno para proteger las credenciales de la base de datos


### Configuración Inicial

```bash
# 1. Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 2. Instalar dependencias necesarias
pip install mysql-connector-python sqlalchemy python-dotenv

# 3. Crear archivo .env con tus credenciales (no subir a GitHub)
touch .env

```

## Migraciones

```bash 
# Crear nuevo archivo SQL con la estructura de tablas
nano crear_tablas.sql

#Este es un ejemplo del contenido de la tabla:

CREATE TABLE imagenes (
    id_imagen INT AUTO_INCREMENT PRIMARY KEY,
    ruta_imagen TEXT NOT NULL,
    fecha_subida DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE resultados (
    id_resultado INT AUTO_INCREMENT PRIMARY KEY,
    id_imagen INT,
    etiquetas_detectadas TEXT,
    fecha_analisis DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_imagen) REFERENCES imagenes(id_imagen)
);

CREATE TABLE contenido_multimedia (
    id_contenido INT AUTO_INCREMENT PRIMARY KEY,
    tipo_contenido VARCHAR(50),
    descripcion TEXT,
    ruta_archivo TEXT,
    id_imagen INT,
    FOREIGN KEY (id_imagen) REFERENCES imagenes(id_imagen)
);

CREATE TABLE historial_consultas (
    id_consulta INT AUTO_INCREMENT PRIMARY KEY,
    id_imagen INT,
    fecha_consulta DATETIME DEFAULT CURRENT_TIMESTAMP,
    contador INT DEFAULT 1,
    FOREIGN KEY (id_imagen) REFERENCES imagenes(id_imagen)
);

```

### Crear una Nueva Migración

```bash
# Crear nuevo archivo SQL con la estructura de tablas
nano crear_tablas.sql
```

### Ejecutar Migraciones

```bash
# Usando la terminal de MySQL o desde DBeaver
mysql -u tu_usuario -p -h tu_host -D nombre_base_datos < crear_tablas.sql
```

### Revertir Migraciones

```bash
# Puedes crear un archivo para eliminar las tablas
nano revertir_tablas.sql

#Ejemplo:

DROP TABLE IF EXISTS historial_consultas;
DROP TABLE IF EXISTS contenido_multimedia;
DROP TABLE IF EXISTS resultados;
DROP TABLE IF EXISTS imagenes;
```

## Datos de Prueba

Para cargar datos iniciales/prueba:

```bash
# Crear archivo de prueba
nano datos_prueba.sql

#Ejemplo:

INSERT INTO imagenes (ruta_imagen) VALUES ('/static/img/ejemplo1.jpg');
INSERT INTO resultados (id_imagen, etiquetas_detectadas) VALUES (1, '["perro", "parque"]');
INSERT INTO historial_consultas (id_imagen, contador) VALUES (1, 1);

```

## Backup y Restauración

### Crear Backup

```bash
# Backup completo de la base de datos
mysqldump -u tu_usuario -p -h tu_host nombre_base_datos > backup.sql
```

### Restaurar desde Backup

```bash
# Restaurar desde archivo de backup
mysql -u tu_usuario -p -h tu_host nombre_base_datos < backup.sql
```

## Optimización y Rendimiento

- Uso de índices en columnas como id_imagen, fecha_subida, y fecha_consulta.
- Evitar redundancias y normalizar los datos (por ejemplo, etiquetas como campo JSON para evitar múltiples tablas si no hay clasificación compleja).
- Evitar SELECT *, usar solo los campos necesarios.
- Eliminar imágenes y resultados no utilizados después de cierto tiempo para reducir espacio.
- Considerar almacenamiento externo (como S3) para archivos multimedia pesados y solo guardar las rutas en la base de datos.

## Convenciones de Nomenclatura

- Tablas en minúsculas y plural: imagenes, resultados, contenido_multimedia, historial_consultas
- Claves primarias con prefijo: id_imagen, id_resultado, etc.
- Claves foráneas del mismo nombre que el campo primario al que apuntan
- Uso de snake_case para todos los campos
- Campos de tipo fecha en formato fecha_subida, fecha_consulta, fecha_analisis

## Equipo de Base de Datos

- Cesar castillo
- [Integrante 2]
- [Integrante 3]
- [Integrante 4]

## Recursos Adicionales

- Por el momento no tenemos recursos adicionales.