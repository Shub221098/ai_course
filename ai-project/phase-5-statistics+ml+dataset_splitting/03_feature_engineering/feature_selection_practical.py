import pandas as pd

df = pd.DataFrame({
    "area": [500, 700, 900, 1100, 1300, 1500, 1800, 2000],
    "bedrooms": [1, 1, 2, 2, 3, 3, 4, 4],
    "bathrooms": [1, 1, 2, 2, 2, 3, 3, 4],
    "age": [10, 8, 7, 5, 6, 4, 3, 2],
    "distance": [15, 12, 10, 8, 7, 6, 4, 3],
    "random_noise": [99, 12, 45, 87, 23, 65, 34, 78],
    "price": [25, 30, 42, 48, 58, 65, 78, 90]
})

X = df.drop("price", axis=1)
y = df["price"]

print("Features:")
print(X.columns)

print("\nTarget:")
print(y.name)

print("\nShape:")
print(X.shape)

# Correlation-based Feature Selection
correlation = df.corr()

print(correlation["price"].sort_values(ascending=False))
selected_features = correlation["price"].abs()

selected_features = selected_features[
    (selected_features > 0.5) &
    (selected_features.index != "price")
]

print(selected_features)

# RFECV (Wrapper Method)
from sklearn.feature_selection import RFECV
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold

model = LinearRegression()

cv = KFold(
    n_splits=4,
    shuffle=True,
    random_state=42
)

rfecv = RFECV(
    estimator=model,
    step=1,
    cv=cv,
    scoring="r2",
    min_features_to_select=1
)

rfecv.fit(X, y)

print("Optimal number of features:")
print(rfecv.n_features_)

print("\nSelected features:")
print(X.columns[rfecv.support_])

print("\nFeature ranking:")
print(rfecv.ranking_)

# Lasso Regression (Embedded Method)
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso
from sklearn.feature_selection import SelectFromModel

# 1. Scale the features
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# 2. Create Lasso model
lasso = Lasso(alpha=0.1)

# 3. Train the model
lasso.fit(X_scaled, y)

# 4. Check coefficients
print("--- Lasso Coefficients ---")

for feature, coefficient in zip(X.columns, lasso.coef_):
    print(f"{feature}: {coefficient:.4f}")

# 5. Select features using Lasso
selector = SelectFromModel(
    lasso,
    prefit=True,
)

selected_features = X.columns[selector.get_support()]

print("\n--- Selected Features ---")
print(selected_features)

# Decision Tree Feature Importance (Embedded Method)
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

model = DecisionTreeRegressor(random_state=42)

# 4. Train model
model.fit(X, y)

# 5. Get feature importance
importance = pd.Series(
    model.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

print("--- Feature Importance ---")
print(importance)

# 6. Plot feature importance
importance.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Decision Tree Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Random Forest Feature Importance (Embedded Method)
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# 4. Train model
model.fit(X, y)

# 5. Get feature importance
importance = pd.Series(
    model.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

print("--- Random Forest Feature Importance ---")
print(importance)

# 6. Plot
importance.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Random Forest Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Final Comparison of Feature Selection Methods
# Method	                    Type	                            Result
# Correlation	                Filter	                Linear relationship with price
# RFECV	                        Wrapper	                bedrooms, bathrooms, age
# Lasso	                        Embedded	area, bedrooms, bathrooms had strong non-zero coefficients; age and distance were ~0; random_noise small non-zero
# Decision Tree	                Embedded	distance 0.751, age 0.225, random_noise 0.020
# Random Forest	                Embedded	area 0.258, distance 0.239, bedrooms 0.205, age 0.153, bathrooms 0.102, random_noise 0.043