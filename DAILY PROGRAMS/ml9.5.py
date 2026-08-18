from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

X = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
y = [3.0,3.8,4.9,6.3,8.0,10.2,12.9,16.1,19.8,24.0]

new = [[7.5]]

linear = LinearRegression()
linear.fit(X,y)

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly,y)

print("Linear:", linear.predict(new))
print("Polynomial:", model.predict(poly.transform(new)))
