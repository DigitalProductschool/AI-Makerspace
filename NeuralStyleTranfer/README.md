---
title: Neural Style Transfer
sdk: streamlit
sdk_version: 1.15.2
app_file: app.py
license: Apache License 2.0
---

# Neural image style transfer

Neural style transfer is an optimization technique used to take two images—a content image and a style reference image (such as an artwork by a famous painter)—and blend them together so the output image looks like the content image, but “painted” in the style of the style reference image.

This is implemented by optimizing the output image to match the content statistics of the content image and the style statistics of the style reference image. These statistics are extracted from the images using a convolutional network.

## Goal

In this project we are buidling **streamlit** demo for Fast arbitrary image style transfer using a **pretrained** Image Stylization model from **TensorFlow Hub**. To use it, simply upload a content image and style image.

## Deployed app

The app is deployed on Huggingface **Spaces**: [Click here for live demo](https://huggingface.co/spaces/SudhanshuBlaze/neural-style-transfer-streamlit)

### Project Structure

```bash
Neural Style Transfer Project

├── app.py
├── requirements.txt
└── examples
```

### Project Requirements

- Python3
- git

### Project Steps

- `Step 1`: Cloning the repo

```bash
git clone https://github.com/DigitalProductschool/AI-Makerspace.git
```

- `Step 2`: Changing working directory to NeuralStyleTransfer

```bash
cd AI-Makerspace/NeuralStyleTransfer
```

- `Step 3`: Installing dependencies using pip3

```bash
pip3 install -r requirements.txt
```

- `Step 4`: Running the streamlit web app

```bash
streamlit run app.py
```

#### Now go to http://localhost:8501/ to test out this streamlit web-app

### References:

<a href='https://arxiv.org/abs/1705.06830' target='_blank'>1. Exploring the structure of a real-time, arbitrary neural artistic stylization network</a>

<a href='https://www.tensorflow.org/hub/tutorials/tf2_arbitrary_image_stylization' target='_blank'>2. Tutorial to implement Fast Neural Style Transfer using the pretrained model from TensorFlow Hub</a>

<a href='https://huggingface.co/spaces/luca-martial/neural-style-transfer' target='_blank'>3. The idea to build a neural style transfer application was inspired from this Hugging Face Space </a>
