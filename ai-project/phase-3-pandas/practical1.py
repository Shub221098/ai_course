# This is complete mini data pipeline

import pandas as pd

properties = pd.read_csv("properties.csv")
print(properties)

print(properties.head())
print(properties.info())
print(properties.isna().sum())

properties["price"] = properties["price"].fillna(
    properties["price"].median()
)
print(properties)

print(properties.isna().sum())
properties = properties.drop_duplicates()
print(properties)

surat_properties = properties[
    properties["city"].str.lower() == "surat"
]
print(surat_properties)

summary = (
    surat_properties
    .groupby("type")["price"]
    .mean()
    .reset_index()
    .sort_values("price", ascending=False)
)

print(summary)

summary.to_csv("surat_property_summary.csv", index=False)