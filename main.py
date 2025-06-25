import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
import os
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"


# Load your model
model_path = os.path.join(os.path.dirname(__file__), 'model.h5')
model = tf.keras.models.load_model(model_path)

# Set title
st.title(" COVID-19 Detection from X-ray")

# Upload image
uploaded_file = st.file_uploader("Upload Chest X-ray Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file).resize((224, 224))
    img = img.convert("RGB") 
    st.image(img, caption="Uploaded Image", use_container_width=300)

    # Preprocess image
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # (1, 224, 224, 3)

    # Predict
    prediction = model.predict(img_array)
    label = "Negative" if prediction[0][0] > 0.5 else "Positive"

    st.markdown(f"###  Prediction: **{label}**")
