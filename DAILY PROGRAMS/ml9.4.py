from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

X = [[5],[10],[15],[20],[25],[30],[35],[40],[45],[50]]
y = [1.2,2.5,4.1,6.2,8.8,11.9,15.5,19.6,24.2,29.3]

new = [[32]]

linear = LinearRegression()
linear.fit(X,y)

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly,y)

print("Linear:", linear.predict(new))
print("Polynomial:", model.predict(poly.transform(new)))
