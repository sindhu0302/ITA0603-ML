data = [
    ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Positive'],
    ['Yes', 'Yes', 'No', 'Yes', 'Yes', 'Positive'],
    ['No', 'Yes', 'Yes', 'No', 'No', 'Negative'],
    ['Yes', 'Yes', 'Yes', 'No', 'Yes', 'Positive'],
    ['No', 'No', 'Yes', 'Yes', 'No', 'Negative'],
    ['Yes', 'Yes', 'No', 'No', 'Yes', 'Positive'],
    ['Yes', 'No', 'Yes', 'Yes', 'Yes', 'Positive'],
    ['No', 'No', 'No', 'No', 'No', 'Negative']
]

S = data[0][:-1]
G = ['?'] * len(S)

for x in data:
    if x[-1] == 'Positive':
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
