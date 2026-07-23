import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

df = pd.DataFrame({
    'Experience': ['High','High','Medium','Low','Medium','Low','High','Medium','High','Low'],
    'Performance': ['Excellent','Good','Good','Average','Excellent','Poor','Good','Average','Excellent','Poor'],
    'Leadership': ['Yes','Yes','No','No','Yes','No','Yes','No','Yes','No'],
    'Training': ['Yes','Yes','Yes','No','Yes','No','No','Yes','Yes','Yes'],
    'Promotion': ['Yes','Yes','Yes','No','Yes','No','Yes','No','Yes','No']
})

encoders = {}

for col in df.columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

X = df.drop('Promotion', axis=1)
y = df['Promotion']

model = DecisionTreeClassifier(criterion='entropy')
model.fit(X, y)

new_sample = pd.DataFrame({
    'Experience': ['Medium'],
    'Performance': ['Good'],
    'Leadership': ['Yes'],
    'Training': ['Yes']
})

for col in new_sample.columns:
    new_sample[col] = encoders[col].transform(new_sample[col])

prediction = model.predict(new_sample)

print("Prediction:", encoders['Promotion'].inverse_transform(prediction)[0])
