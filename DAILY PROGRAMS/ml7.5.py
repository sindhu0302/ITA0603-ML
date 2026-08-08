from sklearn.linear_model import LinearRegression
import pandas as pd

data = {
    'EngineCapacity': [1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8],
    'Weight': [900,950,1050,1150,1250,1350,1450,1550,1650,1750],
    'Speed': [60,70,80,90,100,110,120,130,140,150],
    'Mileage': [24,22,20,18,16,15,13,12,11,10]
}

df = pd.DataFrame(data)

X = df[['EngineCapacity', 'Weight', 'Speed']]
y = df['Mileage']

model = LinearRegression()
model.fit(X, y)

new_data = pd.DataFrame({
    'EngineCapacity': [1.5],
    'Weight': [1100],
    'Speed': [85]
})

prediction = model.predict(new_data)

print("Predicted Mileage:", round(prediction[0], 2), "km/L")
