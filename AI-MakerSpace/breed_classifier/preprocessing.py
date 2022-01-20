# regular imports
import tensorflow as tf
import numpy as np
import requests
from PIL import Image
from io import BytesIO

# preprocessing steps
def read_img(image):
    return np.asarray(Image.open(image)) #BytesIO(image)

def scale(image): # normalize and resize
    image = tf.cast(image, tf.float32)
    image /= 255.0
    return tf.image.resize(image,[224,224])

def decode_img(image):
  img = tf.image.decode_jpeg(image, channels=3)
  img = scale(img)
  return np.expand_dims(img, axis=0)



