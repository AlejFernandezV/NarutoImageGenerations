import requests
import base64
from PIL import Image
import io

# Reemplaza esta URL con la que te dé ngrok en Colab
API_URL = "https://1ad3-34-16-184-26.ngrok-free.app/generate"

def generate_image(prompt: str) -> Image.Image:
    response = requests.post(API_URL, json={"prompt": prompt})

    if response.status_code == 200:
        data = response.json()
        img_base64 = data["image"]
        img_bytes = base64.b64decode(img_base64)
        image = Image.open(io.BytesIO(img_bytes))
        return image
    else:
        raise Exception(f"Error al generar la imagen: {response.status_code}, {response.text}")
