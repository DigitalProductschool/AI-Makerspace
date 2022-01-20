# regular imports
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import tensorflow as tf
import numpy as np
from PIL import Image
import requests
from io import BytesIO

# streamlit part
import streamlit as st

# local module for classes/features
from features import classes

st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("Dog Breed Image Classifier")
st.text("Provide URL of Dog Image for image classification")

#path = st.text_input('Enter Image URL to Classify.. ','http://vision.stanford.edu/aditya86/ImageNetDogs/images/n02099601-golden_retriever/n02099601_3073.jpg')
img_file_buffer = st.file_uploader("Upload Dog Image to Classify....")

if img_file_buffer  is not None:
    image = img_file_buffer
    image_out = Image.open(img_file_buffer)
    image = image.getvalue()
else:
    test_image = 'http://vision.stanford.edu/aditya86/ImageNetDogs/images/n02099601-golden_retriever/n02099601_3073.jpg'
    image = requests.get(test_image).content
    image_out = Image.open(BytesIO(image))

def scale(image):
  image = tf.cast(image, tf.float32)
  image /= 255.0

  return tf.image.resize(image,[224,224])

def decode_img(image):
  img = tf.image.decode_jpeg(image, channels=3)
  img = scale(img)
  return np.expand_dims(img, axis=0)

@st.cache(allow_output_mutation=True)
def load_model():
  model = tf.keras.models.load_model('./models')
  return model

with st.spinner('Loading Model Into Memory....'):
  model = load_model()

st.write("Predicted Class :")
with st.spinner('classifying.....'):
    label =np.argmax(model.predict(decode_img(image)),axis=1)
    st.write(classes[label[0]][10:])    

st.write("")
st.image(image_out, caption='Classifying Dog Image', use_column_width=True)
