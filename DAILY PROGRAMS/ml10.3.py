from sklearn.mixture import GaussianMixture

X = [
    [800,30],[900,35],[1000,40],[1200,50],[1400,60],
    [1600,75],[1800,90],[2000,105],[2200,120],[2400,135]
]

new = [[1700,82]]

model = GaussianMixture(n_components=2, random_state=42)
model.fit(X)

print("Cluster Labels:", model.predict(X))
print("New Sample Cluster:", model.predict(new))
