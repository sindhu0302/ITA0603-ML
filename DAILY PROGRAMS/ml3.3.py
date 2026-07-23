import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

df = pd.DataFrame({
    'CGPA': ['High','High','Medium','Medium','Low','High','Low','Medium','High','Low'],
    'Communication': ['Good','Excellent','Good','Average','Poor','Good','Average','Good','Excellent','Poor'],
    'Internship': ['Yes','Yes','Yes','No','No','No','No','Yes','Yes','Yes'],
    'Programming': ['Good','Excellent','Good','Average','Poor','Good','Average','Excellent','Good','Average'],
    'Placement': ['Yes','Yes','Yes','No','No','Yes','No','Yes','Yes','No']
})

encoders = {}

for col in df.columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

X = df.drop('Placement', axis=1)
y = df['Placement']

model = DecisionTreeClassifier(criterion='entropy')
model.fit(X, y)

new_sample = pd.DataFrame({
    'CGPA': ['High'],
    'Communication': ['Good'],
    'Internship': ['Yes'],
    'Programming': ['Excellent']
})

for col in new_sample.columns:
    new_sample[col] = encoders[col].transform(new_sample[col])

prediction = model.predict(new_sample)

print("Prediction:", encoders['Placement'].inverse_transform(prediction)[0])
