data = [
    ['High', 'Good', 'Permanent', 'Yes', 'Young', 'Yes'],
    ['High', 'Good', 'Permanent', 'No', 'Middle', 'Yes'],
    ['Low', 'Poor', 'Temporary', 'No', 'Young', 'No'],
    ['Medium', 'Good', 'Permanent', 'Yes', 'Middle', 'Yes'],
    ['High', 'Average', 'Temporary', 'Yes', 'Old', 'No'],
    ['High', 'Good', 'Permanent', 'Yes', 'Middle', 'Yes']
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
