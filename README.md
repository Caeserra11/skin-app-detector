# Acne & Eczema Detector Web App

A simple Gradio-based web app that classifies skin conditions into 4 categories:
- Acne
- Eczema
- Normal
- Other

## Deploying on Render

1. Upload this repository to GitHub.
2. Create a new **Web Service** on [Render](https://render.com/).
3. Use the following settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
4. Wait for deployment. The app will be live once built!

## Notes
- Currently uses random predictions (for demo).
- You can later integrate your trained TensorFlow model by loading it in `app.py`.
