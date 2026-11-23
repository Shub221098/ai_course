import pandas as pd

data = {
    "name": ["Rahul", "Amit", "Priya", "Neha"],
    "age": [25, 30, 28, 32],
    "city": ["Surat", "Delhi", "Mumbai", "Pune"],
    "salary": [40000, 55000, 60000, 70000]
}

df = pd.DataFrame(data)

# Greater than
df_filtered = df[df["age"] > 28]

print(df_filtered)

# Less than
df_filtered = df[df["salary"] < 60000]

print(df_filtered)

# Equal ==

df_filtered = df[df["city"] == "Delhi"]

print(df_filtered)

# Greater than or equal >=
df_filtered = df[df["age"] >= 30]

print(df_filtered)

# Less than or equal <=
df_filtered = df[df["salary"] <= 60000]

print(df_filtered)

# Muliple Conditions

# AND (&)
df_filtered = df[(df["age"] > 25) & (df["salary"] > 50000)]

print(df_filtered)

# OR (|)
df_filtered = df[(df["age"] < 30) | (df["salary"] > 60000)]

print(df_filtered)

# NOT (~)
df_filtered = df[~(df["city"] == "Mumbai")]

print(df_filtered)

# isin() — Filter rows based on a list of values
df_filtered = df[df["city"].isin(["Delhi", "Pune"])]

print(df_filtered)

# notin() — Filter rows not in a list of values
df_filtered = df[~df["city"].isin(["Delhi", "Pune"])]

print(df_filtered)

# between() — Filter rows based on a range of values
df_filtered = df[df["age"].between(28, 32)]

print(df_filtered)

# query() — Filter rows using a query string
df_filtered = df.query("age > 28 and salary > 50000")

print(df_filtered)

# iloc = position based

df_filtered = df.iloc[1:3]  # Rows 1 and 2

print(df_filtered)

df_filtered = df.iloc[:, 1:3]  # Columns 1 and 2

print(df_filtered)

df_filtered = df.iloc[1:3, 1:3]  # Rows 1 and 2, Columns 1 and 2

print(df_filtered)

df_filtered = df.iloc[[0, 2], [1, 3]]  # Rows 0 and 2, Columns 1 and 3

print(df_filtered)

df_filtered = df.iloc[1:3, [0, 2]]  # Rows 1 and 2, Columns 0 and 2

print(df_filtered)

# loc = label based

df_filtered = df.loc[1:3]  # Rows 1 to 3 (inclusive)

print(df_filtered)

df_filtered = df.loc[:, ["age", "salary"]]  # Columns "age" and "salary"

print(df_filtered)

df_filtered = df.loc[1:3, ["age", "salary"]]  # Rows 1 to 3 (inclusive), Columns "age" and "salary"

print(df_filtered)

df_filtered = df.loc[[0, 2], ["name", "city"]]  # Rows 0 and 2, Columns "name" and "city"

print(df_filtered)

df_filtered = df.loc[1:3, ["name", "city"]]  # Rows 1 to 3 (inclusive), Columns "name" and "city"

print(df_filtered)

# Filter rows based on a condition and select specific columns
# df.loc[
#     condition,
#     columns
# ]

df_filtered = df.loc[df["age"] > 28, ["name", "salary"]]

print(df_filtered)

df_filtered = df.loc[df["salary"] < 60000, ["name", "city"]]

print(df_filtered)

df_filtered = df.loc[df["city"] == "Delhi", ["name", "age"]]

print(df_filtered)

df_filtered = df.loc[df["age"] >= 30, ["name", "city"]]

print(df_filtered)

df_filtered = df.loc[df["salary"] <= 60000, ["name", "age"]]

print(df_filtered)

df_filtered = df.loc[(df["age"] > 25) & (df["salary"] > 50000), ["name", "city"]]

print(df_filtered)

df_filtered = df.loc[(df["age"] < 30) | (df["salary"] > 60000), ["name", "city"]]

print(df_filtered)

df_filtered = df.loc[~(df["city"] == "Mumbai"), ["name", "age"]]

print(df_filtered)

df_filtered = df.loc[df["city"].isin(["Delhi", "Pune"]), ["name", "salary"]]

print(df_filtered)

df_filtered = df.loc[~df["city"].isin(["Delhi", "Pune"]), ["name", "age"]]

print(df_filtered)

df_filtered = df.loc[df["age"].between(28, 32), ["name", "salary"]]

print(df_filtered)

df_filtered = df.query("age > 28 and salary > 50000")[["name", "city"]]

print(df_filtered)

# Update values based on a condition
df.loc[df["age"] > 30, "salary"] = 80000

print(df)

df.loc[df["city"] == "Mumbai", "salary"] = 65000

print(df)

# Update multiple columns based on a condition
df.loc[df["age"] < 30, ["salary", "city"]] = [45000, "Chennai"]

print(df)

df.loc[df["city"] == "Delhi", ["salary", "age"]] = [60000, 35]

print(df)

# Filter rows based on multiple conditions and update specific columns
df.loc[(df["age"] > 25) & (df["salary"] < 60000), ["salary", "city"]] = [50000, "Bangalore"]

print(df)

df.loc[(df["age"] < 30) | (df["salary"] > 60000), ["salary", "city"]] = [70000, "Hyderabad"]

print(df)

