from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import json
from keywords import generate_key_words
import pandas as pd

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/generate-keywords')
async def get_keywords(desc:str):
    return json.loads(generate_key_words(desc).to_json(orient='records'))
