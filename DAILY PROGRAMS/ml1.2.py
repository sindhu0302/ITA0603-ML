data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Same', 'Yes'],
    ['Rainy', 'Warm', 'Normal', 'Weak', 'Warm', 'Same', 'No'],
    ['Sunny', 'Warm', 'Normal', 'Weak', 'Warm', 'Same', 'Yes']
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
