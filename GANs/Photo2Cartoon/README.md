<h1>Photo2Cartoon Streamlit App </h1>

This directory holds the files for the Photo2Cartoon Streamlit App based on Photo2Cartoon GAN project. 

<h3>Model:</h3>

<a href='https://github.com/minivision-ai/photo2cartoon'>Photo2Cartoon</a> by minivision-ai.

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

|- Dockerfile - for deploying docker container

|- environment.bak.yml - listing conda based packages

|- packages.txt - listing apt-get packages

|- requirements.txt - listing python pip based packages

|- streamlit_app.py - having streamlit application logic

<h3>References:</h3>
<b>U-GAT-IT</b>: Unsupervised Generative Attentional Networks with Adaptive Layer-Instance Normalization for Image-to-Image Translation. 

<a href='https://arxiv.org/abs/1907.10830'>[Paper]</a> <a href='https://github.com/znxlwm/UGATIT-pytorch'>[Code]</a>

<a href='https://github.com/TreB1eN/InsightFace_Pytorch'>InsightFace_Pytorch</a>
