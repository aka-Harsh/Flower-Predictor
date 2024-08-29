import os
from flask import Flask, render_template, request
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

app = Flask(__name__)

# Load models
model_vgg16 = load_model('models/vgg16_model.h5')
model_resnet50 = load_model('models/resnet50_model.h5')
model_inceptionv3 = load_model('models/inceptionv3_model.h5')

# Define class names
class_names = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']

def predict_flower(image_path):
    img = load_img(image_path, target_size=(224, 224))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.

    # Make predictions with each model
    pred_vgg16 = model_vgg16.predict(img_array)
    pred_resnet50 = model_resnet50.predict(img_array)
    pred_inceptionv3 = model_inceptionv3.predict(img_array)

    # Ensemble predictions (simple averaging)
    ensemble_pred = (pred_vgg16 + pred_resnet50 + pred_inceptionv3) / 3

    predicted_class = class_names[np.argmax(ensemble_pred)]
    confidence = np.max(ensemble_pred) * 100

    return predicted_class, confidence

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', message='No file part')
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', message='No selected file')
        if file:
            image_path = os.path.join('static', 'uploads', file.filename)
            file.save(image_path)
            predicted_class, confidence = predict_flower(image_path)
            return render_template('index.html', 
                                   message='Upload successful',
                                   image_path=image_path,
                                   prediction=predicted_class,
                                   confidence=confidence)
    return render_template('index.html', message='Upload an image')

if __name__ == '__main__':
    os.makedirs('static/uploads', exist_ok=True)
    app.run(debug=True)
