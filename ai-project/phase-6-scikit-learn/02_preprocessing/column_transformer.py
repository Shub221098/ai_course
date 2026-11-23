# ColumnTransformer in Scikit-learn : Applying different transformers to different column subsets

# ColumnTransformer Workflow:
# 
#                 Raw Data
#                     │
#        ┌────────────┴────────────┐
#        ▼                         ▼
#  Numeric Columns          Categorical Columns
# (area, age, income)       (city, property_type)
#        │                         │
#  StandardScaler()          OneHotEncoder()
#        │                         │
#        └────────────┬────────────┘
#                     ▼
#         Combined Feature Matrix

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

df = pd.DataFrame({
    "area": [500, 800, 1200, 1500, 2000],
    "age": [10, 5, 8, 3, 2],
    "city": ["Surat", "Mumbai", "Delhi", "Surat", "Mumbai"],
    "property_type": ["Flat", "Villa", "Flat", "Plot", "Villa"]
})

# Define ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), ["area", "age"]),
        ("cat", OneHotEncoder(drop="first", sparse_output=False), ["city", "property_type"])
    ],
    remainder="passthrough"  # Columns not specified are kept unchanged
)

transformed_data = preprocessor.fit_transform(df)

print("--- Transformed Feature Matrix ---")
print("Transformed Matrix Shape:", transformed_data.shape)
print("Processed Matrix Data:\n", transformed_data)

