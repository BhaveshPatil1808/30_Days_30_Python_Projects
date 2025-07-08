from diffusers import StableDiffusionImg2ImgPipeline
from PIL import Image
import torch

# Load the pipeline (base model)
pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

# Load input image
init_image = Image.open("your_image.jpg").convert("RGB")
init_image = init_image.resize((512, 512))

# Define Ghibli-style prompt
prompt = "A beautiful anime scene in Studio Ghibli style, soft colors, dreamy look, watercolor"

# Generate styled image
image = pipe(prompt=prompt, image=init_image, strength=0.75, guidance_scale=8.5).images[0]

# Save or show result
image.show()
# image.save("ghibli_styled_image.png")
