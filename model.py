from PIL import Image
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import torch

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float32)
pipe = pipe.to("cpu")
pipe.load_lora_weights("./checkpoint-7700")


def generate_image(prompt: str) -> Image.Image: 
    img = pipe(prompt).images[0]
    return img
