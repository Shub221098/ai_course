# Regression Metrics in Scikit-learn : MAE, MSE, RMSE, R²

# Model Evaluation Metrics Formulas:
# MAE  (Mean Absolute Error)     = Σ |y_actual - y_pred| / n
# MSE  (Mean Squared Error)      = Σ (y_actual - y_pred)^2 / n
# RMSE (Root Mean Squared Error) = √MSE
# R²   (Coefficient of Determination) = 1 - (SSR / SST)

import numpy as np
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

y_actual = [25.0, 30.0, 42.0, 48.0, 58.0, 65.0]
y_predicted = [24.0, 32.0, 40.0, 50.0, 56.0, 68.0]

mae = mean_absolute_error(y_actual, y_predicted)
mse = mean_squared_error(y_actual, y_predicted)
rmse = np.sqrt(mse)
r2 = r2_score(y_actual, y_predicted)

print("--- Regression Evaluation Metrics ---")
print(f"MAE  (Mean Absolute Error)     : {mae:.4f}")
print(f"MSE  (Mean Squared Error)      : {mse:.4f}")
print(f"RMSE (Root Mean Squared Error) : {rmse:.4f}")
print(f"R² Score (Variance Explained)  : {r2:.4f}")

