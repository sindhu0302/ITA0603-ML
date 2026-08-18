from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

X = [[40],[50],[60],[70],[80],[90],[100],[110],[120],[130]]
y = [4.5,4.8,5.2,5.9,6.8,8.0,9.5,11.2,13.4,16.0]

new = [[95]]

linear = LinearRegression()
linear.fit(X,y)

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly,y)

print("Linear:", linear.predict(new))
print("Polynomial:", model.predict(poly.transform(new)))
