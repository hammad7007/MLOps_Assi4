import gradio as gr
import pytesseract
from PIL import Image
from PIL import UnidentifiedImageError
import numpy as np

# Define the function to perform OCR
def perform_ocr(input_image):
    try:
        # Convert the Gradio input (which is a byte array) to a PIL Image
        image = Image.fromarray(input_image)  # Convert the numpy array to a PIL Image
        
        # Perform OCR on the image
        text = pytesseract.image_to_string(image)
        
        return text
    except UnidentifiedImageError as e:
        return "Invalid image format. Please upload a valid image."

# Create a Gradio interface
iface = gr.Interface(
    fn=perform_ocr,
    inputs="image",
    outputs="text",
    title="Image to Text OCR",
    description="Upload an image and get the text extracted from it.",
    live=True
)

# Launch the interface
iface.launch()
