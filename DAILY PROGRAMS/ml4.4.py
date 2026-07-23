import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neural_network import MLPClassifier

data = {
    'Fever': ['Yes','Yes','No','Yes','No','Yes','No','Yes','Yes','No'],
    'Cough': ['Yes','Yes','Yes','No','No','Yes','Yes','No','Yes','No'],
    'Headache': ['Yes','No','Yes','Yes','No','Yes','No','No','Yes','Yes'],
    'Body Pain': ['Yes','Yes','No','Yes','No','No','Yes','Yes','Yes','No'],
    'Fatigue': ['Yes','Yes','No','Yes','No','Yes','No','Yes','Yes','No'],
    'Disease': ['Positive','Positive','Negative','Positive','Negative','Positive','Negative','Positive','Positive','Negative']
}

df = pd.DataFrame(data)

le = LabelEncoder()

for col in df.columns:
    df[col] = le.fit_transform(df[col])

X = df.drop('Disease', axis=1)
y = df['Disease']

model = MLPClassifier(hidden_layer_sizes=(4,), max_iter=1000, random_state=42)
model.fit(X, y)

sample = pd.DataFrame({
    'Fever': ['Yes'],
    'Cough': ['Yes'],
    'Headache': ['No'],
    'Body Pain': ['Yes'],
    'Fatigue': ['Yes']
})

for col in sample.columns:
    sample[col] = LabelEncoder().fit(data[col]).transform(sample[col])

prediction = model.predict(sample)

print("Prediction:", "Positive" if prediction[0] == 1 else "Negative")
