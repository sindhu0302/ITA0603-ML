# Find-S Algorithm

data = [
    ['Yes','Yes','Yes','Yes','Yes','Positive'],
    ['Yes','Yes','No','Yes','Yes','Positive'],
    ['No','Yes','Yes','No','No','Negative'],
    ['Yes','Yes','Yes','No','Yes','Positive'],
    ['No','No','Yes','Yes','No','Negative'],
    ['Yes','Yes','No','No','Yes','Positive'],
    ['Yes','No','Yes','Yes','Yes','Positive'],
    ['No','No','No','No','No','Negative']
]

hypothesis = ['Ø'] * 5

for row in data:
    if row[-1] == 'Positive':
        if hypothesis == ['Ø'] * 5:
            hypothesis = row[:-1]
        else:
            for i in range(5):
                if hypothesis[i] != row[i]:
                    hypothesis[i] = '?'

print("Final Hypothesis:", hypothesis)
