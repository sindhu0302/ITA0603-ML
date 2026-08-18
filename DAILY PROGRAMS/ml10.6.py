from sklearn.mixture import GaussianMixture

X = [[1],[2],[3],[10],[11],[12]]

model = GaussianMixture(n_components=2, random_state=42)
model.fit(X)

print("Cluster Labels:", model.predict(X))
