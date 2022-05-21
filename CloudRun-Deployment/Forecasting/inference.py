import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAXResults


class DPSModel():
    def __init__(self):
        self.Alkohol_model = SARIMAXResults.load('./models/Alkoholunfaelle_model.pkl')
        self.Verkehrs_model = SARIMAXResults.load('./models/Verkehrsunfaelle_model.pkl')

    def run(self, n_steps):
        models = [self.Alkohol_model, self.Verkehrs_model]

        output_value = []
        for model in models:
            forecast = model.get_forecast(steps=n_steps)
            mean_forecast = forecast.predicted_mean
            output_value.append(mean_forecast[-1])

        final_value = np.sum(output_value)

        return int(final_value)
