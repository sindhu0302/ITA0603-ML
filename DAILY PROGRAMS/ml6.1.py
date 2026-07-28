from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score

# Training data
X = [[1], [2], [3], [6], [7], [8]]
y = [0, 0, 0, 1, 1, 1]

# Create Naïve Bayes model
model = GaussianNB()

# Train the model
model.fit(X, y)

# Predict the class labels
prediction = model.predict(X)

# Display confusion matrix and accuracy
print("Confusion Matrix:")
print(confusion_matrix(y, prediction))

print("Accuracy:", accuracy_score(y, prediction))
