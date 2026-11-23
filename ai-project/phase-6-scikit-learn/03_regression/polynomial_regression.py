# Polynomial Regression in Scikit-learn : Fitting non-linear curves using PolynomialFeatures + LinearRegression

# Polynomial Transformation:
# Input x → PolynomialFeatures(degree=2) → [x, x^2, x1*x2, etc.]

# Polynomial Regression : Polynomial Regression ek transformed Linear Regression hi hai.
# Ye input features ko polynomial terms mein transform karta hai, taaki non-linear relationships ko bhi linear model ke through capture kiya ja sake.

import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

df = pd.DataFrame({
    "area": [500, 700, 900, 1100, 1300, 1500],
    "price": [20, 28, 40, 55, 75, 100]
})

X = df[["area"]]
y = df["price"]

poly = PolynomialFeatures(
    degree=2,
    include_bias=False
)

X_poly = poly.fit_transform(X)

print(X_poly)

model = LinearRegression()

model.fit(X_poly, y)

new_area = [[1200]]

new_area_poly = poly.transform(new_area)

prediction = model.predict(new_area_poly)

print("Predicted price:", prediction[0])


# -----------------------------------------------------------------------

import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

df = pd.DataFrame({
    "area": [500, 700, 900, 1100, 1300, 1500],
    "price": [20, 28, 40, 55, 75, 100]
})

X = df[["area"]]
y = df["price"]

# Polynomial Regression Pipeline (Degree = 2)
poly_model = Pipeline([
    ("poly", PolynomialFeatures(degree=2, include_bias=False)),
    ("linear", LinearRegression())
])

poly_model.fit(X, y)

print("--- Polynomial Regression (Degree 2) ---")
print("Transformed Feature Names:", poly_model.named_steps["poly"].get_feature_names_out(["area"]))
print("Model Coefficients:", poly_model.named_steps["linear"].coef_)
print("Model Intercept:", poly_model.named_steps["linear"].intercept_)

# Predict for new area
new_area = [[1200]]
pred_price = poly_model.predict(new_area)
print(f"\nPredicted price for area=1200: {pred_price[0]:.2f}")

