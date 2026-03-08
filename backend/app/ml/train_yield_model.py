import pandas as pd
import joblib

from sklearn.linear_model import LinearRegression

data = pd.DataFrame({
    "area_acres": [1,2,3,4,5,6,7,8],
    "rainfall": [200,250,300,350,400,420,450,470],
    "temperature": [25,26,27,28,29,30,31,32],
    "yield_quintal": [10,18,25,35,45,52,60,68]
})

X = data[["area_acres","rainfall","temperature"]]
y = data["yield_quintal"]

model = LinearRegression()

model.fit(X,y)

joblib.dump(model,"yield_model.pkl")

print("Yield model trained and saved")