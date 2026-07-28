# Find-S Algorithm

data = [
    ['Sunny','Warm','Normal','Strong','Warm','Same','Yes'],
    ['Sunny','Warm','High','Strong','Warm','Same','Yes'],
    ['Rainy','Cold','High','Strong','Warm','Change','No'],
    ['Sunny','Warm','High','Strong','Cool','Same','Yes'],
    ['Rainy','Warm','Normal','Weak','Warm','Same','No'],
    ['Sunny','Warm','Normal','Weak','Warm','Same','Yes'],
    ['Cloudy','Warm','Normal','Strong','Warm','Same','Yes'],
    ['Sunny','Cold','High','Weak','Cool','Change','No']
]

hypothesis = ['Ø'] * 6

for row in data:
    if row[-1] == 'Yes':
        if hypothesis == ['Ø'] * 6:
            hypothesis = row[:-1]
        else:
            for i in range(6):
                if hypothesis[i] != row[i]:
                    hypothesis[i] = '?'

print("Final Hypothesis:", hypothesis)
