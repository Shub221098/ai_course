# Comprehensive EDA & Data Cleaning Checklist

Before cleaning or modeling a dataset, you must perform a structured **Exploratory Data Analysis (EDA)** to inspect, quality-check, analyze distributions, and understand feature relationships.

---

## 📋 EDA Master Framework

```text
EDA
│
├── 1. Data Inspection
│
├── 2. Data Quality
│   ├── Missing values
│   ├── Duplicates
│   ├── Wrong data types
│   ├── Invalid values
│   └── Inconsistency
│
├── 3. Univariate Analysis
│   └── Ek column ko samajhna
│
├── 4. Bivariate Analysis
│   └── Do columns ka relationship
│
├── 5. Multivariate Analysis
│   └── Multiple columns together
│
├── 6. Distribution
│   ├── Mean
│   ├── Median
│   ├── Skewness
│   └── Outliers
│
└── 7. Relationships
    ├── Correlation
    └── Patterns
```

---

## 1. Data Inspection

Data Inspection is the first step where you get a complete high-level overview of the dataset structure, shape, and raw samples.

### Key Commands
```python
import pandas as pd

# Check rows and columns count
print("Shape:", df.shape)

# List all column names
print("Columns:", df.columns.tolist())

# View first and last few rows
df.head()
df.tail()

# Check dataset metadata & data types
df.info()

# Count unique values per column
df.nunique()
```

### Key Questions to Ask
- How many rows (observations) and columns (features) exist?
- What are the column names? Are there extra spaces or weird characters?
- What does a sample row look like?

---

## 2. Data Quality

Data Quality checks focus on detecting and fixing errors, corrupted records, missing data, and inconsistencies in the raw dataset.

### 2.1 Missing Values
Values can be missing as `NaN`, `None`, empty strings `""`, or placeholder values like `-999` or `"N/A"`.

```python
# Count missing values per column
df.isna().sum()

# Percentage of missing values
(df.isna().mean() * 100).round(2)
```
- **Why are values missing?** 
  - *Missing Completely at Random (MCAR):* Safe to drop or simple mean/median impute if < 5%.
  - *Missing at Random (MAR):* Can be predicted using other columns.
  - *Missing Not at Random (MNAR):* Business reason behind missing value (e.g. unemployed people not filling salary).

### 2.2 Duplicates
Duplicates can be complete row duplicates or duplicated business keys (like `user_id` or `property_id`).

```python
# Check total duplicate rows
df.duplicated().sum()

# View duplicate rows
df[df.duplicated()]

# Drop exact duplicate rows
df = df.drop_duplicates()

# Check duplicate business keys
df.duplicated(subset=["property_id"]).sum()
```

### 2.3 Wrong Data Types
Columns stored as `object` (string) when they should be numeric, datetime, or boolean.

```python
# Check data types
df.dtypes

# Convert numeric column (turns invalid strings into NaN)
df["price"] = pd.to_numeric(df["price"], errors="coerce")

# Convert datetime column
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Convert category column
df["city"] = df["city"].astype("category")
```

### 2.4 Invalid Values
Values that exist but violate domain/business rules (e.g., negative age, zero price, >100% discount).

```python
# Check logically impossible numerical ranges
df[df["age"] < 0]
df[df["age"] > 120]
df[df["price"] <= 0]

# Check unexpected categorical values against valid list
valid_types = ["Flat", "Villa", "Plot", "Apartment"]
df[~df["type"].isin(valid_types)]
```

### 2.5 Inconsistency
Inconsistent formatting, extra whitespace, casing differences, or multi-column logical contradictions.

```python
# Clean text formatting: remove leading/trailing spaces and fix title casing
df["city"] = df["city"].astype(str).str.strip().str.title()

# Logical inconsistency across columns (min_price > max_price)
df[df["min_price"] > df["max_price"]]

# Contradictory rules (e.g. 0 bedrooms but 10 bathrooms)
df[(df["bedrooms"] == 0) & (df["bathrooms"] > 5)]
```

---

## 3. Univariate Analysis (Ek Column Ko Samajhna)

Univariate Analysis means analyzing **one single column at a time** in isolation to understand its central tendency, spread, frequencies, and unique characteristics.

```text
Univariate Analysis
│
├── Numerical Column   → Summary Stats (mean, median, std, min, max, quantiles)
└── Categorical Column → Value Counts, Proportions, Top categories
```

### 3.1 Numerical Columns
```python
# Summary statistics for all numeric columns
df.describe()

# Single column stats
df["price"].describe()

# Variance & Standard Deviation
print("Std Dev:", df["price"].std())
print("Variance:", df["price"].var())

# Quantiles breakdown
df["price"].quantile([0.1, 0.25, 0.5, 0.75, 0.9])
```

### 3.2 Categorical Columns
```python
# Count of unique values
df["city"].nunique()

# Frequency count of each category (including missing)
df["city"].value_counts(dropna=False)

# Percentage proportion of categories
df["city"].value_counts(normalize=True, dropna=False) * 100
```

---

## 4. Bivariate Analysis (Do Columns Ka Relationship)

Bivariate Analysis focuses on analyzing **the relationship between two columns** to understand how one variable changes relative to another.

```text
Bivariate Analysis Pairings
│
├── 1. Numerical vs Numerical   → Correlation, Scatter trends
├── 2. Categorical vs Numerical → Groupby aggregations, Category-wise means/medians
└── 3. Categorical vs Categorical → Cross-tabulations (pd.crosstab)
```

### 4.1 Numerical vs Numerical
```python
# Correlation between two numeric variables
df[["area_sqft", "price"]].corr()

# Grouping a numeric column into bins and comparing mean of another
df.groupby(pd.qcut(df["area_sqft"], q=4))["price"].mean()
```

### 4.2 Categorical vs Numerical
```python
# Group numerical variable by categorical groups
df.groupby("type")["price"].agg(["count", "mean", "median", "std"])
```

### 4.3 Categorical vs Categorical
```python
# Cross-tabulation frequency count
pd.crosstab(df["city"], df["type"])

# Normalized cross-tabulation (Row percentages)
pd.crosstab(df["city"], df["type"], normalize="index") * 100
```

---

## 5. Multivariate Analysis (Multiple Columns Together)

Multivariate Analysis explores interactions among **three or more columns simultaneously** to uncover multi-dimensional relationships and complex group trends.

### 5.1 Multi-Level Grouping
```python
# Group by city AND property type to analyze price
df.groupby(["city", "type"])["price"].agg(["count", "mean", "median"])
```

### 5.2 Pivot Tables
```python
# Structured matrix view across multiple features
pivot = pd.pivot_table(
    df,
    values="price",
    index="city",
    columns="type",
    aggfunc="median",
    fill_value=0
)
print(pivot)
```

### 5.3 Correlation Matrix
```python
# Full numeric correlation matrix
numeric_df = df.select_dtypes(include=["number"])
correlation_matrix = numeric_df.corr()
print(correlation_matrix)
```

---

## 6. Distribution

Distribution analysis helps you examine the statistical shape, center, spread, skewness, and extreme values (outliers) of numerical features.

### 6.1 Mean
The average of all values in a column.
- **Formula:** $\text{Mean} = \frac{\sum x}{N}$
- **Property:** Sensitive to extreme outliers.
```python
df["price"].mean()
```

### 6.2 Median
The middle value (50th percentile) when data is sorted.
- **Property:** Robust against outliers; represents typical values in skewed data.
```python
df["price"].median()
```

### 6.3 Skewness
Skewness measures the asymmetry of the data distribution.

```python
# Calculate skewness score
df["price"].skew()
```

```text
Skewness Interpretation:
│
├── Skew ≈ 0        → Symmetric / Normal Distribution (Mean ≈ Median)
├── Skew > 0 (+ve)  → Right-skewed (Long tail on right side, Mean > Median) e.g., Salary, Price
└── Skew < 0 (-ve)  → Left-skewed (Long tail on left side, Mean < Median) e.g., Retirement Age
```

### 6.4 Outliers
Outliers are extreme values that lie far outside the overall pattern of the distribution.

#### Detection using Quantiles & IQR Method
```python
# Quantile inspection
df["price"].quantile([0.01, 0.05, 0.25, 0.50, 0.75, 0.95, 0.99])

# Interquartile Range (IQR) Method
Q1 = df["price"].quantile(0.25)
Q3 = df["price"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter outliers
outliers = df[(df["price"] < lower_bound) | (df["price"] > upper_bound)]
print("Total Outliers Found:", len(outliers))
```

---

## 7. Relationships

Relationship analysis synthesizes correlation metrics and business patterns to draw actionable conclusions from the dataset.

### 7.1 Correlation
Measures the direction and linear strength between numerical features ($r \in [-1, 1]$).

```python
df.corr(numeric_only=True)
```

```text
Correlation Values (r):
│
├──  +0.7 to +1.0 → Strong Positive (e.g. Area vs Price)
├──   0.0 to +0.3 → Weak / No Correlation
└──  -0.7 to -1.0 → Strong Negative (e.g. Car Age vs Resale Value)
```
> ⚠️ **Golden Rule:** Correlation does not imply Causation.

### 7.2 Patterns
Identify non-linear trends, temporal behavior, and domain-specific patterns.

- **Temporal / Time Patterns:** Group by date, month, or day to find seasonal trends (`df.groupby(df['date'].dt.month)`).
- **Segment / Cluster Patterns:** Specific groups showing distinct behaviors (e.g., luxury properties vs budget flats).
- **Systematic Error Patterns:** Missing values occurring only in specific branches or data sources.

---

## 💡 Quick Master Script

```python
import pandas as pd

def quick_eda(df):
    print("=== 1. DATA INSPECTION ===")
    print(f"Shape: {df.shape}")
    print("Columns:", df.columns.tolist())
    
    print("\n=== 2. DATA QUALITY ===")
    print("Missing Values:\n", df.isna().sum()[df.isna().sum() > 0])
    print(f"Duplicates: {df.duplicated().sum()}")
    
    print("\n=== 3. UNIVARIATE ANALYSIS (NUMERIC) ===")
    print(df.describe().T[["mean", "50%", "min", "max"]])
    
    print("\n=== 4. DISTRIBUTION (SKEWNESS) ===")
    print(df.select_dtypes(include="number").skew())
    
    print("\n=== 5. CORRELATION ===")
    print(df.corr(numeric_only=True))

# Run on your dataframe:
# quick_eda(df)
```
