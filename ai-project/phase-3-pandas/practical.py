import pandas as pd
import numpy as np

data = {
    "name": ["Rahul", "Amit", "Priya", "Neha"],
    "age": [25, np.nan, 28, 32],
    "city": ["Surat", "Delhi", np.nan, "Pune"],
    "salary": [40000, 55000, 60000, np.nan]
}

df = pd.DataFrame(data)


print(df)

# Check for missing values
print("\nMissing Values:")
print(df.isnull())
print(df.isna())


# Check for missing values in each column
print("\nMissing Values Count:")
print(df.isnull().sum()) # or you can use isna().sum()

# Check for missing values in each row
print("\nMissing Values Count (Row-wise):")
print(df.isnull().sum()) # or you can use isna().sum

# Check for missing values in the column
print(df[df["salary"].isna()])

# Get the row which didn't have missing values
print("\nRows without Missing Values:")
print(df[df["salary"].notna()]) # or you can use notnull()

# Fill missing values with a specific value
print("\nFill Missing Values:")
df_filled = df.fillna(0)
print(df_filled)

# Fill missing values with the mean of the column
print("\nFill Missing Values with Mean:")
df_filled_mean = df.fillna(df.mean(numeric_only=True))
print(df_filled_mean)

# Fill missing values in a specific column with the mean of that column
print("\nFill Missing Values in 'age' Column with Mean:")
df_filled_mean_age = df["age"] = df["age"].fillna(df["age"].mean())
print(df_filled_mean_age)

# Drop rows with missing values
print("\nDrop Rows with Missing Values:")
df_dropped = df.dropna()
print(df_dropped)

# Drop columns with missing values
print("\nDrop Columns with Missing Values:")
df_dropped_columns = df.dropna(axis=1)
print(df_dropped_columns)

