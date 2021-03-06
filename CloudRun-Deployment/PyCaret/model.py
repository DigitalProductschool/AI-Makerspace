# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 08:24:00 2022
@author: MuhammadAli
@org: Digital Product School
@project: AI-MakerSpace
"""

from pycaret.regression import load_model, predict_model


class LoanClassification:

    def __init__(self):
        self.model = load_model('RF_Model_V1')

    def predict_rating(self, df):
        predictions_data = predict_model(estimator=self.model, data=df)
        return predictions_data['Label'][0]
