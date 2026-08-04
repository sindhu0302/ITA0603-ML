from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Patient dataset
data = {
    'Temperature': [39.1, 38.8, 37.0, 39.3, 36.8, 38.7, 37.1, 39.0, 36.9, 38.9],
    'HeartRate': [112, 109, 78, 115, 74, 110, 80, 113, 76, 111],
    'OxygenLevel': [94, 95, 99, 93, 98, 94, 98, 92, 99, 93],
    'Disease': ['Positive', 'Positive', 'Negative', 'Positive', 'Negative',
                'Positive', 'Negative', 'Positive', 'Negative', 'Positive']
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and Target
X = df[['Temperature', 'HeartRate', 'OxygenLevel']]
y = df['Disease']

# Encode target labels
le = LabelEncoder()
y = le.fit_transform(y)

# Train Naïve Bayes model
model = GaussianNB()
model.fit(X, y)

# New patient data
new_patient = pd.DataFrame({
    'Temperature': [38.5],
    'HeartRate': [108],
    'OxygenLevel': [95]
})

# Predict
prediction = model.predict(new_patient)

# Convert prediction back to original label
result = le.inverse_transform(prediction)

print("Prediction:", result[0])
