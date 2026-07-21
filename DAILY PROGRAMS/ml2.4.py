data = [
    ['High', 'Good', 'Yes', 'Good', 'High', 'Yes'],
    ['High', 'Excellent', 'Yes', 'Good', 'High', 'Yes'],
    ['Medium', 'Average', 'No', 'Average', 'Medium', 'No'],
    ['High', 'Good', 'Yes', 'Excellent', 'High', 'Yes'],
    ['Low', 'Poor', 'No', 'Average', 'Low', 'No'],
    ['High', 'Good', 'Yes', 'Good', 'Medium', 'Yes'],
    ['Medium', 'Good', 'Yes', 'Good', 'High', 'Yes'],
    ['Low', 'Average', 'No', 'Poor', 'Medium', 'No']
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
