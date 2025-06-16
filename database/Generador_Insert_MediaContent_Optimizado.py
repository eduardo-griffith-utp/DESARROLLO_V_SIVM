import os
from datetime import datetime

BASE_PATH = "C:/Users/CESAR/Documents/Desarrollo V/DESARROLLO_V_SIVM/assets/storage_structure/training_data"

ITEM_MAPPING = {
    'CANGURO': 1, 'CRISTO_REDENTOR': 2, 'DELFIN': 3, 'ELEFANTE': 4,
    'ESTATUA_DE_LA_LIBERTAD': 5, 'JIRAFA': 6, 'KOALA': 7, 'LAPTOP': 8, 'LIBRO': 9, 'LLAVE': 10,
    'MOUSE': 11, 'OSO_POLAR': 12, 'PARAGUA': 13, 'PEZ_PAYASO': 14, 'PUENTE_CENTENARIO': 15, 
    'RINOCERONTE': 16,'ROD_CAREW_ESTADIO': 17, 'SMARTPHONE': 18, 'TORRE_EIFFEL': 19, 'VOLCAN_BARU': 20
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
    return text.replace("'", "''")

def get_item_id(category_name):
    formatted_name = category_name.upper().replace(' ', '_')
    return ITEM_MAPPING.get(formatted_name, None)

output_file = "Insert_MediaContent.sql"

with open(output_file, "w", encoding="utf-8") as f:
    f.write("-- Script de inserción para MediaContent generado automáticamente\n")
    f.write("USE desarrollov_app;\n")
    f.write("BEGIN;\n\n")

    for category in sorted(os.listdir(BASE_PATH)):
        category_path = os.path.join(BASE_PATH, category)
        if os.path.isdir(category_path):
            item_id = get_item_id(category)
            if item_id is None:
                print(f"Advertencia: No se encontró ID para '{category}'. Omitiendo...")
                continue

            values = []
            for file_name in sorted(os.listdir(category_path)):
                full_path = os.path.join(category_path, file_name)
                if os.path.isfile(full_path):
                    route_path = full_path.replace("\\", "/")
                    media_type = infer_type(file_name)
                    description = sanitize_sql(f"{category} - {file_name}")
                    date_uploaded = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    value = f"({item_id}, '{route_path}', '{media_type}', '{description}', '{date_uploaded}')"
                    values.append(value)

            if values:
                f.write(f"-- Datos para categoría: {category}\n")
                f.write("INSERT INTO MediaContent (item_id, route_path, type, description, date_uploaded)\nVALUES\n")
                f.write(",\n".join(values) + ";\n\n")

    print(f"Archivo '{output_file}' generado correctamente.")