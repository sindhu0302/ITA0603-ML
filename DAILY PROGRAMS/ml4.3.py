import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neural_network import MLPClassifier

data = {
    'Income': ['High','High','Medium','Medium','Low','Low','High','Medium','High','Low'],
    'Credit Score': ['Good','Good','Good','Average','Poor','Average','Average','Good','Good','Poor'],
    'Employment': ['Permanent','Permanent','Permanent','Permanent','Temporary','Temporary','Permanent','Temporary','Permanent','Temporary'],
    'Property': ['Yes','No','Yes','No','No','Yes','Yes','No','Yes','Yes'],
    'Loan Approved': ['Yes','Yes','Yes','Yes','No','No','Yes','No','Yes','No']
}

df = pd.DataFrame(data)

le = LabelEncoder()

for col in df.columns:
    df[col] = le.fit_transform(df[col])

X = df.drop('Loan Approved', axis=1)
y = df['Loan Approved']

model = MLPClassifier(hidden_layer_sizes=(4,), max_iter=5000, random_state=42)
model.fit(X, y)

sample = pd.DataFrame({
    'Income': ['Medium'],
    'Credit Score': ['Good'],
    'Employment': ['Permanent'],
    'Property': ['Yes']
})

for col in sample.columns:
    sample[col] = LabelEncoder().fit(data[col]).transform(sample[col])

prediction = model.predict(sample)

print("Prediction:", "Yes" if prediction[0] == 1 else "No")
