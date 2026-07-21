data = [
    ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Positive'],
    ['Yes', 'Yes', 'No', 'Yes', 'Yes', 'Positive'],
    ['No', 'Yes', 'Yes', 'No', 'No', 'Negative'],
    ['Yes', 'Yes', 'Yes', 'No', 'Yes', 'Positive'],
    ['No', 'No', 'Yes', 'Yes', 'No', 'Negative'],
    ['Yes', 'Yes', 'No', 'No', 'Yes', 'Positive']
]

h = ['0'] * (len(data[0]) - 1)

for row in data:
    if row[-1] == 'Positive':
        if h[0] == '0':
            h = row[:-1]
        else:
            for i in range(len(h)):
                if h[i] != row[i]:
                    h[i] = '?'
    print(h)

print("Final Hypothesis:", h)
