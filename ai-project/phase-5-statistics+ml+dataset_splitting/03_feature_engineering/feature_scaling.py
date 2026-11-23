# Feature Scaling: Different numerical features ko comparable scale/range par lana.

import pandas as pd

df = pd.DataFrame({
    "area": [500, 1000, 1500, 2000],
    "age": [2, 4, 6, 8],
    "price": [30, 50, 70, 90]
})

print(df)

# Ranges of features are completely different here.
# area  → 500–2000
# age   → 2–8
# price → 30–90
# Agar model distance-based hai, to area ka numerical difference bahut bada hai compared to age.
# So model ke calculation mein large-scale feature dominate kar sakta hai.

# Kaunse ML models scaling se affected hote hain?
# Scaling usually important for:
# KNN
# K-Means
# SVM
# Linear Regression
# Logistic Regression
# Neural Networks
# PCA

# Especially algorithms involving:

# distance
# gradients
# magnitude
# regularization
# variance

# Tree-based models generally scaling ke bina bhi kaam karte hain:
# Decision Tree
# Random Forest
# XGBoost
# LightGBM
# CatBoost

# Because tree models mainly conditions/splits use karte hain:

# area < 1000?

# instead of distance calculation.

# Feature Scaling
#      │
#      ├── Standardization --> Mean ≈ 0, Standard Deviation ≈ 1
#      │
#      ├── Min-Max Scaling --> Max = 1, Min = 0
#      │
#      └── Robust Scaling --> Median = 0, IQR = 1 (Outliers se relatively kam affect hota hai)

########### Standarization ##############
# Standardization ka goal: Mean ≈ 0, Standard Deviation ≈ 1

# Formula: z = x−μ​ / σ
# Where:
# x  = original value
# μ  = mean
# σ  = standard deviation
# z  = scaled value

# age = [20, 30, 40, 50, 60]
# mean = 40
# SD = 14.14
# For age=20 => 20 - 40 / 14.14 = -1.41
# For age=40 => 40 - 40 / 14.14 = 0
# For age=60 => 60 - 40 / 14.14 = +1.41

# Original:
# 20  30  40  50  60
#        ↓ Standardization
# -1.41  -0.71  0  +0.71  +1.41
# Instead of calculating this manually, we use scikit learn formulat StandardScaler

import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.DataFrame({
    "area": [500, 1000, 1500, 2000],
    "age": [2, 4, 6, 8]
})

scaler = StandardScaler()

# fit
#  ↓
# mean + std learn

# transform
#  ↓
# values scale

scaled = scaler.fit_transform(df)

print(scaled)

print("Mean:")
print(scaled.mean(axis=0))

print("Standard Deviation:")
print(scaled.std(axis=0))


########### Min-Max Scaling ##############
# Isme hum values ko generally 0 se 1 ke range mein convert karte hain.

# Formula => x′ = x - xmin / xmax - xmin

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

scaled = scaler.fit_transform(df[["area", "age"]])

print(scaled)

########### Robust Scaling ##############
# RobustScaler aisa scaling method hai jo outliers se relatively kam affect hota hai.

# Formula: x′= x−Median / IQR

import pandas as pd
from sklearn.preprocessing import RobustScaler

df = pd.DataFrame({
    "salary": [25000, 30000, 32000, 35000, 40000,
               42000, 45000, 50000, 150000]
})

scaler = RobustScaler()

scaled = scaler.fit_transform(df[["salary"]])

print(scaled)

# Compare all three scaling methods on the same dataset to see how they handle outliers differently.
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

df = pd.DataFrame({
    "salary": [25000, 30000, 32000, 35000, 40000,
               42000, 45000, 50000, 150000]
})

standard = StandardScaler()
minmax = MinMaxScaler()
robust = RobustScaler()

df["standard"] = standard.fit_transform(df[["salary"]])
df["minmax"] = minmax.fit_transform(df[["salary"]])
df["robust"] = robust.fit_transform(df[["salary"]])

print(df)

# Situation	                                                    Common choice
# Normal-ish data, no major outliers	                        StandardScaler
# Need values in 0–1 range	                                    MinMaxScaler
# Significant outliers	                                        RobustScaler
# KNN	                                                        Scaling important
# K-Means	                                                    Scaling important
# SVM	                                                        Scaling important
# Logistic Regression	                                        Usually scale
# Neural Network	                                            Usually scale
# PCA	                                                        Scale is usually important
# Decision Tree	                                                Usually unnecessary
# Random Forest	                                                Usually unnecessary
# XGBoost	                                                    Usually unnecessary

# Wrong way:- scaler.fit_transform(X)

# Right way:- 
# X_train, X_test = train_test_split(X, test_size=0.2)
# scaler.fit(X_train)
# X_train_scaled = scaler.transform(X_train)
# X_test_scaled = scaler.transform(X_test)

############ Data Leakage #############
# Jab test/future data ki information galti se model ki training process mein chali jaati hai,
# usse Data Leakage kehte hain.

# fit_transform() vs transform()
# scaler.fit_transform(X_train) => Because training data se parameters learn karne hain.
# scaler.transform(X_test) => Because test data ko scale karna hai using training data parameters.

from sklearn.model_selection import train_test_split

df = pd.DataFrame({
    "area": [500, 700, 900, 1100, 1300, 1500, 1800, 2000, 2200, 2500],
    "age": [2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
})

X_train, X_test = train_test_split(
    df,
    test_size=0.2,
    random_state=42
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Train:")
print(X_train_scaled)

print("\nTest:")
print(X_test_scaled)