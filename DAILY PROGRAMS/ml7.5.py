# 7.4 Logistic Regression - Employee Promotion

from sklearn.linear_model import LogisticRegression

X = [
    [10,95,50],[8,90,45],[7,88,40],[3,65,20],[2,60,18],
    [9,93,48],[4,70,25],[8,89,42],[2,58,15],[6,85,38]
]

y = [1,1,1,0,0,1,0,1,0,1]

model = LogisticRegression()
model.fit(X, y)

print("Predicted Class:", model.predict([[7,90,44]]))
