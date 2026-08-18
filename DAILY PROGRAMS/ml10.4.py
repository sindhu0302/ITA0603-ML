from sklearn.mixture import GaussianMixture

X = [
    [1,3.0],[2,3.8],[3,4.8],[4,6.0],[5,7.5],
    [6,9.0],[7,10.8],[8,12.6],[9,14.5],[10,16.5]
]

new = [[7,11.0]]

model = GaussianMixture(n_components=2, random_state=42)
model.fit(X)

print("Cluster Labels:", model.predict(X))
print("New Sample Cluster:", model.predict(new))
