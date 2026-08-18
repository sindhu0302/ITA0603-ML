from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

X = [[800],[1000],[1200],[1400],[1600],[1800],[2000],[2200],[2400],[2600]]
y = [32,40,52,68,88,112,140,172,208,248]

new = [[1700]]

linear = LinearRegression()
linear.fit(X,y)

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly,y)

print("Linear:", linear.predict(new))
print("Polynomial:", model.predict(poly.transform(new)))
