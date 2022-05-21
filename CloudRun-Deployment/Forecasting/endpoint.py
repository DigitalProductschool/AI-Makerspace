from flask import Flask
from flask import request

from inference import DPSModel

app = Flask(__name__)

model = None


@app.before_first_request
def load_model():
    global model
    model = DPSModel()


@app.route('/api/predictions', methods=['POST'])
def get_predictions():
    data_dict = request.json
    year = int(data_dict.get('year', 0))
    month = int(data_dict.get('month', 0))

    if (not year) or (not month):
        return {"Error msg": "year/month is missing"}, 400
    elif year < 2021:
        return {"Error msg": "You can't specify a year earlier than 2021"}, 400
    elif month < 1 or month > 12:
        return {"Error msg": "Month value should be between 1 and 12"}, 400
    else:
        n_years = (year - 2021)
        n_steps = (n_years * 12) + month
        value = model.run(n_steps)
        return {"prediction": value}, 200


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
