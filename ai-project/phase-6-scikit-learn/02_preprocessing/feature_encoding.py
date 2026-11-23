# Categorical Encoding in Scikit-learn : OneHotEncoder and OrdinalEncoder

# Categorical Data
#        ↓
# Is there an intrinsic order?
#        ↓
#    ┌───┴────┐
#    NO       YES
#    ↓         ↓
# OneHot     Ordinal
# Encoder    Encoder

import pandas as pd
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, LabelEncoder

df = pd.DataFrame({
    "city": ["Surat", "Mumbai", "Delhi", "Surat", "Mumbai"],
    "education": ["High School", "Bachelor", "Master", "PhD", "Bachelor"]
})

# 1. OneHotEncoder (For Nominal / Unordered categories)
ohe = OneHotEncoder(sparse_output=False, drop="first")  # drop="first" avoids Dummy Variable Trap
city_encoded = ohe.fit_transform(df[["city"]])
city_df = pd.DataFrame(city_encoded, columns=ohe.get_feature_names_out(["city"]))

print("--- OneHotEncoded City Features ---")
print(city_df)

# 2. OrdinalEncoder (For Ordered categories)
education_order = ["High School", "Bachelor", "Master", "PhD"]
oe = OrdinalEncoder(categories=[education_order])
df["education_encoded"] = oe.fit_transform(df[["education"]])

print("\n--- OrdinalEncoded Education Feature ---")
print(df[["education", "education_encoded"]])

# 3. LabelEncoder (Target Variable Y Encoding)
le = LabelEncoder()
y_categorical = ["Pass", "Fail", "Pass", "Pass", "Fail"]
y_encoded = le.fit_transform(y_categorical)
print("\n--- LabelEncoded Target Variable ---")
print("Original Target:", y_categorical)
print("Encoded Target:", y_encoded)

