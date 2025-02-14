import torch
from diffusers import StableDiffusionPipeline
from PIL import Image

def load_model():
    model_id = "CompVis/stable-diffusion-v-1-4-original"
    pipe = StableDiffusionPipeline.from_pretrained(model_id)
    pipe.to("cuda" if torch.cuda.is_available() else "cpu")
    return pipe

def generate_image(prompt):
    pipe = load_model()
    image = pipe(prompt).images[0]
    image.show()
    image.save("generated_image.png")

if __name__ == "__main__":
    prompt = input("Enter your prompt for the image generation: ")
    generate_image(prompt)
