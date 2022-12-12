# Text Autocomplete using HuggingFace 🤗

Text Autocomplete, or text generation, is a task in which an application can fill in incomplete text or paraphrase.

## Goal

In this project we are buidling **text-autocomplete** **streamlit** web-app powered by **GPT-neo**. **GPT-Neo 125M** is a transformer model designed using EleutherAI's replication of the **GPT-3** architecture. GPT-Neo refers to the class of models, while 125M represents the number of parameters of this particular pre-trained model

## Deployed app

The app is deployed on Huggingface **Spaces**: [Click here for live demo](https://huggingface.co/spaces/SudhanshuBlaze/text-generation-gpt-neo)

### Project Structure

```bash
Text Generator Project

├── app.py
└── requirements.txt
```

### Project Requirements

- Python3
- git

### Project Steps

- `Step 1`: Cloning the repo

```bash
git clone https://github.com/DigitalProductschool/AI-Makerspace.git
```

- `Step 2`: Changing working directory to TextAutocomplete-Streamlit

```bash
cd AI-Makerspace/HuggingFace/TextAutocomplete-Streamlit
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

