from sklearn.mixture import GaussianMixture

X = [
    [2,65],[3,70],[4,75],[5,80],[6,85],
    [7,88],[8,90],[9,93],[10,95],[11,98]
]

new = [[7,89]]

model = GaussianMixture(n_components=2, random_state=42)
model.fit(X)

print("Cluster Labels:", model.predict(X))
print("New Sample Cluster:", model.predict(new))
