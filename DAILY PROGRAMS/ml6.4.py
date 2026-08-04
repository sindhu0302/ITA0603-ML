from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Employee dataset
data = {
    'Experience': [10, 9, 8, 4, 3, 11, 5, 8, 2, 7],
    'Performance': [95, 92, 90, 70, 65, 96, 75, 89, 60, 87],
    'TrainingHours': [50, 48, 45, 25, 20, 52, 30, 44, 18, 40],
    'Promotion': ['Yes', 'Yes', 'Yes', 'No', 'No',
                  'Yes', 'No', 'Yes', 'No', 'Yes']
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and Target
X = df[['Experience', 'Performance', 'TrainingHours']]
y = df['Promotion']

# Encode target labels
le = LabelEncoder()
y = le.fit_transform(y)

# Train Naïve Bayes model
model = GaussianNB()
model.fit(X, y)

# New employee data (use DataFrame to avoid warning)
new_employee = pd.DataFrame({
    'Experience': [6],
    'Performance': [80],
    'TrainingHours': [35]
})

# Predict
prediction = model.predict(new_employee)

# Convert prediction back to original label
result = le.inverse_transform(prediction)

print("Prediction:", result[0])
