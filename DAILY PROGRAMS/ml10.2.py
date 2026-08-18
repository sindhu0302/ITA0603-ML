from sklearn.mixture import GaussianMixture

X = [
    [2,20],[3,25],[4,30],[5,40],[6,50],
    [8,65],[10,75],[12,82],[14,90],[16,96]
]

new = [[9,70]]

model = GaussianMixture(n_components=2, random_state=42)
model.fit(X)

print("Cluster Labels:", model.predict(X))
print("New Sample Cluster:", model.predict(new))
