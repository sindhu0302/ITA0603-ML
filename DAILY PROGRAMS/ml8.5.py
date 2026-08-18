from sklearn.linear_model import LinearRegression

X = [
    [10,100],[20,150],[30,200],[40,250],[50,300],
    [60,350],[70,400],[80,450],[90,500],[100,550]
]

y = [12,18,25,32,40,48,57,66,76,87]

model = LinearRegression()
model.fit(X, y)

print("Predicted Sales:", model.predict([[65,375]]))
