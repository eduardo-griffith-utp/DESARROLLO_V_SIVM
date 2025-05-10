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

#### Sesion
ATRIBUTO , TIPO DE DATOS , TIPO DE LLAVE  
- Id_session , int , Primary key  
- name_session , varchar   

#### Contenido Multimedia
ATRIBUTO , TIPO DE DATOS , TIPO DE LLAVE  
- Id_media, int, Primary key
- session_id, int, Foreing key
- route_path, varchar
- type_content, varchar
- description, varchar
- date_uploaded, datetime

#### Resultados Analisis
ATRIBUTO , TIPO DE DATOS , TIPO DE LLAVE  
- Id_results, int, Primary key
- media_id, int, Foreing key
- detected_labes, varchar
- date_analysis, datetime

### Historial de Consultas
ATRIBUTO , TIPO DE DATOS , TIPO DE LLAVE  
- Id_querys , int , Primary key 
- media_id , int , Foreing Key  
- date_consultation , datetime ,   
- counter , int ,   

### Items
ATRIBUTO , TIPO DE DATOS , TIPO DE LLAVE
- Id_items, int, Primary key
- media_id, int, Foreing key
- name, varchar
- description, text

### Item Tags
ATRIBUTO , TIPO DE DATOS , TIPO DE LLAVE
- Id_tag, int, Primary key
- items_id, int, Foreing key
- tag_name, varchar

### Relaciones

- Una sesión puede contener múltiples contenidos multimedia.
- Un contenido multimedia puede tener múltiples resultados de análisis.
- Un contenido multimedia puede ser consultado múltiples veces.
- Un contenido multimedia puede contener múltiples ítems.
- Un ítem puede tener múltiples etiquetas asociadas.

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

# Tabla Session
CREATE TABLE IF NOT EXISTS Session(
    id_session INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    name_session VARCHAR(20) NOT NULL
);

# Tabla MediaContent
CREATE TABLE IF NOT EXISTS MediaContent(
    id_media INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    session_id INT NOT NULL,
    route_path VARCHAR(64) NOT NULL,
    type_content VARCHAR(30) NOT NULL,
    description VARCHAR(50),
    date_uploaded DATETIME NOT NULL
);

# Tabla AnalysisResult
CREATE TABLE IF NOT EXISTS AnalysisResult(
    id_results INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    media_id INT NOT NULL,
    detected_labels VARCHAR(50) NOT NULL,
    date_analysis DATETIME NOT NULL
);

# Tabla QueryHistory
CREATE TABLE IF NOT EXISTS QueryHistory(
    id_query INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    media_id INT NOT NULL,
    date_consultation DATETIME NOT NULL,
    counter INT NOT NULL DEFAULT 1
);

# Tabla Items
CREATE TABLE IF NOT EXISTS Items(
    id_items INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    media_id INT NOT NULL,
    name VARCHAR(30) NOT NULL,
    description TEXT NOT NULL
);

# Tabla ItemTags
CREATE TABLE IF NOT EXISTS ItemTags(
    id_tag INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    items_id INT NOT NULL,
    tag_name VARCHAR(30) NOT NULL
);

# Llaves foráneas corregidas
ALTER TABLE MediaContent 
ADD CONSTRAINT fk_mediacontent_session
FOREIGN KEY (session_id) REFERENCES Session(id_session);

ALTER TABLE AnalysisResult  
ADD CONSTRAINT fk_analysisresult_mediacontent
FOREIGN KEY (media_id) REFERENCES MediaContent(id_media);

ALTER TABLE QueryHistory  
ADD CONSTRAINT fk_queryhistory_mediacontent
FOREIGN KEY (media_id) REFERENCES MediaContent(id_media);

ALTER TABLE Items 
ADD CONSTRAINT fk_items_mediacontent
FOREIGN KEY (media_id) REFERENCES MediaContent(id_media);

ALTER TABLE ItemTags 
ADD CONSTRAINT fk_itemtags_items
FOREIGN KEY (items_id) REFERENCES Items(id_items);


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

- Cesar Castillo
- Javett Pineda C.
- Ricardo Copriz
- Enedina Ortega
- Ricardo Abrego
- Luis Gómez

## Recursos Adicionales

- Por el momento no tenemos recursos adicionales.