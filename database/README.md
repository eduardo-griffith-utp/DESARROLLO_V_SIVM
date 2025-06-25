# Base de Datos del Sistema de Identificación Visual Multimedia (SIVM)

Esta carpeta contiene los scripts, migraciones y documentación relacionada con la base de datos del proyecto SIVM, responsable del almacenamiento persistente de información y referencias a contenido multimedia.

## ⚠️ Nota importante:

_Este esquema no es definitivo. Es solo un ejemplo base que servirá como punto de partida, y será modificado y adaptado a medida que el desarrollo del proyecto avance._

## Tecnologías Utilizadas

- **Sistema de Base de Datos:** MariaDB
- **ORM/ODM:** SQLAlchemy (usado para la conexión desde Python)
- **Herramientas de Migración:** Scripts SQL generados en DBeaver
- **Herramientas de Backup:** Funcionalidades de exportación de MariaDB y Digital Ocean
- **Versionado de Esquema:** Manual a través de scripts SQL y gestión en DBeaver

## Modelo de Datos

### Entidades Principales

#### MediaContent

- id_media_content, int, Primary key
- item_id, int, Foreign key
- route_path, varchar
- type, varchar
- description, varchar
- date_uploaded, datetime

#### AnalysisResult

- id_analysis_result, int, Primary key
- item_id, int, Foreign key
- analysis_id, int, Foreign key
- detected_labels, varchar
- date_analysis, datetime
- status, varchar

#### Analysis

- id_analysis , int , Primary key
- input_image_path, varchar
- timestamp datetime
- status, varchar
- processing_time, datetime
- source, varchar

#### Item

- id_item, int, Primary key
- item_tag_id, int, Foreign key
- name, varchar
- description, text

#### ItemTag

- id_tag, int, Primary key
- tag_name, varchar

### Relaciones

**1. Item → ItemTag**

Relación: Muchos a Uno

Clave foránea: item_tag_id en Item

Descripción: Cada ítem pertenece a una etiqueta (ItemTag), pero una etiqueta puede estar asociada a múltiples ítems.

**2. MediaContent → Item**

Relación: Muchos a Uno

Clave foránea: item_id en

Descripción: Cada contenido multimedia pertenece a un ítem específico. Un ítem puede tener múltiples contenidos multimedia asociados.

**3. AnalysisResult → Item**

Relación: Muchos a Uno

Clave foránea: item_id en AnalysisResult

Descripción: Cada resultado de análisis está asociado a un ítem. Un ítem puede tener varios análisis realizados.

**4. AnalysisResult → Analysis**
Relación: Muchos a Uno

Clave foránea: analysis_id en AnalysisResult

Descripción: Un resultado de análisis proviene de una ejecución de análisis (Analysis). Un análisis puede generar múltiples resultados (aunque usualmente es uno a uno).

**5. Analysis**

No tiene claves foráneas salientes, pero sí recibe referencias desde

AnalysisResult. Se puede considerar que se relaciona indirectamente con Item a través de la ruta de imagen.

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
# Creación de la base de datos
CREATE DATABASE IF NOT EXISTS desarrollov_app;
USE desarrollov_app;

# Tabla MediaContent
CREATE TABLE IF NOT EXISTS MediaContent(
    id_media_content INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    item_id INT NOT NULL,
    route_path VARCHAR(255) NOT NULL,
    type VARCHAR(30) NOT NULL,
    description VARCHAR(50),
    date_uploaded DATETIME NOT NULL
);

# Tabla AnalysisResult
CREATE TABLE IF NOT EXISTS AnalysisResult(
    id_analysis_result INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    item_id INT NOT NULL,
    analysis_id int NOT NULL,
    detected_labels VARCHAR(50) NOT NULL,
    date_analysis DATETIME NOT null,
    status varchar(10)
);

# Tabla Analysis
CREATE TABLE IF NOT EXISTS Analysis(
    id_analysis INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    input_image_path varchar(255) NOT NULL,
    timestamp datetime,
    status varchar(15),
    processing_time datetime,
    source varchar(255)
);

# Tabla Items
CREATE TABLE IF NOT EXISTS Item(
    id_item INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    item_tag_id int not null,
    name varchar(30) not null,
    description TEXT NOT NULL
);

# Tabla ItemTags
CREATE TABLE IF NOT EXISTS ItemTag(
    id_tag INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    tag_name VARCHAR(30) NOT NULL
);

# Creacion de llaves foreanas

ALTER TABLE MediaContent
ADD CONSTRAINT fk_mediacontent_item
FOREIGN KEY (item_id) REFERENCES Item(id_item)
ON DELETE CASCADE;

ALTER TABLE Item
ADD CONSTRAINT fk_item_item_tag
FOREIGN KEY (item_tag_id) REFERENCES ItemTag(id_tag)
ON DELETE CASCADE;

ALTER TABLE AnalysisResult
ADD CONSTRAINT fk_analysisresult_item
FOREIGN KEY (item_id) REFERENCES Item(id_item)
ON DELETE CASCADE;

ALTER TABLE AnalysisResult
ADD CONSTRAINT fk_analysisresult_analysis
FOREIGN KEY (analysis_id) REFERENCES Analysis(id_analysis)
ON DELETE CASCADE;

# Restricciones para evitar duplicidad

ALTER TABLE ItemTag
ADD CONSTRAINT uq_itemtag_tag_name UNIQUE (tag_name);

ALTER TABLE Item
ADD CONSTRAINT uq_item_name_per_tag UNIQUE (item_tag_id, name);

ALTER TABLE MediaContent
ADD CONSTRAINT uq_media_route_per_item UNIQUE (item_id, route_path);

ALTER TABLE AnalysisResult
ADD CONSTRAINT uq_analysisresult_item_date UNIQUE (item_id, date_analysis);

ALTER TABLE Analysis
ADD CONSTRAINT uq_analysis_input_image_path UNIQUE (input_image_path);

ALTER TABLE AnalysisResult
ADD CONSTRAINT uq_analysisresult_item_analysis UNIQUE (item_id, analysis_id);

```

### Crear una Nueva Migración

```bash
# Crear nuevo archivo SQL con la estructura de tablas
nano estructura_tablas.sql
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

# Orden correcto: primero las más dependientes, luego las raíces

DROP TABLE IF EXISTS AnalysisResult;
DROP TABLE IF EXISTS MediaContent;
DROP TABLE IF EXISTS Analysis;
DROP TABLE IF EXISTS Item;
DROP TABLE IF EXISTS ItemTag;
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

- Uso de índices en columnas como id_item, date_uploaded, date_analysis.
- Evitar redundancias y normalizar los datos (por ejemplo, etiquetas como campo JSON para evitar múltiples tablas si no hay clasificación compleja).
- Evitar SELECT \*, usar solo los campos necesarios.
- Eliminar imágenes y resultados no utilizados después de cierto tiempo para reducir espacio.
- Considerar almacenamiento externo (como S3) para archivos multimedia pesados y solo guardar las rutas en la base de datos.

## Convenciones de Nomenclatura

- Tablas en minúsculas y plural: imagenes, resultados, contenido_multimedia, historial_consultas
- Claves primarias con prefijo: id_imagen, id_resultado, etc.
- Claves foráneas del mismo nombre que el campo primario al que apuntan
- Uso de snake_case para todos los campos
- Campos de tipo fecha en formato fecha_subida, fecha_consulta, fecha_analisis

## Equipo de Base de Datos

- Cesar Castillo
- Javett Pineda C.
- Ricardo Copriz
- Enedina Ortega
- Ricardo Abrego
- Luis Gómez

## Recursos Adicionales

- Por el momento no tenemos recursos adicionales.
