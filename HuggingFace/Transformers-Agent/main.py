## Can use OpenAI Agent as well instead of HfAgent
# from transformers import OpenAiAgent
# agent = OpenAiAgent(model="text-davinci-003", api_key="<your_api_key>")

from huggingface_hub import login
from transformers import HfAgent
from PIL import Image
import sounddevice as sd
import pdfplumber

# Login to HuggingFace
login("<Insert HuggingFace Token>")

## Initialise HuggingFace Agent
# Starcoder
agent = HfAgent("https://api-inference.huggingface.co/models/bigcode/starcoder")
# StarcoderBase
# agent = HfAgent("https://api-inference.huggingface.co/models/bigcode/starcoderbase")
# OpenAssistant
# agent = HfAgent(url_endpoint="https://api-inference.huggingface.co/models/OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5")


## Image Generation Code
# Generate code from prompt. Works with Starcoder and StarcoderBase agent.
code = agent.run("Draw me a picture of rivers and lakes", return_code=True)
print('Code:-')
print(code)


## Image to Text
# Load the image
image_path = "beaver.png"
image = Image.open(image_path)

# Get the caption
caption = agent.run("Caption the following image", image=image)
print('Caption:',caption)


## Text to Speech
# Get Audio Array
audio_data = agent.run("Read the following text out loud", text="My name is Dhruv")

# Play the audio
sd.play(audio_data, samplerate=20000)  # Adjust the samplerate if necessary

# Wait until the audio finishes playing
sd.wait()


## PDF Question Answering
# Converting PDF to text
with pdfplumber.open("Dhruv_Essay.pdf") as pdf:
    # Extract the text from the PDF document
    text = ""
    for page in pdf.pages:
        text += page.extract_text()

# Text Question Answering
agent.run(
    "In the following `text`, what is Dhruv's aim?",
    text=text,
)


## Text Translation Code
code = agent.run(
    "Translate the following `text` to German",
    text='My name is Dhruv.',
    return_code=True
)
print('Code:-')
print(code)


## Summary of link
summary = agent.run("Summarize http://hf.co")
print('Summary:', summary)