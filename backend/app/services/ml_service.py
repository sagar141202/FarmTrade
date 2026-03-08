import joblib
import numpy as np

yield_model = joblib.load("app/ml/yield_model.pkl")

price_model = joblib.load("app/ml/price_anomaly_model.pkl")


def predict_yield(area_acres, rainfall, temperature):

    input_data = np.array([[area_acres, rainfall, temperature]])

    prediction = yield_model.predict(input_data)

    return float(prediction[0])


def detect_price_anomaly(price):

    input_data = np.array([[price]])

    result = price_model.predict(input_data)

    score = price_model.decision_function(input_data)[0]

    if result[0] == -1:
        status = "Exploitative Price"
    elif score < 0.05:
        status = "Slightly Low Price"
    else:
        status = "Fair Price"

    return {
        "status": status,
        "score": float(score)
    }