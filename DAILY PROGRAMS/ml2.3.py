data = [
    ['High', 'Good', 'Permanent', 'Yes', 'Young', 'Yes'],
    ['High', 'Good', 'Permanent', 'No', 'Middle', 'Yes'],
    ['Low', 'Poor', 'Temporary', 'No', 'Young', 'No'],
    ['Medium', 'Good', 'Permanent', 'Yes', 'Middle', 'Yes'],
    ['High', 'Average', 'Temporary', 'Yes', 'Old', 'No'],
    ['Medium', 'Good', 'Permanent', 'No', 'Young', 'Yes'],
    ['Low', 'Good', 'Permanent', 'Yes', 'Middle', 'Yes'],
    ['Low', 'Poor', 'Temporary', 'Yes', 'Old', 'No']
]

S = data[0][:-1]
G = ['?'] * len(S)

for x in data:
    if x[-1] == 'Yes':
        for i in range(len(S)):
            if S[i] != x[i]:
                S[i] = '?'
    else:
        for i in range(len(S)):
            if S[i] != x[i]:
                G[i] = S[i]
    print("S =", S, "G =", G)

print("Final S =", S)
print("Final G =", G)
