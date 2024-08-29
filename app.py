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
