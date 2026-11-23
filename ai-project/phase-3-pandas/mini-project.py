# Mini Project: Real Estate Data Analysis

import pandas as pd
import numpy as np

data = {
    "property_id": [101, 102, 103, 104, 105, 106, 106],
    "title": [
        "Luxury 3 BHK",
        "2 BHK Flat",
        "Premium Villa",
        "Affordable 2 BHK",
        "Luxury Villa",
        "3 BHK Apartment",
        "3 BHK Apartment"
    ],
    "city": [
        "Surat",
        " surat ",
        "Mumbai",
        "Delhi",
        None,
        "SURAT",
        "SURAT"
    ],
    "type": [
        "Flat",
        "Flat",
        "Villa",
        "Flat",
        "Villa",
        "Apartment",
        "Apartment"
    ],
    "price": [
        5000000,
        4500000,
        12000000,
        np.nan,
        9000000,
        7000000,
        7000000
    ],
    "bedrooms": [
        3,
        2,
        4,
        2,
        5,
        3,
        3
    ]
}

df = pd.DataFrame(data)

print(df)

# Problems

# 1. 106 property_id coming twice
# 2. city contains " surat "
# 3. city contains "SURAT" uppercase
# 4. city contains none
# 5. price contains NaN

# Step 1: Inspect the data
print(df.head())
print("\nShape:")
print(df.shape)

print("\nInfo:")
df.info()

print("\nMissing values:")
print(df.isna().sum())

print("\nDuplicates:")
print(df.duplicated().sum())

# City value inconsistent, we want one standard format for it.

df["city"] = df["city"].fillna("Unknown").str.strip().str.title()

print(df)

# price contain NaN
df["price"] = df["price"].fillna(df["price"].median())

print(df)

# remove duplicate property

df = df.drop_duplicates(subset=["property_id"])
print(df)
print(df["property_id"].duplicated().sum())

# Verfiy the data
print(df.isna().sum())
print(df.duplicated().sum())

# Match surat properties
surat = df[df["city"] == "Surat"]

print(surat)

# Match property price > 50 lakh

premium = df[df["price"] > 5000000]

print(premium)

# Average price by city

city_summary = df.groupby("city")["price"].mean().reset_index().sort_values("price", ascending=False)
print(city_summary)

# Property type analysis

summary = df.groupby("type").agg(
    average_price=("price", "mean"),
    maximum_price=("price", "max"),
    property_count=("property_id", "count")
).reset_index()

print(summary)

# Save cleaned data to file
df.to_csv("clean_properties.csv", index=False)

# Save cleaned Summary to file
city_summary.to_csv("city_price_summary.csv", index=False)



# Few more Questions

# Q1
# Surat ki properties mein highest price wali property nikalo.

# Solution 1:- 
highest_price = df.loc[
    df[df["city"] == "Surat"]["price"].idxmax()
]

# Solution 2:- 
highest_price = (
    df[df["city"] == "Surat"]
    .sort_values("price", ascending=False)
    .head(1)
)

print(highest_price)
# Q2
# Sirf Flat properties ka average price nikalo.
avg_price = df[df["type"] == "Flat"]["price"].mean()
print(avg_price)

# Q3
# Har city mein kitni properties hain?
city_wise_summary = df.groupby("city").agg(
    property_count=("property_id", "count")
)
print(city_wise_summary)
# Q4 🔥
# Sabse expensive property ki complete row nikalo.
expensive_property = df.sort_values("price", ascending=False).head(1)
print(expensive_property)