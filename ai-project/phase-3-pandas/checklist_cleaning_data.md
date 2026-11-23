# Pandas — How to Find Problems in Data

Before cleaning a dataset, first identify what is wrong with the data.

The correct mindset is:

```text
Raw Data
   ↓
Inspect
   ↓
Find Problems
   ↓
Understand Why
   ↓
Choose Fix
   ↓
Clean
   ↓
Verify
```

## 1. Understand the Dataset

First check the basic structure of the data.

```python
df.head()
df.tail()
df.shape
df.columns
```

Important questions:

```text
How many rows?
How many columns?
What columns exist?
What does the data look like?
```

Example:

```python
df.shape
```

Output:

```text
(10000, 8)
```

Means:

```text
10,000 rows
8 columns
```

---

## 2. Check Data Types

Use:

```python
df.info()
```

or:

```python
df.dtypes
```

Look for columns having the wrong data type.

Example:

```text
age       object
price     object
```

But `age` and `price` should probably be numeric.

Convert numeric columns:

```python
df["age"] = pd.to_numeric(
    df["age"],
    errors="coerce"
)
```

`errors="coerce"` converts invalid values into `NaN`, which can then be investigated.

---

## 3. Check Missing Values

First count missing values:

```python
df.isna().sum()
```

Example:

```text
name       0
age      120
city      35
salary    80
```

To check missing percentage:

```python
(df.isna().mean() * 100).round(2)
```

Example:

```text
age       1.20%
city      0.35%
salary    0.80%
```

Important questions:

```text
How many values are missing?
Which columns have missing values?
Is the missing percentage small or large?
Why are values missing?
```

Do not automatically delete or fill missing values without understanding the reason.

---

## 4. Check Duplicate Rows

Check total duplicate rows:

```python
df.duplicated().sum()
```

See duplicate rows:

```python
df[df.duplicated()]
```

Remove exact duplicate rows:

```python
df = df.drop_duplicates()
```

But complete-row duplicates are not the only problem.

Also check important business keys.

Example:

```python
df["property_id"].duplicated().sum()
```

A `property_id` may need to be unique even when the entire row is not identical.

For specific columns:

```python
df.duplicated(subset=["property_id"])
```

---

## 5. Check Unique / Categorical Values

Check unique values:

```python
df["city"].unique()
```

Check frequency:

```python
df["city"].value_counts(dropna=False)
```

Look for inconsistent values.

Example:

```text
Surat
surat
SURAT
 Surat
```

These may represent the same city but are stored differently.

Clean them:

```python
df["city"] = (
    df["city"]
    .str.strip()
    .str.title()
)
```

Now all become:

```text
Surat
```

---

## 6. Check Invalid Values and Ranges

Not every value that exists is valid.

Example:

```python
df["age"].describe()
```

Suppose:

```text
min = -5
max = 150
```

These values should be investigated.

Find invalid ages:

```python
df[df["age"] < 0]
```

```python
df[df["age"] > 100]
```

For property data:

```python
df[df["price"] <= 0]
```

```python
df[df["bedrooms"] <= 0]
```

The important question is:

> Is this value logically possible?

---

## 7. Check Unexpected Categories

Suppose valid property types are:

```text
Flat
Villa
Plot
Apartment
```

Check actual values:

```python
df["type"].unique()
```

Find invalid categories:

```python
valid_types = [
    "Flat",
    "Villa",
    "Plot",
    "Apartment"
]

df[~df["type"].isin(valid_types)]
```

This helps detect values such as:

```text
Flatt
Vila
UnknownType
```

---

## 8. Check Outliers

An outlier is a value that is unusually different from the rest of the data.

Example:

```text
40000
45000
50000
55000
60000
5000000
```

`5000000` is suspicious compared with the other values.

Start with:

```python
df["salary"].describe()
```

You can also inspect percentiles:

```python
df["salary"].quantile(
    [0.01, 0.25, 0.50, 0.75, 0.99]
)
```

Important:

> An outlier is not automatically incorrect.

For example, a ₹50 crore property may be unusual but still completely valid.

Always investigate before removing an outlier.

---

## 9. Check Logical Relationships Between Columns

Some problems can only be found by comparing multiple columns.

Example:

```text
min_price = 50 lakh
max_price = 30 lakh
```

This is logically inconsistent.

Find such rows:

```python
df[df["min_price"] > df["max_price"]]
```

Another example:

```text
age = 25
date_of_birth = inconsistent value
```

Or real-estate examples:

```text
bedrooms = 0
bathrooms = 10
```

This may or may not be valid depending on the business rules, so it should be investigated.

Important question:

> Do these columns make logical sense together?

---

## 10. Check Number of Unique Values

Use:

```python
df.nunique()
```

Example:

```text
property_id    9800
city              8
type              4
```

This helps understand the structure of the dataset.

Suspicious example:

```text
city = 10,000 unique values
```

when the business should only have a few cities.

---

## 11. Check Numerical Statistics

Use:

```python
df.describe()
```

Pay attention to:

```text
count
mean
std
min
25%
50%
75%
max
```

Especially inspect:

```text
count → how many valid values?
min   → suspicious low values?
max   → suspicious high values?
mean  → unusual average?
50%   → median
```

---

## 12. Check Text Quality

Text columns can contain:

```text
leading spaces
trailing spaces
different casing
empty strings
unexpected characters
```

Remove extra spaces:

```python
df["name"] = df["name"].str.strip()
```

Find empty strings:

```python
df[df["name"].str.strip() == ""]
```

Normalize case:

```python
df["city"] = df["city"].str.lower()
```

or:

```python
df["city"] = df["city"].str.title()
```

---

# Complete First-Pass Data Quality Check

When receiving a new dataset, run:

```python
import pandas as pd

print("=== SHAPE ===")
print(df.shape)

print("\n=== COLUMNS ===")
print(df.columns.tolist())

print("\n=== DATA TYPES ===")
print(df.dtypes)

print("\n=== HEAD ===")
print(df.head())

print("\n=== MISSING VALUES ===")
print(df.isna().sum())

print("\n=== MISSING % ===")
print((df.isna().mean() * 100).round(2))

print("\n=== DUPLICATE ROWS ===")
print(df.duplicated().sum())

print("\n=== UNIQUE VALUES ===")
print(df.nunique())

print("\n=== NUMERICAL SUMMARY ===")
print(df.describe())
```

Then investigate important categorical columns:

```python
print(df["city"].value_counts(dropna=False))
```

```python
print(df["type"].value_counts(dropna=False))
```

---

# Professional Data-Quality Checklist

Whenever you receive a new dataset, check:

```text
1. Shape
2. Columns
3. Data types
4. Missing values
5. Duplicate rows
6. Duplicate business keys
7. Unique values
8. Category consistency
9. Invalid ranges
10. Outliers
11. Logical relationships
12. Text quality
13. Suspicious values
```

---

# Most Important Mindset

Data cleaning does NOT mean:

```text
NaN found
   ↓
fill it
```

or:

```text
Duplicate found
   ↓
delete it
```

Instead:

```text
Problem found
     ↓
Why is it a problem?
     ↓
How much data is affected?
     ↓
What does the value actually mean?
     ↓
Choose the correct fix
     ↓
Apply the fix
     ↓
Verify the result
```

Example:

```text
Salary is missing
        ↓
10 rows or 1,00,000 rows?
        ↓
Why is it missing?
        ↓
Mean / Median / Remove / Business Rule?
        ↓
Fix
        ↓
Check again
```

## Final Mental Model

```text
RAW DATA
   ↓
INSPECT
   ↓
MISSING VALUES
   ↓
DUPLICATES
   ↓
DATA TYPES
   ↓
INVALID VALUES
   ↓
INCONSISTENCY
   ↓
OUTLIERS
   ↓
LOGICAL ERRORS
   ↓
CHOOSE FIX
   ↓
CLEAN DATA
   ↓
VERIFY
   ↓
ANALYZE / ML
```

🔥 **Core rule:**

> First find and understand the problem. Then decide how to clean it.
