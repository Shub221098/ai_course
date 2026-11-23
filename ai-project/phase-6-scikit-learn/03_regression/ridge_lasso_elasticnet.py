# Regularized Regression in Scikit-learn : Ridge (L2), Lasso (L1), and ElasticNet

# Regularization Concept:
# Linear Regression
#        ↓
# Overfitting?
#        ↓
# Regularization
# ┌──────┼──────┐
# ▼      ▼      ▼
# Ridge  Lasso  ElasticNet
# (L2)   (L1)   (L1 + L2)
# Shrink Feature Shrink +
# coefs  Select  Selection


# Linear Regression
#        ↓
# Overfitting?
#        ↓
# Regularization
#     ↙       ↘
#  Ridge      Lasso
#   L2          L1
#   ↓           ↓
# Shrink      Shrink
# coefficients coefficients
#               ↓
#          Some → 0
#               ↓
#       Feature Selection

# Practical Example: Ridge Regression
import pandas as pd
from sklearn.linear_model import Ridge

df = pd.DataFrame({
    "area": [500, 700, 900, 1100, 1300, 1500],
    "bedrooms": [1, 1, 2, 2, 3, 3],
    "price": [25, 30, 42, 48, 58, 65]
})

X = df[["area", "bedrooms"]]
y = df["price"]

model = Ridge(alpha=1)

model.fit(X, y)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

# Practical Example: Lasso Regression
import pandas as pd
from sklearn.linear_model import Lasso

model = Lasso(alpha=1)

model.fit(X, y)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

# Practical Example: Ridge Regression with Feature Scaling using Pipeline
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge

model = Pipeline([
    ("scaler", StandardScaler()),
    ("ridge", Ridge(alpha=1))
])

from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score

for alpha in [0.01, 0.1, 1, 10]:
    
    model = Ridge(alpha=alpha)
    
    scores = cross_val_score(
        model,
        X,
        y,
        cv=5,
        scoring="r2"
    )
    
    print(
        "Alpha:", alpha,
        "Mean CV R²:", scores.mean()
    )
    
# Cross-validation + Regularization

# Full Dataset
#      ↓
# Train/Test Split
#      ↓
#   ┌───────────────┐
#   │               │
# Train            Test
#   ↓                ↓
# CV               FINAL
#   ↓              EVALUATION
# Choose model

# ------------------------------------------------------------------------

import pandas as pd
from sklearn.linear_model import Ridge, Lasso, ElasticNet
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

df = pd.DataFrame({
    "area": [500, 700, 900, 1100, 1300, 1500],
    "bedrooms": [1, 1, 2, 2, 3, 3],
    "bathrooms": [1, 1, 2, 2, 2, 3],
    "price": [25, 30, 42, 48, 58, 65]
})

X = df[["area", "bedrooms", "bathrooms"]]
y = df["price"]

# 1. Ridge Regression (L2 Penalty)
# Minimizes Loss + alpha * Σ(w_i^2)
ridge_pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", Ridge(alpha=1.0))
])
ridge_pipeline.fit(X, y)
print("--- Ridge (L2) Coefficients ---")
print(dict(zip(X.columns, ridge_pipeline.named_steps["model"].coef_)))

# 2. Lasso Regression (L1 Penalty)
# Minimizes Loss + alpha * Σ|w_i| (Can zero out unimportant coefficients)
lasso_pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", Lasso(alpha=0.5))
])
lasso_pipeline.fit(X, y)
print("\n--- Lasso (L1) Coefficients ---")
print(dict(zip(X.columns, lasso_pipeline.named_steps["model"].coef_)))

# 3. ElasticNet (L1 + L2 Penalty combination)
# l1_ratio controls balance between L1 and L2 (1.0 = Lasso, 0.0 = Ridge)
elastic_pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", ElasticNet(alpha=0.5, l1_ratio=0.5))
])
elastic_pipeline.fit(X, y)
print("\n--- ElasticNet Coefficients ---")
print(dict(zip(X.columns, elastic_pipeline.named_steps["model"].coef_)))

