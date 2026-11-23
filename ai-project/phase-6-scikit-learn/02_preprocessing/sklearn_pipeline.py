# Scikit-learn Pipeline : Chaining preprocessing transformers and estimators seamlessly

# Pipeline Architecture
# 
#    Raw Data (X)
#         │
#         ▼
#   [Step 1: StandardScaler]
#         │
#         ▼
#   [Step 2: LinearRegression / Classifier]
#         │
#         ▼
#    Final Output (Predictions)

import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split

df = pd.DataFrame({
    "area": [500, 700, 900, 1100, 1300, 1500, 1800, 2000],
    "bedrooms": [1, 1, 2, 2, 3, 3, 4, 4],
    "price": [25, 30, 42, 48, 58, 65, 78, 90]
})

X = df[["area", "bedrooms"]]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build Scikit-learn Pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", Ridge(alpha=1.0))
])

# Fit pipeline on training data (fits scaler AND model automatically)
pipeline.fit(X_train, y_train)

# Predict on test data (transforms test data AND predicts automatically)
predictions = pipeline.predict(X_test)

print("--- Pipeline Model Predictions ---")
print("Actual Test Prices:", y_test.values)
print("Pipeline Predictions:", predictions)

