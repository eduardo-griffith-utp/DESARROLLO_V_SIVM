from database_connection import MariaDBConnection

connection = MariaDBConnection()
conn = connection.conectar()

if conn:
    cursor = conn.cursor()
    cursor.execute("SELECT NOW()")  # Consulta de prueba
    for (fecha,) in cursor:
        print("Fecha actual:", fecha)
    
    #connection.insert_into_analysis("training_data/TELEVISOR/img_001.jpg2")
    #connection.insert_into_analysis_result("analysis result")
    #connection.insert_into_item(31,'Prueba De Insert', 'Prueba de Insersción de datos')
    #connection.insert_into_item_tag("item_tag2")
    #connection.insert_into_media_content(1, 'training_data/CANGURO/img_003.jpg', 'image/jpeg', 'Imagen de canguro 3')
    connection.cerrar()

