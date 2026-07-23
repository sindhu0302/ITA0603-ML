import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neural_network import MLPClassifier

data = {
    'Experience': ['High','High','Medium','Medium','Low','High','Medium','Low','High','Low'],
    'Performance': ['Excellent','Good','Good','Average','Poor','Excellent','Good','Average','Good','Poor'],
    'Leadership': ['Yes','Yes','Yes','No','No','Yes','No','No','Yes','No'],
    'Training': ['Yes','Yes','Yes','Yes','No','No','Yes','No','Yes','Yes'],
    'Promotion': ['Promoted','Promoted','Promoted','Not Promoted','Not Promoted','Promoted','Promoted','Not Promoted','Promoted','Not Promoted']
}

df = pd.DataFrame(data)

le = LabelEncoder()

for col in df.columns:
    df[col] = le.fit_transform(df[col])

X = df.drop('Promotion', axis=1)
y = df['Promotion']

model = MLPClassifier(hidden_layer_sizes=(4,), max_iter=5000, random_state=42)
model.fit(X, y)

sample = pd.DataFrame({
    'Experience': ['Medium'],
    'Performance': ['Good'],
    'Leadership': ['Yes'],
    'Training': ['Yes']
})

for col in sample.columns:
    sample[col] = LabelEncoder().fit(data[col]).transform(sample[col])

prediction = model.predict(sample)

print("Prediction:", "Promoted" if prediction[0] == 1 else "Not Promoted")
