<h1>Photo2Cartoon Streamlit App </h1>

This directory holds the files for the Photo2Cartoon Streamlit App based on Photo2Cartoon GAN project. 

<h3>Directory Structure:</h3>

|- Img2Cartoon.ipynb - main working notebook

|- models - directory for hosting onnx model
   - photo2cartoon_weights.onnx
  
|- utils - for hosting utility files
   - __init__.py
   - face_detect.py
   - face_seg.py
   - preprocess.py
   - seg_model_384.pb
   - utils.py

|- images - hosting test img
   - photo_test.jpg

|- environment.yml - listing conda based packages

|- packages.txt - listing apt-get packages

|- requirements.txt - listing python pip based packages

|- streamlit_app.py - having streamlit application logic
