from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
import pandas as pd

# Dataset
data = {
    'Outlook':['Sunny','Sunny','Overcast','Rain','Rain','Rain','Overcast','Sunny',
               'Sunny','Rain','Sunny','Overcast','Overcast','Rain'],
    'Temperature':['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild',
                   'Cool','Mild','Mild','Mild','Hot','Mild'],
    'Humidity':['High','High','High','High','Normal','Normal','Normal','High',
                'Normal','Normal','Normal','High','Normal','High'],
    'Wind':['Weak','Strong','Weak','Weak','Weak','Strong','Strong','Weak',
            'Weak','Weak','Strong','Strong','Weak','Strong'],
    'PlayTennis':['No','No','Yes','Yes','Yes','No','Yes','No',
                  'Yes','Yes','Yes','Yes','Yes','No']
}

df = pd.DataFrame(data)

# Label Encoding
le = LabelEncoder()

for col in df.columns:
    df[col] = le.fit_transform(df[col])

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Train Naïve Bayes model
model = GaussianNB()
model.fit(X, y)

# Prediction
prediction = model.predict(X)

# Evaluation
print("Confusion Matrix")
print(confusion_matrix(y, prediction))

print("Accuracy:", accuracy_score(y, prediction))
