from sklearn.linear_model import LinearRegression
import pandas as pd

data = {
    'AdvertisingCost': [10,15,20,25,30,35,40,45,50,55],
    'Salespersons': [2,3,4,5,6,7,8,9,10,11],
    'StoreVisits': [120,150,180,210,240,260,280,300,320,340],
    'MonthlySales': [3.5,4.5,5.8,7.0,8.2,9.5,10.8,12.0,13.5,15.0]
}

df = pd.DataFrame(data)

X = df[['AdvertisingCost', 'Salespersons', 'StoreVisits']]
y = df['MonthlySales']

model = LinearRegression()
model.fit(X, y)

new_data = pd.DataFrame({
    'AdvertisingCost': [38],
    'Salespersons': [7],
    'StoreVisits': [270]
})

prediction = model.predict(new_data)

print("Predicted Monthly Sales:", round(prediction[0], 2), "Lakhs")
