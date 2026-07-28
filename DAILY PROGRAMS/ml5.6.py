# Find-S Algorithm

data = [
    ['Yes','Yes','Yes','No','Yes','Yes'],
    ['Yes','Yes','Yes','Yes','Yes','Yes'],
    ['No','No','No','No','No','No'],
    ['Yes','No','Yes','No','Yes','Yes'],
    ['No','Yes','No','Yes','No','No'],
    ['Yes','Yes','Yes','No','No','Yes'],
    ['Yes','No','Yes','Yes','Yes','Yes'],
    ['No','No','Yes','No','No','No']
]

hypothesis = ['Ø'] * 5

for row in data:
    if row[-1] == 'Yes':
        if hypothesis == ['Ø'] * 5:
            hypothesis = row[:-1]
        else:
            for i in range(5):
                if hypothesis[i] != row[i]:
                    hypothesis[i] = '?'

print("Final Hypothesis:", hypothesis)
