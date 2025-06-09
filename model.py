from PIL import Image
from diffusers import DiffusionPipeline

pipe = DiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5").to("cuda")
pipe.load_lora_weights("AlejFernandezV/NarutoImageGenerations")

def generate_image(prompt: str) -> Image.Image:
    img = pipe(prompt).images[0]
    return img
