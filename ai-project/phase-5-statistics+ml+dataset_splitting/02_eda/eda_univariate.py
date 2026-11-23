# EDA (Exploratory Data Analysis)
# │
# ├── Data Inspection
# │
# ├── Data Quality
# │   ├── Missing values
# │   ├── Duplicates
# │   ├── Wrong data types
# │   ├── Invalid values
# │   └── Inconsistency
# │
# ├── Univariate Analysis
# │   └── Ek column ko samajhna
# │
# ├── Bivariate Analysis
# │   └── Do columns ka relationship
# │
# ├── Multivariate Analysis
# │   └── Multiple columns together
# │
# ├── Distribution
# │   ├── Mean
# │   ├── Median
# │   ├── Skewness
# │   └── Outliers
# │
# └── Relationships
#     ├── Correlation
#     └── Patterns

import numpy as np
import pandas as pd

# ==============================================================================
# 1. DESCRIPTIVE STATISTICS
# ==============================================================================
# Mathematically summarizes and quantifies key characteristics of data.
#
# A. Central Tendency (Where center lies):
#   - Mean   : Average of values (sensitive to outliers).   --> df['col'].mean()
#   - Median : Middle value sorted (robust to outliers).    --> df['col'].median()
#   - Mode   : Most frequent value (best for categorical). --> df['col'].mode()[0]
#
# B. Dispersion / Spread (Data spread):
#   - Range   : Max - Min distance.                         --> df['col'].max() - df['col'].min()
#   - Variance: Avg squared distance from mean (σ²).        --> df['col'].var()
#   - Std Dev : Square root of variance (σ, original unit). --> df['col'].std()
#   - IQR     : Middle 50% spread (Q3 - Q1, outlier detection)--> q3 - q1
#
# C. Distribution Shape:
#   - Skewness: Symmetry (-ve = left tail, 0 = symmetric, +ve = right tail). --> df['col'].skew()
#   - Kurtosis: Peakness / Tailedness (identifies extreme outlier presence). --> df['col'].kurt()
#
# Auto Summary in Python:
#   df.describe()  --> Returns key summary statistics automatically
# ==============================================================================


# ==============================================================================
# 2. EXPLORATORY DATA ANALYSIS (EDA)
# ==============================================================================
# Investigative workflow combining descriptive stats, visualizations, data cleaning,
# and relationship mapping to discover patterns, anomalies, and test assumptions.
#
# Key Steps in EDA Workflow:
#   1. Data Inspection & Structure : Shape, data types, columns     --> df.info(), df.head()
#   2. Data Hygiene & Cleaning    : Missing values, duplicates, bad inputs --> df.isnull().sum(), df.duplicated().sum()
#   3. Outlier Detection           : Spot extreme/unusual values   --> Box plots, IQR / Z-score
#   4. Visualizations              :
#       - Univariate (1 column)    : Histograms, KDE density plots, Bar charts
#       - Bivariate / Multivariate : Scatter plots, Pair plots, Correlation Heatmaps
#   5. Feature Relationships       : Inter-feature dependencies & target feature linkage
# ==============================================================================


###################### Univariate Analysis = ek time par sirf ONE column ko analyze karna. ################

# UNIVARIATE
# │
# ├── Numerical
# │   ├── Mean
# │   ├── Median
# │   ├── Std
# │   ├── Histogram
# │   ├── Boxplot
# │   └── Skewness ✅
# │
# └── Categorical
#     ├── Unique values
#     ├── nunique()
#     ├── value_counts() ✅
#     ├── Percentage ✅
#     └── Bar chart

# Numberical Univariate Analysis
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "price": [40, 45, 50, 55, 60, 65, 70, 75, 200]
})

print(df["price"].describe())
# Output:
# count      9.000000
# mean      73.333333
# std       50.270000
# min       40.000000
# 25%       50.000000
# 50%       60.000000
# 75%       70.000000
# max      200.000000

# Visualization: Numbers dekhna useful hai, lekin graph se pattern aur easily dikhta hai
plt.hist(df["price"], bins=5)
plt.xlabel("Price")
plt.ylabel("Number of Properties")
plt.title("Property Price Distribution")
plt.show()

# BoxPlot : Outliers dekhne ke liye boxplot bahut useful hai.
plt.boxplot(df["price"])
plt.ylabel("Price")
plt.title("Property Price")
plt.show()

# Practical Assigned (Univariate Analysis)

df = pd.DataFrame({
    "salary": [25000, 30000, 32000, 35000, 40000, 42000, 45000, 50000, 150000]
})

print(df['salary'].describe())

# Visualization
plt.hist(df['salary'], bins=5)
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.title("Employee Salary Distribution")
plt.show()

# BoxPlot
plt.boxplot(df["salary"])
plt.ylabel("Salary")
plt.title("Employee Salary")
plt.show()

# Skeness : Skewness batata hai ki data ki distribution kis direction mein jhuki hui hai.
# Skewness
#    ↓
# Distribution kis taraf tilted hai?

# Positive / Right skew
#    → long tail right
#    → usually Mean > Median

# Negative / Left skew
#    → long tail left
#    → usually Mean < Median

# ≈ 0
#    → roughly symmetric

print("Mean:", df["salary"].mean())
print("Median:", df["salary"].median())
print("Skewness:", df["salary"].skew())

# Categorical Univariate Analysis: Ab agar ek column categories/text contain karta hai, toh us ek categorical column ko analyze karna

df = pd.DataFrame({
    "city": [
        "Surat",
        "Mumbai",
        "Surat",
        "Delhi",
        "Surat",
        "Mumbai",
        "Surat",
        "Delhi",
        "Mumbai",
        "Surat"
    ]
})

# Count
print(df["city"].value_counts())

# Percentage
print(df["city"].value_counts(normalize=True) * 100)

# Visualization
df["city"].value_counts().plot(kind="bar")

plt.xlabel("City")
plt.ylabel("Number of Properties")
plt.title("Properties by City")
plt.show()

# nunique : tell how much unique categories are there
print(df["city"].nunique())

