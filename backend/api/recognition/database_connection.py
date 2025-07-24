import mariadb
import configparser
from datetime import datetime
import json
#import os

class MariaDBConnection:

    def __init__(self):
        archivo_ini='recognition/config.ini'

        #path = os.path.abspath('config.ini')
        #print(f'Leyendo desde: {path}')
        #print(os.path.exists(path))
        try: 
            self.config = configparser.ConfigParser()
            self.config.read(archivo_ini)
            self.conn = None
        except Exception as e:
            print(e)
    #def conectar(self):
        try:
            db_conf = self.config['database']
            self.conn = mariadb.connect(
                host=db_conf.get('host'),
                port=int(db_conf.get('port')),
                user=db_conf['user'],
                password=db_conf['password'],
                database=db_conf['database']
            )
            print("Conexión exitosa a MariaDB.")
            #return self.conn
        except mariadb.Error as e:
            print(f"Error al conectar con MariaDB: {e}")
            #return None

    def cerrar(self):
        if self.conn:
            now = datetime.now()
            self.conn.close()
            print(f"{now}     Conexión cerrada.")

    def insert_into_analysis(self,image_path):
        insert = f"""INSERT INTO Analysis (input_image_path, timestamp, status, processing_time)
        VALUES ('{image_path}',NOW(),'PROCESSING',NOW());"""
        result = self.execute_sql(insert, image_path)
        # Retornar el lastrowid directamente como ID numérico
        return result if result != -1 else None
       

    def insert_into_analysis_result(self,image_path):
        insert = f"""INSERT INTO Analysis (input_image_path, timestamp, status, processing_time)
        VALUES ('{image_path}',NOW(),'PROCESSING',NOW());"""
        return self.execute_sql(insert,image_path)
        

    def insert_into_item(self, item_tag_id, item_name, item_description):
        insert = f"INSERT INTO Item (item_tag_id, name, description) VALUES ({item_tag_id}, '{item_name}', '{item_description}')"
        return self.execute_sql(insert, item_name+" en table ITEM")


    def insert_into_item_tag(self, tag_name):
        insert = f"""INSERT INTO ItemTag (tag_name) VALUES('{tag_name}');"""
        return  self.execute_sql(insert,tag_name + " en Tabla ItemTag" )
        

    def insert_into_media_content(self, item_id, route_path, type, description): 
        insert = f"""INSERT INTO MediaContent (item_id, route_path, type, description, date_uploaded) 
        VALUES ({item_id}, '{route_path}', '{type}', '{description}', NOW());"""
        return self.execute_sql(insert, route_path + " en Tabla MediaContent" )

    def get_analysis_by_image_id(self, image_id):
        """
        Obtiene el análisis de una imagen específica por su ID
        Convierte el image_id formato 'img_xxxxxxxx' a ID numérico para buscar en la BD
        """
        try:
            # Extraer el ID numérico del formato img_xxxxxxxx
            if image_id.startswith('img_'):
                numeric_id = int(image_id[4:], 16)  # Convierte de hexadecimal a decimal
            else:
                return None
            
            # Query para obtener los datos del análisis usando el ID numérico
            query = """
            SELECT 
                id,
                input_image_path,
                timestamp,
                status,
                processing_time
            FROM Analysis 
            WHERE id = %s
            """
            
            result = self.execute_sql_select_one(query, (numeric_id,))
            
            if result:
                # Procesar el resultado para formato de respuesta
                analysis_data = {
                    "image_id": image_id,  # Mantener el formato original
                    "database_id": result[0],  # ID numérico de la base de datos
                    "image_path": result[1],
                    "timestamp": result[2].isoformat() if result[2] else None,
                    "status": result[3],
                    "processing_time": result[4].isoformat() if result[4] else None,
                    "analysis": {
                        "message": "Análisis encontrado en la base de datos",
                        "found": True,
                        "details": {
                            "original_numeric_id": numeric_id,
                            "converted_from": image_id
                        }
                    }
                }
                
                return analysis_data
            else:
                return None
                
        except Exception as e:
            print(f"Error getting analysis by image_id: {e}")
            return None

    def execute_sql(self,sql,dato):
        now = datetime.now()
        try:
            #print(insert)
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            last_id = cursor.lastrowid
            cursor.close()
            print(f"{now}   {dato} insertado correctamente")
            return last_id
        except mariadb.Error as e:
            print(f"{now}   error al insertar en {dato} \n{e}")
            return -1

    def execute_sql_select(self,sql):
        now = datetime.now()
        try:
            #print(insert)
            cursor = self.conn.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            return results
        except mariadb.Error as e:
            print(f"{now}   error al consultar \n{e}")
            return None

    def execute_sql_select_one(self, sql, params=None):
        """
        Ejecuta una consulta SELECT y retorna un solo resultado
        """
        now = datetime.now()
        try:
            cursor = self.conn.cursor()
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            result = cursor.fetchone()
            cursor.close()
            return result
        except mariadb.Error as e:
            print(f"{now}   error al consultar \n{e}")
            return None