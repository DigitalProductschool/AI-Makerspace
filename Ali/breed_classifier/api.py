# import local module
import preprocessing 
import inference
# fastAPI part
import uvicorn 
from fastapi import FastAPI
from fastapi import UploadFile, File
import requests

app = FastAPI()

@app.post('/predict')

async def predict_img(file: UploadFile = File(...)):
    """
    Steps:
    1. Read Uploaded img
    2. Scale img
    3. Decode img
    4. Make inference
    """
    contents = await file.read()
    # Step 1. Read Uploaded img
    image = preprocessing.read_img(contents)
    # Step 2. Preprocess the img
    image = preprocessing.scale(image)
    # Step 3. Preprocess the img
    image = preprocessing.decode_img(image) 
    # Step 4. Make inference
    prediction= inference.breed_model(image)
    
    return {
      'likely_class': prediction
    }


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host='0.0.0.0')