# Feature Scaling in Scikit-learn : StandardScaler, MinMaxScaler, and RobustScaler

# Feature Scaling
#      │
#      ├── StandardScaler --> Mean = 0, Std = 1 (z = (x - μ) / σ)
#      │
#      ├── MinMaxScaler   --> Range [0, 1]      (x' = (x - min) / (max - min))
#      │
#      └── RobustScaler   --> Median = 0, IQR = 1 (Robust against outliers)

import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.model_selection import train_test_split

# Dataset with different feature scales and outliers
df = pd.DataFrame({
    "area": [500, 700, 900, 1100, 1300, 1500, 1800, 2000, 2200, 5000],  # 5000 is an outlier
    "age": [2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
})

X = df[["area", "age"]]

# 1. StandardScaler (Standardization)
standard = StandardScaler()
X_standard = standard.fit_transform(X)

# 2. MinMaxScaler (Normalization to 0-1)
minmax = MinMaxScaler()
X_minmax = minmax.fit_transform(X)

# 3. RobustScaler (Outlier Resistant using Median & IQR)
robust = RobustScaler()
X_robust = robust.fit_transform(X)

print("--- Comparison of Scaled Values (Area Column) ---")
comp_df = pd.DataFrame({
    "Original": df["area"],
    "Standard": X_standard[:, 0],
    "MinMax": X_minmax[:, 0],
    "Robust": X_robust[:, 0]
})
print(comp_df)


# Data Leakage Prevention (fit on train, transform on test)
# WRONG : scaler.fit_transform(X) before train_test_split (Leaks test stats into training!)
# RIGHT : fit_transform on X_train, transform on X_test

X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # Learn stats from Train set
X_test_scaled = scaler.transform(X_test)         # Apply Train stats to Test set

print("\n--- Properly Scaled Train & Test Sets ---")
print("X_train_scaled shape:", X_train_scaled.shape)
print("X_test_scaled shape:", X_test_scaled.shape)

