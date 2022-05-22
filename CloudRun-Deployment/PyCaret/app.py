import os
from flask import Flask
from flask import request
from flask_cors import CORS
import pandas as pd

from model import LoanClassification

app = Flask(__name__)
CORS(app)

model = None


@app.before_first_request
def load_model():
    global model
    model = LoanClassification()


@app.route('/predictions', methods=['POST'])
def get_predictions():
    global model
    data_dict = request.json
    features = {
        "Age": int(data_dict.get("Age", 0)),
        "Experience": int(data_dict.get("Experience", 0)),
        "Income": int(data_dict.get("Income", 0)),
        "Family": int(data_dict.get("Family", 0)),
        "CCAvg": float(data_dict.get("CCAvg", 0)),
        "Education": int(data_dict.get("Education", 0)),
        "Mortgage": int(data_dict.get("Mortgage", 0)),
        "SecuritiesAccount": int(data_dict.get("SecuritiesAccount", 0)),
        "CDAccount": int(data_dict.get("CDAccount", 0)),
        "Online": int(data_dict.get("Online", 0)),
        "CreditCard": int(data_dict.get("CreditCard", 0))}

    features_df = pd.DataFrame([features])

    prediction = model.predict_rating(features_df)

    if prediction == 1:
        response = "Accepted"
    else:
        response = "Rejected"

    return {"Result": f"Loan {response}"}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
