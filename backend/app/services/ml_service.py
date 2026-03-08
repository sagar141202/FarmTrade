import joblib
import numpy as np

model = joblib.load("app/ml/yield_model.pkl")

def predict_yield(area_acres, rainfall, temperature):

    input_data = np.array([[area_acres, rainfall, temperature]])

    prediction = model.predict(input_data)

    return float(prediction[0])