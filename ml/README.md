# Creacion de modelo con Tensorflow, con un modelo base desde 0.

01 de mayo, creando otro codigo desde 0 con python. A.S.

## OBJETIVOS ##
Para empezar, siento que al generar un codigo desde 0 con documentacion de lo mas esecencial para entrenar 
un modelo con tensorflow ( data_loading, model, train) me va a ayudar a comprender como funciona y darle un uso en la vida real(trabajo).

## REQUERIMIENTOS##
Version de python requerida 3.10.0 https://www.python.org/downloads/release/python-3100/
Repositorio del codigo: https://github.com/gravitax7/clasificador-tensorflow
(A la fecha de hoy, la rama main esta actualizada con los ultimos cambios, de igual forma siempre revisar la de "version-preliminar")

##INSTRUCCIONES##
(Ya esta el modelo creado y entrenado, por lo cual no es necesario ejecutar el proceso de entrenamiento, estas instrucciones son mas bien para darle uso a la prediccion
en base a las clases de imagenes brindadas por el grupo de contenido)


        -- Crear y activar un entorno virtual (opcional pero recomendado) con los siguientes scripts
        python -m venv venv
        venv\Scripts\activate

        -- Instalar todas las dependencias del proyecto
        pip install -r requirements.txt

        -- Preparar la imagen a procesar
        Si no existe, crea el archivo imagen.txt dentro de la carpeta src/.

        -- Configurar la ruta del archivo imagen.txt
        Abre el archivo src/predict_b64.py y verifica que la función with open() tenga la ruta correcta.
        Convierte la imagen que quieres procesar a formato Base64
        Copia el código Base64 generado y reemplaza su contenido dentro de src/imagen.txt.

        -- Ejecutar clase con el siguiente comando para obtener la predidccion:
        python src/predict_b64.py

        -- Revisar el json generado en la carpeta output


## ESTRUCTURA ##

Tensorf_desde0/
│
├── data/                # Directorio de imagenes para el entrenamiento del modelo
│   └── raw/             # Subcarpetas con las distintas clases
│   
├── output/                # Directorio de salida donde se guarda el json del resultado
│   └── resultado.json/             # respuesta de la prediccion con las clases y confianza
|
│
├── src/                 # Código fuente
│   ├── __init__.py
│   ├── data_loading.py  # Clases/funciones para cargar datos
│   ├── model.py         # Definición del modelo
│   ├── prediccion.py    # Distintos metodos para mostrar la prediccion con el porcentaje de confianza
│   ├── predict_b64.py   # *****Clase principal para el proyecto, devuelve la prediccion en formato json para imagenes base 64****
│   ├── retrain.py       # Rentrena el modelo
│   └── train.py         # Entrenamiento del modelo convolucional y creacion de diccionarios/metadata de las clases y del modelo
│
├── models/              # Modelos guardados
│   └── best_model.h5    # Modelo CNN entrenado
│
├── resultado.json       # Contiene el resultado de la prediccion y confianza
├── requirements.txt     # Dependencias del proyecto ( instalar en el entorno virtual)
└── README.md            # Documentación

Texto de desmostracion del json "resultado.json":
[
    {
        "PANDA": 0.9997
    },
    {
        "OSO POLAR": 0.0002
    },
    {
        "SILLA": 0.0001
    },
    {
        "RELOJ": 0.0
    },
    {
        "CRISTO REDENTOR": 0.0
    }
]



## Integrantes del grupo de ML/ I.A.
## Alvan Samudio
## Jose Ariano
