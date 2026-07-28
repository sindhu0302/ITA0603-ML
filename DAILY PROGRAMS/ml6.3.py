from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Dataset
data = {
    'CGPA':['High','High','Medium','Medium','Low','High','Low','Medium','High','Low'],
    'Communication':['Good','Excellent','Good','Average','Poor','Good','Average','Good','Excellent','Poor'],
    'Internship':['Yes','Yes','Yes','No','No','No','No','Yes','Yes','Yes'],
    'Programming':['Good','Excellent','Good','Average','Poor','Good','Average','Excellent','Good','Average'],
    'Placement':['Yes','Yes','Yes','No','No','Yes','No','Yes','Yes','No']
}

df = pd.DataFrame(data)

# Encode categorical data
encoder = {}
for column in df.columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    encoder[column] = le

# Features and Target
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Train model
model = GaussianNB()
model.fit(X, y)

# New Sample
sample = pd.DataFrame({
    'CGPA':['High'],
    'Communication':['Good'],
    'Internship':['Yes'],
    'Programming':['Excellent']
})

# Encode sample
for column in sample.columns:
    sample[column] = encoder[column].transform(sample[column])

# Prediction
prediction = model.predict(sample)

# Convert prediction back to original label
result = encoder['Placement'].inverse_transform(prediction)

print("Prediction:", result[0])
