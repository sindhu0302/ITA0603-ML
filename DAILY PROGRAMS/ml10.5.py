from sklearn.mixture import GaussianMixture

X = [
    [40,4.5],[50,5.0],[60,5.6],[70,6.5],[80,7.8],
    [90,9.2],[100,10.8],[110,12.5],[120,14.3],[130,16.2]
]

new = [[95,10.0]]

model = GaussianMixture(n_components=2, random_state=42)
model.fit(X)

print("Cluster Labels:", model.predict(X))
print("New Sample Cluster:", model.predict(new))
