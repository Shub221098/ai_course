# Linear Regression in Scikit-learn : Simple & Multiple Linear Regression

# Simple Linear Regression: y = m*x + b
# Multiple Linear Regression: y = b0 + b1*x1 + b2*x2 + ... + bn*xn


# Supervised Learning : Supervised Learning mein training data ke saath correct answer/target already available hota hai.

# Supervised Learning
# │
# ├── Regression => Target continuous numerical value hota hai.
# │
# └── Classification => Target discrete category/label hota hai.

# Regression Example: House price prediction, Stock price prediction, Temperature forecasting.
# Common algorithms: Linear Regression, Decision Tree Regressor, Random Forest Regressor

# Classification Example: Email spam detection, Disease diagnosis, Sentiment analysis.
# Common algorithms: Logistic Regression, Decision Tree Classifier, Random Forest Classifier, SVM, KNN


########## Linear Regression ##########
# Linear Regression ek supervised learning algorithm hai jo continuous target variable ko predict karta hai.
# Linear Regression ka goal: ek straight line find karna jo data points ke beech best fit ho aur target variable ko predict kare.

# Simple Linear Regression: y = mx + b
# Where:

# y → predicted value
# x → input feature
# m → slope
# b → intercept

import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.DataFrame({
    "area": [500, 700, 900, 1100, 1300, 1500],
    "price": [25, 30, 42, 48, 58, 65]
})

# Feature
X = df[["area"]]

# Target
y = df["price"]

# Create model
model = LinearRegression()

# Train
model.fit(X, y)

# Predict
prediction = model.predict([[1200]])

print("Predicted price:", prediction[0])

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# Multiple Linear Regression: Multiple Linear Regression mein ek se zyada input features hote hain.
# Model in features ke combination se target variable ko predict karta hai.
# goal: ek hyperplane find karna jo data points ke beech best fit ho aur target variable ko predict kare.

# Formula: y = b0 + b1*x1 + b2*x2 + ... + bn*xn

df = pd.DataFrame({
    "area": [500, 700, 900, 1100, 1300, 1500, 1800, 2000],
    "bedrooms": [1, 1, 2, 2, 3, 3, 4, 4],
    "bathrooms": [1, 1, 2, 2, 2, 3, 3, 4],
    "age": [10, 8, 7, 5, 6, 4, 3, 2],
    "price": [25, 30, 42, 48, 58, 65, 78, 90]
})

# Features
X = df[["area", "bedrooms", "bathrooms", "age"]]

# Target
y = df["price"]

# Create model
model = LinearRegression()

# Train
model.fit(X, y)

# New property
new_property = [[1200, 3, 2, 5]]

# Predict
prediction = model.predict(new_property)

print("Predicted price:", prediction[0])

print("\nCoefficients:")
for feature, coefficient in zip(X.columns, model.coef_):
    print(feature, ":", coefficient)

print("\nIntercept:", model.intercept_)

# Linear Regression coefficient = model prediction mein feature ke unit change ka estimated effect, while other included features are held constant.

# Train-Test Split : abi tak humne model ko train karne ke liye saara data use kiya hai. Lekin real-world mein humein model ko unseen data par test karna hota hai. Isliye hum data ko training aur testing sets mein split karte hain.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.DataFrame({
    "area": [500, 700, 900, 1100, 1300, 1500, 1800, 2000],
    "bedrooms": [1, 1, 2, 2, 3, 3, 4, 4],
    "price": [25, 30, 42, 48, 58, 65, 78, 90]
})

X = df[["area", "bedrooms"]]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training data:")
print(X_train)
# Training data:
#    area  bedrooms
# 0   500         1
# 7  2000         4
# 2   900         2
# 4  1300         3
# 3  1100         2
# 6  1800         4

print("\nTraining target values:")
print(y_train)
# Training target values:
# 0    25
# 7    90
# 2    42
# 4    58
# 3    48
# 6    78
# Name: price, dtype: int64

print("\nTesting data:")
print(X_test)
# Testing data:
#    area  bedrooms
# 1   700         1
# 5  1500         3

print("\nTesting target values:")
print(y_test)
# Testing target values:
# 1    30
# 5    65
# Name: price, dtype: int64

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Actual prices:", y_test.values) 
print("Predicted prices:", y_pred) # Predicted prices: [33.078125 66.890625]

# Errors in prices : [3.078125 1.890625]
# Currenly we are calculatin metric by subtracting actual and predicted values. But we can also use sklearn metrics to calculate the error.

# Model Prediction
#       ↓
# Actual vs Predicted
#       ↓
# How much error?
#       ↓
# MAE
# MSE
# RMSE
# R²

# Model Evaluation Metrics:
# Mean Absolute Error (MAE): MAE actual aur predicted values ke beech average absolute difference ko measure karta hai. Ye error ka average magnitude batata hai, bina direction ke.
# Formula: MAE = Actaul - Predicted / n

# MAE = (3.08 + 1.89) / 2 ≈ 2.485
from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(y_test, y_pred)

print("MAE:", mae)

# Mean Squared Error (MSE): MSE actual aur predicted values ke beech average squared difference ko measure karta hai. Ye larger errors ko zyada penalize karta hai.
# Formula: MSE = (Actual - Predicted)² / n
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, y_pred)

print("MSE:", mse)

# Root Mean Squared Error (RMSE): RMSE MSE ka square root hai.
# Formula: RMSE = √MSE
import numpy as np

rmse = np.sqrt(mse)

print("RMSE:", rmse)

# R² (R-squared): R² model ke performance ko measure karta hai. Ye batata hai ki kitna variance target variable mein explain ho raha hai input features ke through. 
# R² ka range commonly:

# 1      → perfect fit
# 0      → baseline mean ke around
# < 0    → very poor model possible
from sklearn.metrics import r2_score

r2 = r2_score(y_test, y_pred)

print("R²:", r2)

# Overfitting & Underfitting

# Underfitting: Model ne data ka pattern properly learn hi nahi kiya.
# Training Performance → Poor
# Testing Performance  → Poor

# Overfitting: Model ne training data ka pattern itna zyada learn kar liya ki wo testing data ke liye generalize nahi kar pa raha.
# Training Performance → Excellent
# Testing Performance  → Poor

# Bias vs Variance — ye explain karega ki underfitting aur overfitting actually kyun hote hain.

# Bias = Model ki assumptions ki wajah se hone wali error.
# High Bias → Underfitting

# Variance = Training data change hone par model ka behavior kitna change hota hai.
# High Variance → Overfitting

# Regularization: Prediction error kam karo, but coefficients ko unnecessarily bada mat hone do
# Techniques:  Ridge(L2) & Lasso(L1)
# Ridge → Reduce coefficients
# Lasso → Leave some coefficients out
# Model ko unnecessarily complex hone se rokna, taaki overfitting kam ho.


# alpha kya hai? => ye regularization strength ko control karta hai. Higher alpha → more regularization → coefficients shrink more.
# alpha too small → Overfitting risk
# alpha too large → Underfitting risk


# ---------------------------------------------------------------------------

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Dataset
df = pd.DataFrame({
    "area": [500, 700, 900, 1100, 1300, 1500, 1800, 2000],
    "bedrooms": [1, 1, 2, 2, 3, 3, 4, 4],
    "bathrooms": [1, 1, 2, 2, 2, 3, 3, 4],
    "age": [10, 8, 7, 5, 6, 4, 3, 2],
    "price": [25, 30, 42, 48, 58, 65, 78, 90]
})

# 1. Simple Linear Regression (Single Feature)
X_simple = df[["area"]]
y = df["price"]

model_simple = LinearRegression()
model_simple.fit(X_simple, y)
print("--- Simple Linear Regression ---")
print("Slope (m):", model_simple.coef_[0])
print("Intercept (b):", model_simple.intercept_)

# 2. Multiple Linear Regression (Multiple Features)
X_multi = df[["area", "bedrooms", "bathrooms", "age"]]
X_train, X_test, y_train, y_test = train_test_split(X_multi, y, test_size=0.25, random_state=42)

model_multi = LinearRegression()
model_multi.fit(X_train, y_train)

y_pred = model_multi.predict(X_test)

print("\n--- Multiple Linear Regression ---")
print("Coefficients:", dict(zip(X_multi.columns, model_multi.coef_)))
print("Intercept:", model_multi.intercept_)
print("Test Set R² Score:", r2_score(y_test, y_pred))

