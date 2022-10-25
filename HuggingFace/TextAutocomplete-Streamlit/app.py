import streamlit as st
from transformers import pipeline

st.title("AI text-gen Web-app")
st.write("This is a auto-complete/text generation web-app powered by GPT-neo. GPT-Neo 125M is a transformer model designed using EleutherAI's replication of the GPT-3 architecture. GPT-Neo refers to the class of models, while 125M represents the number of parameters of this particular pre-trained model.")

# instantiate the model / download
@st.cache(allow_output_mutation=True)
def load_model():
  generator = pipeline('text-generation', model='EleutherAI/gpt-neo-125M')
  return (generator)

generator=load_model()

min_length=st.slider(
  'Specify Min length of the text of want to be generated', 
  10, 100, 20)
max_length=st.slider(
  'Specify Max length of the text of want to be generated', 
  20, 150, 30)

# create a prompt text for the text generation 
prompt_text = st.text_input(
  label = "Type some text here and this model will generate more....",
  value="We live in a society")


if(max_length<=min_length):
  st.error("max_length cannot be less than equal to min_length")
else:
  with st.spinner("AI is at Work........"):
    gpt_text = generator(
      prompt_text, 
      min_length=min_length, 
      max_length=max_length, 
      do_sample=True)[0]["generated_text"]
    st.success("Successfully generated the below text:")
    st.write(gpt_text)