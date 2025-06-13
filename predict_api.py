from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
import io
from PIL import Image
from tensorflow.keras.preprocessing import image
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
model = load_model("model/model_jenis_kulit.h5")
skin_classes = ['dry', 'normal', 'oily']

def preprocess_image(img_bytes):
    img = Image.open(io.BytesIO(img_bytes)).convert('RGB')
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    return img_array

@app.route("/predict", methods=["POST"])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file'}), 400
    file = request.files['file']
    img_array = preprocess_image(file.read())
    prediction = model.predict(img_array)
    skin_type = skin_classes[np.argmax(prediction)]
    return jsonify({'type': skin_type})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
