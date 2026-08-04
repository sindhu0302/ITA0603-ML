from sklearn.linear_model import LogisticRegression
import pandas as pd

data = {
    'Income': [8, 7, 6, 4, 3, 9, 5, 8, 4, 7],
    'CreditScore': [780, 760, 730, 620, 590, 810, 650, 770, 610, 750],
    'LoanAmount': [5, 4, 5, 8, 9, 4, 7, 5, 8, 6],
    'LoanApproved': [1, 1, 1, 0, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df[['Income', 'CreditScore', 'LoanAmount']]
y = df['LoanApproved']

model = LogisticRegression()
model.fit(X, y)

new_data = pd.DataFrame({
    'Income': [7],
    'CreditScore': [760],
    'LoanAmount': [5]
})

prediction = model.predict(new_data)

print("Prediction:", prediction[0])
