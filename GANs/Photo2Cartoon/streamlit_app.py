import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import os
from io import BytesIO
from subprocess import call

import cv2
import numpy as np
import onnxruntime
import requests
import streamlit as st
from PIL import Image

from utils import Preprocess


@st.experimental_memo(show_spinner=False)
def download_model():
    call('gdown -q "1bjXhuTt0CNc5tqNN8ogcfB_F1V_RxnXM" -O models/', shell=True)

st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("Cartoon Image Generator")
st.text("Either Upload or Provide URL of Your Image")

with st.spinner('Wait for model download...'):
    download_model()

path = st.text_input('Enter Image URL to Classify...')
img_file_buffer = st.file_uploader("Upload Your Image to Cartoonify...")

if img_file_buffer is not None:
    image = img_file_buffer
    image_out = Image.open(img_file_buffer)
    image_out = image_out.convert('RGB')
    st.image(image_out, caption='Your Image', use_column_width=False, width=400)
    im1 = image_out.save("input.jpg")
    image_input = cv2.imread("input.jpg")
    if im1:
        call('rm -R "input.jpg" ', shell=True)
else:
    if path:
        test_image = repr(path)
    else:
        test_image = r'https://6.vikiplatform.com/image/c65419246af34d5982e5e9f1d59b0e0d.jpg'
    image_input = requests.get(test_image, stream=True).raw
    image_input = np.asarray(bytearray(image_input.read()), dtype="uint8")
    image_input = cv2.imdecode(image_input, cv2.IMREAD_COLOR)

    defualt_url = 'https://6.vikiplatform.com/image/c65419246af34d5982e5e9f1d59b0e0d.jpg'
    image_url_content = requests.get(defualt_url).content
    image_out = Image.open(BytesIO(image_url_content))
    st.image(image_out, caption='Your Image', use_column_width=False, width=400)


class Photo2Cartoon:
    def __init__(self):
        self.pre = Preprocess()

        assert os.path.exists(
            './models/photo2cartoon_weights.onnx'), "[Step1: load weights] Can not find 'photo2cartoon_weights.onnx' in folder 'models!!!'"
        self.session = onnxruntime.InferenceSession(
            './models/photo2cartoon_weights.onnx')
        print('[Step1: load weights] success!')

    def inference(self, img):
        # face alignment and segmentation
        face_rgba = self.pre.process(img)
        if face_rgba is None:
            print('[Step2: face detect] can not detect face!!!')
            return None

        print('[Step2: face detect] success!')
        face_rgba = cv2.resize(face_rgba, (256, 256), interpolation=cv2.INTER_AREA)
        face = face_rgba[:, :, :3].copy()
        mask = face_rgba[:, :, 3][:, :, np.newaxis].copy() / 255.
        face = (face*mask + (1-mask)*255) / 127.5 - 1

        face = np.transpose(face[np.newaxis, :, :, :],
                            (0, 3, 1, 2)).astype(np.float32)

        # inference
        cartoon = self.session.run(['output'], input_feed={'input': face})

        # post-process
        cartoon = np.transpose(cartoon[0][0], (1, 2, 0))
        cartoon = (cartoon + 1) * 127.5
        cartoon = (cartoon * mask + 255 * (1 - mask)).astype(np.uint8)
        cartoon = cv2.cvtColor(cartoon, cv2.COLOR_RGB2BGR)
        print('[Step3: photo to cartoon] success!')
        return cartoon


if st.button('Generate'):
    if image_input is None:
        st.error("Please Upload Your Image")
    else:
        with st.spinner('Abra ka dabra...'):
            img = cv2.cvtColor(image_input, cv2.COLOR_BGR2RGB)
            c2p = Photo2Cartoon()
            cartoon = c2p.inference(img)
            if cartoon is not None:
                cv2.imwrite("cartoon_result.png", cartoon)
                st.image("cartoon_result.png", caption='Cartoon Image',
                        use_column_width=False, width=300)
                with open("cartoon_result.png", "rb") as file:
                    btn = st.download_button(
                        label="Download Cartoon Image",
                        data=file,
                        file_name="cartoon_result.png",
                        mime="image/png"
                    )
                st.success('Cartoon portrait has been made successfully!')
