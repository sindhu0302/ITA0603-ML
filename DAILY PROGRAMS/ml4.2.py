import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neural_network import MLPClassifier

df = pd.DataFrame({
    'CGPA': [9,8,7,6,5,9,8,6,7,5],
    'Communication': ['Excellent','Good','Good','Average','Poor','Excellent','Good','Average','Excellent','Poor'],
    'Internship': ['Yes','Yes','Yes','No','No','Yes','No','Yes','Yes','No'],
    'Programming': ['Excellent','Good','Average','Average','Poor','Good','Good','Average','Good','Average'],
    'Placement': ['Placed','Placed','Placed','Not Placed','Not Placed','Placed','Placed','Not Placed','Placed','Not Placed']
})

encoders = {}

for col in ['Communication', 'Internship', 'Programming', 'Placement']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

X = df.drop('Placement', axis=1)
y = df['Placement']

ann = MLPClassifier(hidden_layer_sizes=(4,), max_iter=5000, random_state=42)
ann.fit(X, y)

new_sample = pd.DataFrame({
    'CGPA': [8],
    'Communication': ['Excellent'],
    'Internship': ['Yes'],
    'Programming': ['Good']
})

for col in ['Communication', 'Internship', 'Programming']:
    new_sample[col] = encoders[col].transform(new_sample[col])

prediction = ann.predict(new_sample)

print("Prediction:", encoders['Placement'].inverse_transform(prediction)[0])
