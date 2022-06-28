import streamlit as st
import tensorflow as tf
import numpy as np
import requests
import cv2
import gdown
from tensorflow.keras.applications.inception_v3 import preprocess_input
from subprocess import call
from glob import glob

@st.cache(allow_output_mutation=True)
def downloading_model():
  id = "1FgnD8ixlLscDvFCHuq99TDYpMV66I-Mb"
  output = "bestmodel_3class.hdf5"
  gdown.download(id=id, output=output, quiet=False)

downloading_model()

files = glob('*bestmodel_3class.hdf5*')
call(f'mv {files} bestmodel_3class.hdf5', shell=True)
call(f'mv bestmodel_3class.hdf5 models/', shell=True)

@st.cache(allow_output_mutation=True)
def load_model():
    model = tf.keras.models.load_model('models/bestmodel_3class.hdf5', compile = False)
    return model

with st.spinner('Loading Model Into Memory....'):
    model = load_model()

food_list = ['samosa','pizza','omelette']

path = st.text_input('Enter Image URL to Classify...')
img_file_buffer = st.file_uploader("Upload Your Image to Classify...")

if img_file_buffer is not None:
    image = img_file_buffer.read()
    np_arr = np.frombuffer(image, np.uint8)
    # decode image
    image_input = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    image_input = cv2.cvtColor(image_input, cv2.COLOR_BGR2RGB)
    st.image(image_input, caption='Your Image', use_column_width=False, width=400)
else:
    if path:
        test_image = path
    else:
        test_image = r'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Samosachutney.jpg/280px-Samosachutney.jpg'
    image_input = requests.get(test_image, stream=True).raw
    image_input = np.asarray(bytearray(image_input.read()), dtype="uint8")
    image_input = cv2.imdecode(image_input, cv2.IMREAD_COLOR)
    image_input = cv2.cvtColor(image_input, cv2.COLOR_BGR2RGB)
    st.image(image_input, caption='Your Image', use_column_width=False, width=400)


def predict_class(model, img):
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    pred = model.predict(img)
    index = np.argmax(pred)
    food_list.sort()
    pred_value = food_list[index]
    return pred_value


st.write("Predicted Class :")
with st.spinner('classifying.....'):
    st.write(predict_class(model, image_input))
st.write("")
