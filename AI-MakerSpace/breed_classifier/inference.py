from tensorflow.keras.models import load_model
from features import classes
from preprocessing import decode_img
import numpy as np
from PIL import Image

# Load the model
model = load_model('./models')

def breed_model(image):
    label =np.argmax(model.predict(decode_img(image)),axis=1)
    return classes[label[0]][10:]