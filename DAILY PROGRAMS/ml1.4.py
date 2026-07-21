data = [
    ['High', 'Good', 'Yes', 'Good', 'High', 'Yes'],
    ['High', 'Excellent', 'Yes', 'Good', 'High', 'Yes'],
    ['Medium', 'Average', 'No', 'Average', 'Medium', 'No'],
    ['High', 'Good', 'Yes', 'Excellent', 'High', 'Yes'],
    ['Low', 'Poor', 'No', 'Average', 'Low', 'No'],
    ['High', 'Good', 'Yes', 'Good', 'Medium', 'Yes']
]

h = ['0'] * (len(data[0]) - 1)

for row in data:
    if row[-1] == 'Yes':
        if h[0] == '0':
            h = row[:-1]
        else:
            for i in range(len(h)):
                if h[i] != row[i]:
                    h[i] = '?'
    print(h)

print("Final Hypothesis:", h)
