from sklearn.linear_model import LogisticRegression

# Training data
X = [[1], [2], [3], [6], [7], [8]]
y = [0, 0, 0, 1, 1, 1]

# Create Logistic Regression model
model = LogisticRegression()

# Train the model
model.fit(X, y)

# Predict the class of a new sample
prediction = model.predict([[5]])

print("Prediction:", prediction)
