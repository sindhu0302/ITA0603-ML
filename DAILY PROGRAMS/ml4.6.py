import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neural_network import MLPClassifier

data = {
    'Contains Link': ['Yes','Yes','No','Yes','No','Yes','Yes','No','Yes','No'],
    'Offer Words': ['Yes','Yes','No','No','Yes','Yes','No','No','Yes','No'],
    'Unknown Sender': ['Yes','Yes','No','Yes','No','Yes','Yes','Yes','No','No'],
    'Attachment': ['No','Yes','No','No','Yes','No','Yes','No','No','Yes'],
    'Many Recipients': ['Yes','Yes','No','Yes','No','No','Yes','No','Yes','No'],
    'Spam': ['Spam','Spam','Not Spam','Spam','Not Spam','Spam','Spam','Not Spam','Spam','Not Spam']
}

df = pd.DataFrame(data)

le = LabelEncoder()

for col in df.columns:
    df[col] = le.fit_transform(df[col])

X = df.drop('Spam', axis=1)
y = df['Spam']

model = MLPClassifier(hidden_layer_sizes=(4,), max_iter=5000, random_state=42)
model.fit(X, y)

sample = pd.DataFrame({
    'Contains Link': ['Yes'],
    'Offer Words': ['Yes'],
    'Unknown Sender': ['Yes'],
    'Attachment': ['No'],
    'Many Recipients': ['Yes']
})

for col in sample.columns:
    sample[col] = LabelEncoder().fit(data[col]).transform(sample[col])

prediction = model.predict(sample)

print("Prediction:", "Spam" if prediction[0] == 1 else "Not Spam")
