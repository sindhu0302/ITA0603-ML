data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Same', 'Yes'],
    ['Rainy', 'Warm', 'Normal', 'Weak', 'Warm', 'Same', 'No'],
    ['Sunny', 'Warm', 'Normal', 'Weak', 'Warm', 'Same', 'Yes'],
    ['Cloudy', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Cold', 'High', 'Weak', 'Cool', 'Change', 'No']
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
