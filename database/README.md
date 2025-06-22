# Base de Datos del Sistema de Identificación Visual Multimedia (SIVM)

Esta carpeta contiene los scripts, migraciones y documentación relacionada con la base de datos del proyecto SIVM, responsable del almacenamiento persistente de información y referencias a contenido multimedia.

## Tecnologías Utilizadas

* **Sistema de Base de Datos:** MariaDB
* **ORM/ODM:** SQLAlchemy (usado para la conexión desde Python)
* **Herramientas de Migración:** Scripts SQL generados en DBeaver
* **Herramientas de Backup:** Funcionalidades de exportación de MariaDB y Digital Ocean
* **Versionado de Esquema:** Manual a través de scripts SQL y gestión en DBeaver

## Modelo de Datos

### Entidades Principales

#### MediaContent

* id\_media\_content, int, Primary key
* item\_id, int, Foreign key
* route\_path, varchar
* type, varchar
* description, varchar
* date\_uploaded, datetime

#### AnalysisResult

* id\_analysis\_result, int, Primary key
* item\_id, int, Foreign key
* analysis\_id, int, Foreign key
* detected\_labels, varchar
* date\_analysis, datetime
* status, varchar

#### Analysis

* id\_analysis , int , Primary key
* input\_image\_path, varchar
* timestamp datetime
* status, varchar
* processing\_time, datetime
* source, varchar

#### Item

* id\_item, int, Primary key
* item\_tag\_id, int, Foreign key
* name, varchar
* description, text

#### ItemTag

* id\_tag, int, Primary key
* tag\_name, varchar

### Relaciones

**1. Item → ItemTag**
Relación: Muchos a Uno
Clave foránea: item\_tag\_id en Item
Descripción: Cada ítem pertenece a una etiqueta (ItemTag), pero una etiqueta puede estar asociada a múltiples ítems.

**2. MediaContent → Item**
Relación: Muchos a Uno
Clave foránea: item\_id en MediaContent
Descripción: Cada contenido multimedia pertenece a un ítem específico. Un ítem puede tener múltiples contenidos multimedia asociados.

**3. AnalysisResult → Item**
Relación: Muchos a Uno
Clave foránea: item\_id en AnalysisResult
Descripción: Cada resultado de análisis está asociado a un ítem. Un ítem puede tener varios análisis realizados.

**4. AnalysisResult → Analysis**
Relación: Muchos a Uno
Clave foránea: analysis\_id en AnalysisResult
Descripción: Un resultado de análisis proviene de una ejecución de análisis (Analysis). Un análisis puede generar múltiples resultados (aunque usualmente es uno a uno).

**5. Analysis**
No tiene claves foráneas salientes, pero sí recibe referencias desde AnalysisResult. Se puede considerar que se relaciona indirectamente con Item a través de la ruta de imagen.

## Configuración del Entorno

### Requisitos Previos

* Python 3.10 o superior
* MariaDB instalado localmente o acceso a instancia remota (por ejemplo, en Digital Ocean)
* DBeaver (opcional, para diseño y ejecución visual de consultas SQL)
* Entorno virtual Python (recomendado)
* Conexión a la base de datos mediante mysql-connector-python o SQLAlchemy
* Acceso a variables de entorno para proteger las credenciales de la base de datos

### Configuración Inicial

```bash
# Creación de la base de datos
CREATE DATABASE IF NOT EXISTS desarrollov_app;
USE desarrollov_app;
```

**Script de creación de tablas:** Ver archivo `script-data/create_tables.sql`

**Script de inserción de datos reales:** Ver archivo `script-data/insert_data.sql`

**Script de datos dummy:** Ver archivo `script-data/datos_dummy.sql`

**Ejecución general:** Ver archivo `main.sql` para correr los scripts anteriores en orden.

### Crear una Nueva Migración

```bash
# Crear nuevo archivo SQL con la estructura de tablas
nano estructura_tablas.sql
```

### Ejecutar Migraciones

```bash
# Usando la terminal de MySQL o desde DBeaver
mysql -u tu_usuario -p -h tu_host -D nombre_base_datos < main.sql
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

Para cargar datos de prueba:

```bash
# Ejecutar script de datos dummy
mysql -u tu_usuario -p nombre_base_datos < script-data/datos_dummy.sql
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

* Uso de índices en columnas como id\_item, date\_uploaded, date\_analysis.
* Evitar redundancias y normalizar los datos.
* Evitar SELECT \*, usar solo los campos necesarios.
* Eliminar datos no utilizados después de cierto tiempo.
* Considerar almacenamiento externo (como S3) para archivos multimedia pesados.

## Convenciones de Nomenclatura

* Tablas en minúsculas y plural: items, itemtags, mediacontent, analysis, analysisresult
* Claves primarias con prefijo: id\_item, id\_tag, etc.
* Claves foráneas con el mismo nombre que el campo primario al que apuntan
* Uso de snake\_case para todos los campos
* Campos de tipo fecha en formato: date\_uploaded, date\_analysis, etc.

## Equipo de Base de Datos

* Cesar Castillo
* Javett Pineda C.
* Ricardo Copriz
* Enedina Ortega
* Ricardo Abrego
* Luis Gómez

## Recursos Adicionales

* Por el momento no tenemos recursos adicionales.
