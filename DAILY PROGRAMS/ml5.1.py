from sklearn.neighbors import KNeighborsClassifier

# Training data
X = [[1], [2], [3], [6], [7], [8]]
y = [0, 0, 0, 1, 1, 1]

# Create K-NN model
knn = KNeighborsClassifier(n_neighbors=3)

# Train the model
knn.fit(X, y)

# Predict the class of a new sample
print("Prediction:", knn.predict([[5]]))
