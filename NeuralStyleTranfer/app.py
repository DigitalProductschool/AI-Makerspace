import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

st.title("Fast Neural image style transfer")
st.write("Streamlit demo for Fast arbitrary image style transfer using a pretrained Image Stylization model from TensorFlow Hub. To use it, simply upload a content image and style image. To learn more about the project, please find the references listed below.")

# Load image stylization module.
@st.cache(allow_output_mutation=True)
def load_model():
  return hub.load("https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2")

style_transfer_model = load_model()

def perform_style_transfer(content_image, style_image):
  # Convert to float32 numpy array, add batch dimension, and normalize to range [0, 1]
    content_image = tf.convert_to_tensor(content_image, np.float32)[tf.newaxis, ...] / 255.
    style_image = tf.convert_to_tensor(style_image, np.float32)[tf.newaxis, ...] / 255.
    
    output = style_transfer_model(content_image, style_image)
    stylized_image = output[0]
    
    return Image.fromarray(np.uint8(stylized_image[0] * 255))

# Upload content and style images.
content_image = st.file_uploader("Upload a content image")
style_image = st.file_uploader("Upload a style image")

# default images
st.write("Or you can choose from the following examples")
col1, col2, col3,col4 = st.columns(4)

if col1.button("Couple on bench"):
  content_image = "examples/couple_on_bench.jpeg"
  style_image = "examples/starry_night.jpeg"

if col2.button("Couple Walking"):
  content_image = "examples/couple_walking.jpeg"
  style_image = "examples/couple_watercolor.jpeg"

if col3.button("Golden Gate Bridge"):
  content_image = "examples/golden_gate_bridge.jpeg"
  style_image = "examples/couple_watercolor.jpeg"

if col4.button("Joshua Tree"):
  content_image = "examples/joshua_tree.jpeg"
  style_image = "examples/starry_night.jpeg"



if style_image and content_image is not None:
  col1, col2 = st.columns(2)

  content_image = Image.open(content_image)
  # It is recommended that the style image is about 256 pixels (this size was used when training the style transfer network).
  style_image = Image.open(style_image).resize((256, 256))

  col1.header("Content Image")
  col1.image(content_image, use_column_width=True)
  col2.header("Style Image")
  col2.image(style_image, use_column_width=True)

  output_image=perform_style_transfer(content_image, style_image)

  st.header("Output: Style transfer Image")
  st.image(output_image, use_column_width=True)

# scroll down to see the references
st.markdown("**References**")

st.markdown("<a href='https://arxiv.org/abs/1705.06830' target='_blank'>1. Exploring the structure of a real-time, arbitrary neural artistic stylization network</a>", unsafe_allow_html=True)

st.markdown("<a href='https://www.tensorflow.org/hub/tutorials/tf2_arbitrary_image_stylization' target='_blank'>2. Tutorial to implement Fast Neural Style Transfer using the pretrained model from TensorFlow Hub</a>  \n", unsafe_allow_html=True)

st.markdown("<a href='https://huggingface.co/spaces/luca-martial/neural-style-transfer' target='_blank'>3. The idea to build a neural style transfer application was inspired from this Hugging Face Space </a>", unsafe_allow_html=True)