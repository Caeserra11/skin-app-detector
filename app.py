import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image

# ======== MODEL LOADING ========
# If you have a trained model file, put it in your repo (e.g., model.h5)
# and uncomment this line:
# model = tf.keras.models.load_model("model.h5")

# For now, use a mock prediction (random) until your model is trained:
labels = ["Acne", "Eczema", "Normal", "Other"]

def classify_image(image):
    # Convert uploaded image to array
    img = image.convert("RGB").resize((224, 224))
    img_array = np.expand_dims(np.array(img) / 255.0, axis=0)

    # ==== Replace this with actual model prediction ====
    # preds = model.predict(img_array)
    # predicted_class = labels[np.argmax(preds)]
    # confidence = float(np.max(preds))
    # ==== Temporary mock ====
    predicted_class = np.random.choice(labels)
    confidence = round(np.random.uniform(0.8, 1.0), 2)
    # ================================================

    return {predicted_class: confidence, **{lbl: 0.0 for lbl in labels if lbl != predicted_class}}

# ======== GRADIO UI ========
title = "Skin Disease Detector (Acne, Eczema, Normal, Other)"
description = "Upload a clear face image. The model will predict whether the skin is normal or shows signs of acne, eczema, or other conditions."

interface = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=4),
    title=title,
    description=description,
    examples=[],
)

if __name__ == "__main__":
    # Bind to 0.0.0.0 for Render to detect the app
    interface.launch(server_name="0.0.0.0", server_port=10000)
