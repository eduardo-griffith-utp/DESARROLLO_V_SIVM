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
ATRIBUTO , TIPO DE DATOS , TIPO DE LLAVE  
-Id_image , int , Primary key  
- route_imagen , varchar ,   
- date_uploaded , datetime ,   

#### Resultados de Análisis
ATRIBUTO , TIPO DE DATOS , TIPO DE LLAVE  
- Id_image , int , Primary key  
- route_imagen , varchar ,   
- date_uploaded , datetime ,   

#### Contenido Multimedia
ATRIBUTO , TIPO DE DATOS , TIPO DE LLAVE  
- Id_multimedia , int , Primary key  
- Imagen_ID , int , Foreing key  
- type_content  , varchar ,   
- description , varchar ,   
- file_path , varchar ,   - id_contenido (PK)

#### Usuarios 
ATRIBUTO , TIPO DE DATOS , TIPO DE LLAVE  
- Id_User , int , Primary key  
- name_user , varchart ,   

### Historial de Consultas
ATRIBUTO , TIPO DE DATOS , TIPO DE LLAVE  
- Id_querys , int , Primary key 
- Image_ID , int , Foreing Key  
- date_consultation , datetime ,   
- counter , int ,   

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
# primero debemos crear la base de datos

create database desarrollov_app;

# una vez creada la base de datos procedemos a crear la estructura de las tablas

create table if not exists Session(
	id_session int primary key not null,
	name_session varchar(20)
);


create table if not exists MediaContent(
	id_media int primary key not null,
	user_id int not null,
	route_path varchar(64),
	type_content varchar(30),
	description varchar(50),
	date_uploaded datetime not null
);

create table if not exists AnalysisResult(
	id_results int primary key not null,
	media_is int not null,
	detected_labes varchar(50),
	date_analysis datetime not null
);

create table if not exists QueryHistory(
	id_query int primary key not null,
	media_id int not null,
	date_consultation datetime not null,
	counter int not null
);

create table if not exists Items(
	id_items int primary key not null,
	media_id int not null,
	name varchar(30) not null,
	description text not null
);

create table if not exists ItemTags(
	id_tag int primary key not null,
	item_id int not null,
	tag_name varchar(30) not null
);


# una vez creada la estructura procedemos a crear las llaves foraneas

alter table mediacontent 
add constraint fk_mediacontent_session
foreign key (user_id) references Session(id_session); 

alter table analysisresult  
add constraint fk_analisysresults_mediacontent
foreign key (media_is) references MediaContent(id_media); 

alter table queryhistory  
add constraint fk_queryhistory_mediacontent
foreign key (media_id) references MediaContent(id_media) ;

alter table items 
add constraint fk_items_mediacontent
foreign key (media_id) references MediaContent(id_media);

alter table ItemTags 
add constraint fk_itemtags_items
foreign key (item_id) references items(id_items) ;


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
- 
- [Integrante 3]
- [Integrante 4]

## Recursos Adicionales

- Por el momento no tenemos recursos adicionales.