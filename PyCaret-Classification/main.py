import pandas as pd
from pycaret.classification import load_model, predict_model
from fastapi import FastAPI
from fastapi.params import Body
import uvicorn
from pydantic import BaseModel
from typing import Optional

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
model = load_model('models/RF_Model_V1')
model2 = load_model('models/RF_Model_V1')

@app.get('/')
def root():
    return {"Welcome": "Please append /docs to the above url for Swagger UI"}

@app.post('/loans')
def predict(schema_model: Model):

    # converting pydantic model to dictionary
    data_dict = schema_model.dict()
    #print(data_dict) 

    # removing version from dict
    data_dict.pop('version')

    # converting data_dict to pandas dataframce
    data_df = pd.DataFrame([data_dict])

    #print(type(model))
    # making a prediction
    # predictions = model.predict(data_df[:])
    predictions = predict_model(model, data=data_df) 
    
    #print(data_df)

    return {'prediction': list(predictions['Label'])}

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
        data_df = pd.DataFrame([data_dict])
        print(data_df)

        # making a prediction
        predictions = predict_model(model2, data=data_df) 
        
        
        return {'prediction': list(predictions['Label'])}

# # /loans/fixed_endpoint comes first or else if FastAPI will find it later, 
# # it will assume it to be a version while calling 
# # and thus will call version endpoint.
# @app.post('/loans/greetings')
# def predict():
#     return {"hello":"keep it up!"}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000, reload=True)
