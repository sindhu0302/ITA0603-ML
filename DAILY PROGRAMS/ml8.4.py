from sklearn.linear_model import LinearRegression

X = [
    [1.0,900,60],
    [1.2,950,70],
    [1.4,1050,80],
    [1.6,1100,90],
    [1.8,1200,100],
    [2.0,1300,110],
    [2.2,1400,120],
    [2.4,1500,130],
    [2.6,1600,140],
    [2.8,1700,150]
]

y = [24,22,20,18,17,15,14,13,12,11]

model = LinearRegression()
model.fit(X, y)

print("Predicted Mileage:", model.predict([[1.8,1200,100]]))
