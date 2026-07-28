# Find-S Algorithm

data = [
    ['High','Good','Yes','Good','High','Yes'],
    ['High','Excellent','Yes','Good','High','Yes'],
    ['Medium','Average','No','Average','Medium','No'],
    ['High','Good','Yes','Excellent','High','Yes'],
    ['Low','Poor','No','Average','Low','No'],
    ['High','Good','Yes','Good','Medium','Yes'],
    ['Medium','Good','Yes','Good','High','Yes'],
    ['Low','Average','No','Poor','Medium','No']
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
