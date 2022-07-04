from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import uvicorn
from models import Text #pydantic
from warnings import filterwarnings
filterwarnings("ignore")  #ignore deprecation warnings
from transformers import AutoTokenizer, AutoModelWithLMHead, pipeline
import os

app = FastAPI()

# load model
dirname = os.path.dirname(__file__)
filepath = os.path.join(dirname, 't5-small-saved')


tokenizer = AutoTokenizer.from_pretrained(filepath)
model = AutoModelWithLMHead.from_pretrained(filepath)

summarization = pipeline(
    "summarization", 
    model=model, 
    tokenizer=tokenizer,
    min_length=10,
    max_length=50,
    num_beams=2)

    
@app.get('/')
def welcome():
    return "Welcome All" 

@app.post('/summarize')
async def summarize(text : Text):
    return summarization(text.text)[0]["summary_text"]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)