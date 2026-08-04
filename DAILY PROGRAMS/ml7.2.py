from sklearn.linear_model import LogisticRegression
import pandas as pd

# Student Placement Dataset
data = {
    'CGPA': [9.2, 8.8, 8.5, 7.2, 6.8, 9.0, 7.0, 8.7, 6.5, 9.1],
    'AptitudeScore': [90, 85, 82, 72, 68, 91, 70, 86, 65, 92],
    'CommunicationScore': [88, 84, 80, 70, 65, 89, 68, 83, 60, 90],
    'Placement': [1, 1, 1, 0, 0, 1, 0, 1, 0, 1]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and Target
X = df[['CGPA', 'AptitudeScore', 'CommunicationScore']]
y = df['Placement']

# Train Logistic Regression model
model = LogisticRegression()
model.fit(X, y)

# New student data
new_student = pd.DataFrame({
    'CGPA': [8.9],
    'AptitudeScore': [88],
    'CommunicationScore': [85]
})

# Predict
prediction = model.predict(new_student)

print("Prediction:", prediction[0])

if prediction[0] == 1:
    print("Result: Placed")
else:
    print("Result: Not Placed")
