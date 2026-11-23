############### Bivariate Analysis = 2 variables/columns ke beech relationship ko analyze karna. ########

#               BIVARIATE
#                   ↓
#           2 columns together
#                   ↓
#        ┌──────────┼──────────┐
#        ↓          ↓          ↓
#  Numerical +  Numerical +  Categorical +
#  Numerical    Categorical  Categorical
#        ↓          ↓          ↓
#  Scatter       Groupby     Crosstab
#  Correlation   Bar chart   Bar chart
import pandas as pd
import matplotlib.pyplot as plt

# Type -1 => Numerical + Numerical
df = pd.DataFrame({
    "area": [500, 700, 900, 1100, 1300, 1500, 1800, 2000],
    "price": [25, 32, 40, 48, 55, 65, 75, 90]
})

plt.scatter(df["area"], df["price"])
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Area vs Price")

plt.show()

print(df["area"].corr(df["price"])) # -> 0.9957474974017998

# -1 ←──────── 0 ────────→ +1
# -1 => Strong negative relationship
# 0 => Neutral relationship
# +1 => Strong positive relationship


# Type -2 => Numerical + Categorial
df = pd.DataFrame({
    "city": ["Surat", "Surat", "Mumbai", "Mumbai", "Delhi", "Delhi",
             "Surat", "Mumbai", "Delhi"],
    "price": [50, 60, 80, 90, 70, 75, 55, 85, 65]
})

print(df.groupby("city")["price"].agg(["mean", "median", "min", "max"]))

avg_price = df.groupby("city")["price"].mean()

avg_price.plot(kind="bar")

plt.xlabel("City")
plt.ylabel("Average Price")
plt.title("Average Property Price by City")
plt.show()


df.boxplot(column="price", by="city")

plt.title("Property Price Distribution by City")
plt.suptitle("")
plt.xlabel("City")
plt.ylabel("Price")
plt.show()

#         •  ← Outlier
#         |
#      ┌─────┐
#      │     │
# ─────┼─────┼─────
#      │     │
#      └─────┘
#         |
# Middle line → Median
# Box → Q1 se Q3, yani middle 50% data
# Whiskers → normal range
# Dots outside → potential outliers

# Type-3 : Categorial + Categorial

df = pd.DataFrame({
    "city": [
        "Surat", "Surat", "Surat",
        "Mumbai", "Mumbai", "Mumbai",
        "Delhi", "Delhi", "Delhi"
    ],
    "property_type": [
        "Flat", "Villa", "Flat",
        "Flat", "Flat", "Villa",
        "Villa", "Flat", "Villa"
    ]
})

# Count Distribution
cross = pd.crosstab(df["city"], df["property_type"])

# Percentile Distribution
pd.crosstab(
    df["city"],
    df["property_type"],
    normalize="index"
) * 100

cross.plot(kind="bar")

plt.xlabel("City")
plt.ylabel("Number of Properties")
plt.title("Property Type Distribution by City")
plt.show()