# Find-S Algorithm

data = [
    ['High','Good','Permanent','Yes','Young','Yes'],
    ['High','Good','Permanent','No','Middle','Yes'],
    ['Low','Poor','Temporary','No','Young','No'],
    ['Medium','Good','Permanent','Yes','Middle','Yes'],
    ['High','Average','Temporary','Yes','Old','No'],
    ['Medium','Good','Permanent','No','Young','Yes'],
    ['Low','Good','Permanent','Yes','Middle','Yes'],
    ['Low','Poor','Temporary','Yes','Old','No']
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
