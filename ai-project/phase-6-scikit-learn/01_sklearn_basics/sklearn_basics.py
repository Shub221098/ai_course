# Scikit-learn Basics : Core workflow of Scikit-learn estimators and transformers

# Scikit-learn Workflow
# 
#         Dataset (X, y)
#              │
#      ┌───────┴───────┐
#      ▼               ▼
#   Features (X)   Target (y)
# (2D Matrix)     (1D Array)
#      │               │
#      └───────┬───────┘
#              ▼
#         fit(X, y)        <-- Model learns patterns/parameters
#              │
#      ┌───────┴───────┐
#      ▼               ▼
# predict(X_new)   transform(X_new)
# (Estimators)     (Transformers)

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# 1. Dataset Creation (X and y)
# X must be a 2D matrix (DataFrame or 2D array) representing Independent Features
# y must be a 1D vector (Series or 1D array) representing Dependent Target
df = pd.DataFrame({
    "area": [500, 700, 900, 1100, 1300, 1500],
    "bedrooms": [1, 1, 2, 2, 3, 3],
    "price": [25, 30, 42, 48, 58, 65]
})

X = df[["area", "bedrooms"]]  # 2D Feature Matrix
y = df["price"]              # 1D Target Vector

print("--- Feature Matrix (X) ---")
print(X)
print("\n--- Target Vector (y) ---")
print(y)


# 2. Fit and Predict (Estimators - Models)
# fit()     → Data se parameters learn karta hai (e.g. slope, intercept)
# predict() → Unseen inputs ke liye target predict karta hai
model = LinearRegression()

# Model training
model.fit(X, y)
print(f"\nModel Learned Coefficients (m): {model.coef_}")
print(f"Model Learned Intercept (b): {model.intercept_}")

# Prediction
new_data = [[1200, 2]]
prediction = model.predict(new_data)
print(f"Predicted Price for area=1200, bedrooms=2: {prediction[0]:.2f}")


# 3. Fit and Transform (Transformers - Scalers / Encoders)
# fit()           → Data statistics learn karta hai (e.g. mean, std)
# transform()     → Learn kiye stats se data ko modify / scale karta hai
# fit_transform() → Donon steps ek saath execute karta hai
scaler = StandardScaler()

# Scaler fit and transform
scaled_X = scaler.fit_transform(X)
print("\n--- Scaled Features (StandardScaler) ---")
print(scaled_X)

