from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import uvicorn
from warnings import filterwarnings
filterwarnings("ignore")  #ignore deprecation warnings
from transformers import AutoTokenizer, AutoModelWithLMHead, pipeline
import os

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# loads tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("t5-small")
model = AutoModelWithLMHead.from_pretrained("t5-small")

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

@app.get('/ai/')
def ai():
    return "Welcome at AI Home page, navigate to '/docs' for API documentation";

@app.get('/ai/summarize')
async def getSummary(text: str):
    return summarization(text)[0]["summary_text"]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)