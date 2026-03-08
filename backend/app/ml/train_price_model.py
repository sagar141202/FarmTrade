import pandas as pd
import joblib

from sklearn.ensemble import IsolationForest

data = pd.DataFrame({
    "price": [
        1800,1900,2000,2100,2200,
        1950,2050,2150,2250,2350,
        1700,1650,1600
    ]
})

model = IsolationForest(contamination=0.2)

model.fit(data)

joblib.dump(model, "price_anomaly_model.pkl")

print("Price anomaly model trained")