from sklearn.linear_model import LinearRegression
import pandas as pd

data = {
    'Experience': [1,2,3,4,5,6,7,8,9,10],
    'Education': [15,15,16,16,17,17,18,18,18,19],
    'SkillScore': [60,65,70,75,80,82,85,88,90,94],
    'Salary': [3.5,4.2,5.1,6.0,7.2,8.0,9.1,10.0,11.2,12.5]
}

df = pd.DataFrame(data)

X = df[['Experience', 'Education', 'SkillScore']]
y = df['Salary']

model = LinearRegression()
model.fit(X, y)

new_data = pd.DataFrame({
    'Experience': [7],
    'Education': [18],
    'SkillScore': [86]
})

prediction = model.predict(new_data)

print("Predicted Salary:", round(prediction[0], 2), "Lakhs")
