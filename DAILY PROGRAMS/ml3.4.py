import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

df = pd.DataFrame({
    'Income': ['High','High','Medium','Low','Medium','High','Low','Medium','High','Low'],
    'Credit Score': ['Good','Good','Good','Poor','Average','Average','Poor','Good','Good','Average'],
    'Employment': ['Permanent','Permanent','Permanent','Temporary','Permanent','Temporary','Temporary','Permanent','Permanent','Temporary'],
    'Property': ['Yes','No','Yes','No','No','Yes','Yes','Yes','Yes','No'],
    'Loan Approved': ['Yes','Yes','Yes','No','Yes','No','No','Yes','Yes','No']
})

encoders = {}

for col in df.columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

X = df.drop('Loan Approved', axis=1)
y = df['Loan Approved']

model = DecisionTreeClassifier(criterion='entropy')
model.fit(X, y)

new_sample = pd.DataFrame({
    'Income': ['Medium'],
    'Credit Score': ['Good'],
    'Employment': ['Permanent'],
    'Property': ['Yes']
})

for col in new_sample.columns:
    new_sample[col] = encoders[col].transform(new_sample[col])

prediction = model.predict(new_sample)

print("Prediction:", encoders['Loan Approved'].inverse_transform(prediction)[0])
