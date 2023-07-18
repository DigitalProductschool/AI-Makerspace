import pandas as pd
from fastapi import FastAPI
from fastapi.params import Body
import uvicorn
from pydantic import BaseModel 
from typing import Optional
import joblib

# Create the app
app = FastAPI()

# create basemodel class
class Model(BaseModel):
    Age: int 
    Experience: int
    Income: int
    Family: int
    CCAvg: float
    Education: int
    Mortgage: int 
    SecuritiesAccount: int = 0 # req but 0 will be default
    CDAccount: int
    Online: int
    CreditCard: int 
    version: Optional[int]  # optional and None will be default

# Load trained Pipeline
model = joblib.load("models/model.pkl")
model2 = joblib.load("models/model.pkl")

@app.get('/')
def root():
    return {"Welcome": "Please append /docs to the above url for Swagger UI"}

@app.post('/loans')
def predict(schema_model: Model):

    # converting pydantic model to dictionary
    data_dict = schema_model.dict()
    
    # removing version from dict
    data_dict.pop('version')

    #print(data_dict)

    # converting data_dict to pandas dataframce
    data_df=pd.DataFrame.from_dict([data_dict])

    #print(type(model))
    # making a prediction
    predictions = model.predict(data_df[:])

    return {'prediction': predictions[0].item()}

# /loans/fixed_endpoint comes first or else if FastAPI will find it later, 
# it will assume it to be a version while calling 
# and thus will call version endpoint.
@app.post('/loans/greetings')
def predict():
    return {"hello":"keep it up!"}

@app.post('/loans/{version}')
def predict(schema_model: Model,version: str): # version to int, default str
    # converting pydantic model to dictionary
    data_dict = schema_model.dict()
    print(data_dict)

    # removing version from dict
    data_dict.pop('version')
    
    if version == 'churn':
        # converting data_dict to pandas dataframce
        data_df=pd.DataFrame.from_dict([data_dict])
        print(data_df)

        # making a prediction
        predictions = model.predict(data_df[:])
         
        return {'prediction': predictions[0].item()}

# # /loans/fixed_endpoint comes first or else if FastAPI will find it later, 
# # it will assume it to be a version while calling 
# # and thus will call version endpoint.
# @app.post('/loans/greetings')
# def predict():
#     return {"hello":"keep it up!"}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000, reload=True)
