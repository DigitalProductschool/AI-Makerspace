# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 08:24:00 2022
@author: MuhammadAli
@org: Digital Product School
@project: AI-MakerSpace
"""

from pycaret.regression import load_model, predict_model
import streamlit as st
import pandas as pd

#with st.echo(code_location='below'):
def predict_rating(model, df):
    
    predictions_data = predict_model(estimator = model, data = df)
    
    return predictions_data['Label'][0]
    
model = load_model('RF_Model_V1')


st.title('Loan Classification Web App')
st.write('This is a web app to classify whether a person is eligible for a loan or not based on\
        several features that you can see in the sidebar. Please adjust the\
        value of each feature. After that, click on the Predict button at the bottom to\
        see the prediction.')

                        
Age = int(st.sidebar.number_input(label = 'Age', value = 37))

Experience = int(st.sidebar.number_input(label = 'Experience', value = 13))

Income = int(st.sidebar.number_input(label = 'Income', value = 29))

Family = st.sidebar.selectbox(
    "Family",
    (1,2,3,4)
)

CCAvg = float(st.sidebar.number_input(label = 'CCAvg', value = 1.6))

CDAccount = st.sidebar.selectbox(
    "CDAccount",
    (0,1)
)

SecuritiesAccount = st.sidebar.selectbox(
    "SecuritiesAccount",
    (0,1)
)

Education = st.sidebar.selectbox(
    "Education",
    (1,2,3)
)

Mortgage = int(st.sidebar.number_input(label = 'Mortgage', value = 155))

Online = st.sidebar.selectbox(
    "Online",
    (0,1)
)

CreditCard = st.sidebar.selectbox(
    "CreditCard",
    (0,1)
)

features={
    'Age':Age, 
    'Experience':Experience,
    'Income':Income,
    'Family':Family,
    'CCAvg': CCAvg,
    'Education':Education,	
    'Mortgage':Mortgage,
    'SecuritiesAccount':SecuritiesAccount,	
    'CDAccount':CDAccount,	
    'Online':Online,
    'CreditCard':CreditCard}

features_df  = pd.DataFrame([features])

st.table(features_df)  

if st.button('Predict'):
    
    prediction = predict_rating(model, features_df)

    if prediction == 1:
        prediction = "Accepted"
    else:
        prediction = "Rejected"
    
    st.write(' Based on feature values, the Personal Loan Application is '+ prediction)
    
