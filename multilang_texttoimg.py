from googletrans import Translator
import torch
from diffusers import StableDiffusionPipeline

class CFG:
    device = "cuda" if torch.cuda.is_available() else "cpu"
    seed = 42
    generator = torch.Generator(device).manual_seed(seed)
    image_gen_steps = 35
    image_gen_model_id = "stabilityai/stable-diffusion-2"
    image_gen_size = (900, 900)
    image_gen_guidance_scale = 9

# Initialize the Stable Diffusion model
def initialize_model():
    model = StableDiffusionPipeline.from_pretrained(
        CFG.image_gen_model_id, 
        torch_dtype=torch.float16 if CFG.device == "cuda" else torch.float32,
        revision="fp16" if CFG.device == "cuda" else None,
        use_auth_token='API_KEY'
    )
    model = model.to(CFG.device)
    return model

# Translation function
def get_translation(text, dest_lang="en"):
    translator = Translator()
    translated_text = translator.translate(text, dest=dest_lang)
    return translated_text.text

# Generate image function
def generate_image(prompt, model):
    image = model(
        prompt, 
        num_inference_steps=CFG.image_gen_steps,
        generator=CFG.generator,
        guidance_scale=CFG.image_gen_guidance_scale
    ).images[0]
    
    # Resize image to desired size
    image = image.resize(CFG.image_gen_size)
    return image
