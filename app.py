import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image

CLASS_NAMES = ["acne", "eczema", "normal", "other"]

def preprocess(img):
    img = img.convert("RGB").resize((224, 224))
    arr = np.array(img) / 255.0
    return np.expand_dims(arr, axis=0)

def predict(img):
    # Placeholder random prediction (replace with model later)
    probs = np.random.dirichlet(np.ones(len(CLASS_NAMES)), size=1)[0]
    result = {CLASS_NAMES[i]: float(probs[i]) for i in range(len(CLASS_NAMES))}
    top = CLASS_NAMES[int(np.argmax(probs))]
    return {top: result[top]}, result

demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs=[gr.Label(num_top_classes=4), gr.JSON()],
    title="Acne & Eczema Detector",
    description="Upload an image to detect acne, eczema, normal, or other skin conditions."
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
