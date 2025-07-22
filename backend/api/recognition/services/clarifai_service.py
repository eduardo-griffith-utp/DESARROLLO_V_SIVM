import os
if os.name == 'nt' and 'HOME' not in os.environ:
    os.environ['HOME'] = os.environ.get('USERPROFILE', 'C:/Users/DELL')
from dotenv import load_dotenv
from clarifai.client.model import Model
import asyncio 

from clarifai.client.model import Model
from dotenv import load_dotenv
import base64


load_dotenv()

MODEL_ID = "nsfw-recognition"
USER_ID = "clarifai"
APP_ID = "main"
#PAT = os.getenv("CLARIFAI_PAT")
PAT = "eaf0e0d143844590becc80fd27091fc4"

def analizar_imagen_nsfw(image_base64):
    try:
        try:
            asyncio.get_running_loop()
        except RuntimeError:
            asyncio.set_event_loop(asyncio.new_event_loop())

        model = Model(user_id=USER_ID, app_id=APP_ID, model_id=MODEL_ID,pat=PAT)

        decoded_bytes = base64.b64decode(image_base64)

        response = model.predict_by_bytes(decoded_bytes, input_type="image")

        if response.status.code != 10000:
            return {
                "exito": False,
                "error": f"Clarifai error: {response.status.description}"
            }

        resultados = {
            concept.name: concept.value
            for concept in response.outputs[0].data.concepts
        }

        return {
            "exito": True,
            "nsfw_scores": resultados
        }

    except Exception as e:
        return {
            "exito": False,
            "error": str(e)
        }