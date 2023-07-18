import os
from io import BytesIO
from subprocess import call
import fastai
import streamlit as st
import numpy as np
from PIL import Image
from deoldify.visualize import *

st.set_page_config()
# st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("Image Colorizer")
st.text("The solution uses DeOldify to fill color in black and white images using GANS.")

@st.cache(allow_output_mutation=True)
def load_model():
    colorizer = get_image_colorizer(artistic=True)
    return colorizer

def load_image(image_file):
	img = Image.open(image_file)
	return img

with st.spinner('Loading Model Into Memory....'):
    model = load_model()

#path = st.text_input('Enter Image URL to Colorize...')
img_file_buffer = st.file_uploader("Upload Your Image to Colorize...")

if img_file_buffer is not None:
  file_details = {
      "filename":img_file_buffer.name,
      "filetype":img_file_buffer.type,
      "filesize":img_file_buffer.size
      }
  saved_file_name=f"{file_details['filetype']}".replace("/",".")
  img = Image.open(img_file_buffer)
  im1 = img.save(saved_file_name)
  st.write("Transformed Image:")
  model.plot_transformed_image(saved_file_name, render_factor=10, display_render_factor=True, figsize=(8,8))
  show_img = st.image(load_image(f'result_images/{saved_file_name}'),width=250)

  with open(f'result_images/{saved_file_name}', "rb") as file:
    if st.download_button(
      label=f"Download {saved_file_name}",
      data=file,
      file_name=f'result_images/{saved_file_name}',
      mime=saved_file_name.replace(".","/")):
  
        with st.spinner('Downloading Image....'):
          os.remove(f'result_images/{saved_file_name}')
          os.remove(saved_file_name)
