from prediccion import predict_from_base64, load_saved_model
import json
import os

''' 
09/07/2025 Funcion agregada para hacer su llamado por medio del api y que retorne el
    resultado en la memoria del hilo, sin necesidad de escribir el archivo json,
    en teoria el api convierte el resultado en formato json, A.S.
'''
def predict_imagen_api(base64_string):
    model, class_names = load_saved_model()
    if base64_string.startswith("data:image"):
        base64_string = base64_string.split(",")[1]
    result = predict_from_base64(model, class_names,base64_string)
    ##json.sumps(result, direct, ensure_ascii=False, indent=4)
    return result

if __name__ == "__main__":
    try:
        ##print("Directorio actual:", os.getcwd())
        model, class_names = load_saved_model()
        ##print("Modelo cargado.")

        ##con estas lineas se elimina el encabezado del archivo base64 para que no mande error
        with open("src\imagen.txt", "r") as f:
            base64_str = f.read()
        if base64_str.startswith("data:image"):
            base64_str = base64_str.split(",")[1]
        ##llamada al metodo que predice
        resultado = predict_from_base64(model, class_names, base64_str)

        with open("output/resultado.json","w", encoding="utf-8") as direct:
            print(json.dumps(resultado, ensure_ascii=False, indent=4))
            ##metodo de json para guardar el resultado
            json.dump(resultado, direct, ensure_ascii=False, indent=4)
            
    except Exception as e:
        print(f"\nError general: {str(e)}")

 