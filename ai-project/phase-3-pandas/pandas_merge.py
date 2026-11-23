import pandas as pd

properties = pd.DataFrame({
    "property_id": [101, 102, 103, 104],
    "property_name": ["Palm Residency", "Green Valley", "Sky Heights", "Lake View"],
    "builder_id": [1, 2, 1, 3]
})

builders = pd.DataFrame({
    "builder_id": [1, 2, 3],
    "builder_name": ["Karma Builders", "ABC Developers", "XYZ Group"]
})

# Types of joins:- inner, left, right, outer
# INNER
# A ∩ B
# ↓
# Only matching


# LEFT
# A + matching B
# ↓
# Left ki all rows


# RIGHT
# B + matching A
# ↓
# Right ki all rows


# OUTER
# A ∪ B
# ↓
# Dono ki all rows

# Inner join:- Merge Result based on builder_id with default join as inner
print("\nMerge Results based on inner join")
result = pd.merge(
    properties,
    builders,
    on="builder_id",
    how="inner"
)

print(result)

print("\nMerge Results based on left join")
result = pd.merge(
    properties,
    builders,
    on="builder_id",
    how="left"
)
print(result)

print("\nMerge Results based on right join")
result = pd.merge(
    properties,
    builders,
    on="builder_id",
    how="right"
)
print(result)


print("\nMerge Results based on outer join")
result = pd.merge(
    properties,
    builders,
    on="builder_id",
    how="outer"
)
print(result)


# Different column names but same key
properties = pd.DataFrame({
    "property_id": [101, 102],
    "builder_id": [1, 2]
})

builders = pd.DataFrame({
    "id": [1, 2],
    "builder_name": ["Karma Builders", "ABC Developers"]
})

# properties → builder_id
# builders   → id

pd.merge(
    properties,
    builders,
    left_on="builder_id",
    right_on="id"
)


# Concat

df1 = pd.DataFrame({'A': ['A0', 'A1'], 'B': ['B0', 'B1']})
df2 = pd.DataFrame({'A': ['A2', 'A3'], 'B': ['B2', 'B3']})

# Stack rows
result = pd.concat([df1, df2], ignore_index=True)
print(result)

# Stack rows vertically
result = pd.concat([df1, df2], axis=0)
print(result)

# Stack rows horizontally
result = pd.concat([df1, df2], axis=1)
print(result)


jan = pd.DataFrame({
    "name": ["Rahul", "Amit"],
    "salary": [40000, 50000]
})

feb = pd.DataFrame({
    "name": ["Priya", "Neha"],
    "salary": [60000, 70000]
})

print(pd.concat([jan, feb], ignore_index=True))