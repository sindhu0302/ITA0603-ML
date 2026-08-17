from sklearn.linear_model import LogisticRegression

X = [[1],[2],[3],[6],[7],[8]]
y = [0,0,0,1,1,1]

model = LogisticRegression()
model.fit(X, y)

print("Prediction:", model.predict([[5]]))
