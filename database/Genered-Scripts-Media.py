import os
from datetime import datetime

BASE_PATH = "C:/Users/CESAR/Documents/Desarrollo V/DESARROLLO_V_SIVM/assets/storage_structure/training_data"

# Mapeo de nombres de ítem a IDs basado en Item.sql
ITEM_MAPPING = {
    'CANGURO': 1,
    'CRISTO_REDENTOR': 2,
    'CUBIERTO': 3,
    'DELFIN': 4,
    'ELEFANTE': 5,
    'ESTATUA_DE_LA_LIBERTAD': 6,
    'JIRAFA': 7,
    'KOALA': 8,
    'LAPTOP': 9,
    'LENTES': 10,
    'LEON': 11,
    'LIBRO': 12,
    'LLAVE': 13,
    'MOUSE': 14,
    'OSO_POLAR': 15,
    'PANDA': 16,
    'PARAGUA': 17,
    'PEZ_PAYASO': 18,
    'PUENTE_CENTENARIO': 19,
    'RINOCERONTE': 20,
    'ROD_CAREW_ESTADIO': 21,
    'SMARTPHONE': 22,
    'TAZA': 23,
    'TIGRE': 24,
    'TORRE_EIFFEL': 25,
    'VENTILADOR': 26,
    'VOLCAN_BARU': 27
}

def infer_type(file_name):
    ext = os.path.splitext(file_name)[1].lower()
    if ext in [".jpg", ".jpeg", ".png", ".bmp", ".gif"]:
        return "image"
    elif ext in [".mp4", ".mov", ".avi"]:
        return "video"
    else:
        return "unknown"

def sanitize_sql(text):
    """Escape comillas simples para SQL"""
    return text.replace("'", "''")

def get_item_id(category_name):
    formatted_name = category_name.upper().replace(' ', '_')
    return ITEM_MAPPING.get(formatted_name, None)

sql_lines = []

for category in os.listdir(BASE_PATH):
    category_path = os.path.join(BASE_PATH, category)
    if os.path.isdir(category_path):
        item_id = get_item_id(category)
        if item_id is None:
            print(f"Advertencia: No se encontró ID para '{category}'. Omitiendo...")
            continue
            
        for file_name in os.listdir(category_path):
            full_path = os.path.join(category_path, file_name)
            if os.path.isfile(full_path):
                route_path = full_path.replace("\\", "/")
                media_type = infer_type(file_name)
                description = sanitize_sql(f"{category} - {file_name}")
                date_uploaded = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                insert_sql = f"""INSERT INTO MediaContent (item_id, route_path, type, description, date_uploaded)
VALUES ({item_id}, '{route_path}', '{media_type}', '{description}', '{date_uploaded}');"""

                sql_lines.append(insert_sql)

# Guardar en archivo .sql con formato correcto
with open("Insert_MediaContent.sql", "w", encoding="utf-8") as f:
    f.write("\n".join(sql_lines))
    # Asegurarse de que no haya espacios/lineas vacías al inicio
    f.write("\n")  # Solo un salto de línea al final