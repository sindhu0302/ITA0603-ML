from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Fruit dataset
data = {
    'Weight': [150, 160, 145, 120, 125, 130, 155, 118, 148, 122],
    'Diameter': [7.5, 7.8, 7.3, 5.5, 5.8, 6.0, 7.6, 5.4, 7.4, 5.7],
    'Sweetness': [90, 88, 91, 70, 72, 74, 89, 69, 92, 71],
    'Fruit': ['Apple', 'Apple', 'Apple', 'Orange', 'Orange',
              'Orange', 'Apple', 'Orange', 'Apple', 'Orange']
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and Target
X = df[['Weight', 'Diameter', 'Sweetness']]
y = df['Fruit']

# Encode target labels
le = LabelEncoder()
y = le.fit_transform(y)

# Train Naïve Bayes model
model = GaussianNB()
model.fit(X, y)

# New fruit sample
new_fruit = pd.DataFrame({
    'Weight': [152],
    'Diameter': [7.5],
    'Sweetness': [90]
})

# Predict
prediction = model.predict(new_fruit)

# Convert prediction back to original label
result = le.inverse_transform(prediction)

print("Prediction:", result[0])
