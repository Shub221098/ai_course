# Feature Distribution + Target Distribution

# We will see here:
# target skewed hai ya nahi
# transformation ki zarurat hai ya nahi
# log transformation kya hota hai
# ML model par iska kya impact padta hai

# Our data
# area
# bhk
# age
# price ← Target

########### Target Distribution ###########

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "area": [500, 700, 900, 1100, 1300, 1500, 1800, 2000],
    "bhk": [1, 1, 2, 2, 3, 3, 4, 4],
    "age": [10, 8, 7, 5, 6, 4, 3, 2],
    "price": [25, 30, 42, 48, 58, 65, 78, 90]
})

df2 = pd.DataFrame({
    "salary": [25000, 30000, 32000, 35000, 40000, 42000, 45000, 50000, 150000]
})

plt.hist(df["price"], bins=5)

plt.xlabel("Price")
plt.ylabel("Frequency")
plt.title("Price Distribution")

plt.show()

plt.hist(df2["salary"], bins=5)
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.title("Salary Distribution")

plt.show()

# Skewness ≈ 0
#      ↓
# Approximately symmetric

# Positive
#      ↓
# Right-skewed
#      ↓
# Long tail → high values

# Negative
#      ↓
# Left-skewed
#      ↓
# Long tail → low values

print("Price Skewness:", df["price"].skew())

############## Log Transformation ############################
# Feature/Target
#       ↓
# Right-skewed
#       ↓
# Large values have long tail
#       ↓
# Log transformation may help

df["log_price"] = np.log1p(df["price"])

print(df[["price", "log_price"]])
#    ↓
# ~ 0       → roughly symmetric
# +0.27     → slightly right-skewed
# +2.7      → strongly right-skewed

print("Salary Skewness:", df2["salary"].skew()) # Stronly right-skewed

# For this salary distributon we have one fix log transformation

########################## Feature Transformation ##################################3

# Feature ke values ko mathematically transform karke uski distribution/relationship ko ML
# ke liye more useful banana

df2["log_salary"] = np.log1p(df2["salary"])

print(df2[["salary", "log_salary"]])

print("Original Skewness:", df2["salary"].skew())
print("Log Skewness:", df2["log_salary"].skew())

plt.hist(df2["log_salary"], bins=5)
plt.xlabel("Log Salary")
plt.ylabel("Frequency")
plt.title("Log Salary Distribution")
plt.show()

# Still after log skewness, we got 2.763 → 2.028 = improvement, but still right-skewed.

############# Square root Tranformation - Also used for reduced skewness #############
df2["sqrt_salary"] = np.sqrt(df2["salary"])

print(df2[["salary", "sqrt_salary"]])

print("Original Skewness:", df2["salary"].skew())
print("Sqrt Skewness:", df2["sqrt_salary"].skew())

plt.hist(df2["sqrt_salary"], bins=5)
plt.xlabel("√ Salary")
plt.ylabel("Frequency")
plt.title("Square Root Salary Distribution")
plt.show()

# Right-Skewed Data
#        ↓
# Try Transformation
#        ↓
#  ┌──────────────────────────┐
#  │             │            │
#  │             │            │
#  │             │            |
# Log           √x           1/x
#  │             │            |
# Strong       Moderate       Inverse
# compression  compression    transformation
#  │             │            |
#  └──────┬──────────────────┘             
#         ↓
# Compare distribution
#         ↓
# Validate with ML

########### Reciprocal Transformation:
# Reciprocal transformation large values ko strongly compress karta hai, but iska effect log/√ se different hai.
# Distance vs Speed
# Agar fixed distance hai:
# Time ≈ Distance / Speed
# Speed badhegi → time decrease hoga.

df2["reciprocal_salary"] = 1 / df2["salary"]

print(df2[["salary", "reciprocal_salary"]])

print("Original Skewness:", df2["salary"].skew())
print(f"Reciprocal Skewness: {df2['reciprocal_salary'].skew():.6f}")
# Transformation ne data ko almost symmetric bana diya, but relationship ka shape completely change ho gaya.
# So reciprocal is not just "skewness remover". It represents an inverse relationship.


####### Box-Cox Transformation: Box-Cox kya hai? -> family of transformations

# Abhi tak hum manually choose kar rahe the:

# Log     → log(x)
# √x      → x^0.5
# 1/x     → x^-1

# Box-Cox ka idea:
# Data ke liye ek suitable power transformation (λ / lambda) find karna.
# λ = 1      → approximately original scale
# λ = 0.5    → approximately √x
# λ = 0      → log(x)
# λ = -1     → reciprocal-type transformation

from scipy.stats import boxcox

df2["boxcox_salary"], lambda_value = boxcox(df2["salary"])

print(df2[["salary", "boxcox_salary"]])
print(df2["boxcox_salary"].nunique())
print(df2["boxcox_salary"].to_list())

print("Lambda:", lambda_value)
print("Original Skewness:", df2["salary"].skew())
print("Box-Cox Skewness:", df2["boxcox_salary"].skew())


########## Yeo-Johnson Transformation ###############
# Yeo-Johnson basically Box-Cox ka flexible version samajh sakta hai.
# Useful - where data contains negative, positive values both.
# Box-Cox
# → Only positive values

# Yeo-Johnson
# → Positive + Zero + Negative values

from scipy.stats import yeojohnson

df3 = pd.DataFrame({
    "profit_loss": [
        -40, -20, -5, 0,
        10, 30, 50, 100, 200
    ]
})

df3["yj_profit_loss"], lambda_value = yeojohnson(df3["profit_loss"])

print("Original Skewness:",
      df3["profit_loss"].skew())

print("Yeo-Johnson Skewness:",
      df3["yj_profit_loss"].skew())


print("Lambda:", lambda_value)

#                 Feature Transformation
#                          │
#         ┌────────────────┼─────────────────┐
#         ↓                ↓                 ↓
#        LOG               √x                1/x
#         │                │                 │
#    Stronger            Moderate          Inverse
#    compression        compression        mapping
#         │                │                 │
#         └────────────────┼─────────────────┘
#                          ↓
#                     Box-Cox
#                          │
#                   Positive only
#                          ↓
#                    Yeo-Johnson
#                          │
#               Positive + Zero + Negative