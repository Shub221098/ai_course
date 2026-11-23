import pandas as pd

# axis=0
# ↓
# column-wise

# axis=1
# ↓
# row-wise

df = pd.DataFrame({
    "name": ["Rahul Sharma", "Amit Patel", "Priya Shah", "Neha Pareta"],
    "city": ["Surat", "Delhi", "Mumbai", "Pune"]
})

print(df)

data = df["city"].str.lower()
print(f"lowercase, ${data}")
data = df["city"].str.upper()
print(f"uppercase, ${data}")
data = df["name"].str.title()
print(f"title, ${data}")
data = df[df["name"].str.contains("Rahul")]
print(f"check rahul contains, ${data}")
data = df[df["name"].str.contains("rahul", case=False)]
print(f"Check rahul contains with case false, ${data}")
data = df[df["city"].str.contains("u", case=False)]
print(f"check u contains with case false, ${data}")
data = df[df["name"].str.startswith("A")]
print(f"startwith capital letter, ${data}")
data = df[df["name"].str.endswith("a")]
print(f"endswith small letter, ${data}")
data = df["name"].str.len()
print(f"length, ${data}")
data = df["name"] = df["name"].str.strip()
print(f"strip, ${data}")
data = df["city"] = df["city"].str.replace("Mumbai", "Bombay")
print(f"replace, ${data}")
data = df["name"].str.split(" ").str[0]
print(f"split, ${data}")


############# Apply with lambda operations #####################

import pandas as pd

df = pd.DataFrame({
    "name": ["Rahul", "Amit", "Priya", "Neha"],
    "age": [25, 30, 28, 32],
    "salary": [40000, 55000, 60000, 70000]
})

# Double the salary
print("\n Making the salary double")
df["double_salary"] = df["salary"].apply(lambda x: x * 2)
print(df)

# Increase the age by 1
print("\n Making the age increase by 1")
df["age_increase"] = df["age"].apply(lambda x: x + 1)
print(df)

# With conditions on age adding new columns determining Junior or Senior
df["age_group"] = df["age"].apply(
    lambda x: "Senior" if x >= 30 else "Junior"
)
print(df)

df["salary_level"] = df["salary"].apply(
    lambda x: "High" if x >= 60000 else "Low"
)
print(df)

# Use custom function with apply
def salary_category(salary):
    if salary >= 60000:
        return "High"
    elif salary >= 50000:
        return "Medium"
    else:
        return "Low"
    
df["salary_level"] = df["salary"].apply(salary_category)
print(df)


# Apply on whole row
def classify(row):
    if row["age"] >= 30 and row["salary"] >= 60000:
        return "Premium"
    return "Regular"
df["type"] = df.apply(classify, axis=1)
print(df)

properties = pd.DataFrame({
    "price": [5000000, 8000000, 12000000, 6000000],
    "bedrooms": [2, 3, 4, 2]
})

properties["price_category"] = properties["price"].apply(
    lambda x: "Premium" if x >= 8000000 else "Standard"
)


############ Value Counts ################
df = pd.DataFrame({
    "name": ["Rahul", "Amit", "Priya", "Neha", "Raj", "Karan"],
    "city": ["Surat", "Delhi", "Surat", "Mumbai", "Delhi", "Surat"],
    "salary": [40000, 55000, 60000, 70000, 45000, 50000]
})

print(df["city"].value_counts())

print(df.groupby("city").size())

print(df.value_counts(["city", "salary"]))

print(df["city"].value_counts(normalize=True) * 100)


# pivot_table

# Raw Data
#    ↓
# Rows → city
# Columns → property type
# Values → price
# Calculation → mean
#    ↓
# Summary table

properties = pd.DataFrame({
    "city": ["Surat", "Surat", "Delhi", "Delhi", "Mumbai"],
    "type": ["Flat", "Villa", "Flat", "Villa", "Flat"],
    "price": [5000000, 8000000, 6000000, 9000000, 10000000]
})

# Average
result = pd.pivot_table(
    properties,
    values="price",
    index="city",
    columns="type",
    aggfunc="mean"
)
print(result)

# Count
result = pd.pivot_table(
    properties,
    values="price",
    index="city",
    columns="type",
    aggfunc="count"
)
print(result)

# Sum

result = pd.pivot_table(
    properties,
    values="price",
    index="city",
    columns="type",
    aggfunc="sum"
)
print(result)

# groupby()
# → grouped analysis

# pivot_table()
# → 2D summary/report