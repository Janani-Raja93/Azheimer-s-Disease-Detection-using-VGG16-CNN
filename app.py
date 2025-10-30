from flask import Flask, render_template, request,send_from_directory
import os
from PIL import Image
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Load the trained model with the correct filename
model = tf.keras.models.load_model("model/alzheimer_model.keras", compile=False)

# Class labels
class_labels = ["Mild Impairment", "Moderate Impairment", "No Impairment", "Very Mild Impairment"]

# Upload folder configuration
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Add the favicon route here, right after app creation
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict")
def predict():
    return render_template("predict.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return render_template("predict.html", message="No file part")

    file = request.files["file"]
    if file.filename == "":
        return render_template("predict.html", message="No selected file")

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # Image preprocessing
    img = Image.open(filepath).convert("RGB").resize((224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    prediction = model.predict(img_array)[0]
    class_index = np.argmax(prediction)
    label = class_labels[class_index]
    confidence = prediction[class_index]

    # Threshold-based classification
    if confidence < 0.50:
        result = "Healthy Brain"
        confidence = 1.0
    else:
        result = f"Alzheimer's Detected: {label}"
        confidence = f"{confidence:.4f}"

    return render_template("result.html", prediction=result, confidence=confidence, image_name=file.filename)

if __name__ == "__main__":
    app.run(debug=True)
