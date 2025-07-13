import mariadb
import configparser
from datetime import datetime
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
        return self.execute_sql(insert, image_path)
       

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

    def execute_sql(self,sql,dato):
        now = datetime.now()
        try:
            #print(insert)
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            return cursor.lastrowid
            print(f"{now}   {dato} insertado correctamente")
        except mariadb.Error as e:
            print(f"{now}   error al insertar en {dato} \n{e}")
            return -1

    def execute_sql_select(self,sql):
        now = datetime.now()
        try:
            #print(insert)
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
           
        except mariadb.Error as e:
            print(f"{now}   error al consultar \n{e}")