# Binning / Discretization: Continuous numerical values ko groups/buckets mein convert karna

# Continuous Feature
#        ↓
#    Binning
#        ↓
#  ┌─────┴─────┐
#  ↓           ↓
# Fixed       Quantile
# ranges      based
#  ↓           ↓
# cut()       qcut()
#        ↓
# Categorical / Bucket Feature

import pandas as pd

df = pd.DataFrame({
    "area": [500, 700, 900, 1200, 1500, 1800, 2200, 3000, 4000]
})

df["area_group"] = pd.cut(
    df["area"],
    bins=[0, 800, 1500, 2500, 5000],
    labels=["Small", "Medium", "Large", "Very Large"]
)

print(df)

df["area_quantile"] = pd.qcut(
    df["area"],
    q=4
)

print(df)