########### Feature Enineering ##############
# Raw data se useful naye features/columns banana, transform karna, ya existing features ko 
# meaningful form mein convert karna

# Raw Data
#    ↓
# Feature Engineering
#    ↓
# More meaningful information
#    ↓
# Better representation
#    ↓
# Potentially better ML model

import pandas as pd

df = pd.DataFrame({
    "area": [500, 800, 1200, 1500, 2000],
    "bedrooms": [1, 2, 2, 3, 4],
    "bathrooms": [1, 2, 2, 2, 3],
    "age": [10, 5, 8, 3, 2]
})

# Feature 1: Area per bedroom
df["area_per_bedroom"] = df["area"] / df["bedrooms"]

# Feature 2: Bathroom-bedroom ratio
df["bathroom_bedroom_ratio"] = (
    df["bathrooms"] / df["bedrooms"]
)

# Feature 3: Area multiplied by bedrooms
df["area_x_bedrooms"] = df["area"] * df["bedrooms"]

# Feature 4: Construction year
df["construction_year"] = 2026 - df["age"]

print(df)

# Kaunse features house price prediction mein use kar sakte hain?

# Feature                         Use kar sakte hain?                     Reason
# Area                            Haan                                Property size
# Bedrooms                        Haan                                Property capacity
# Bathrooms                       Haan                                Property facilities
# Age                             Haan                                Property ki age
# Area per bedroom                Haan, test karke                    Space distribution
# Bathroom-bedroom ratio          Haan, test karke                    Facilities ka ratio
# Area × bedrooms                 Test karke                          Combined effect
# Construction year               Haan, test karke                    Property kab bani


# Yahan humne price column diya hi nahi hai, isliye abhi target leakage ka issue nahi hai.
# Lekin agar price predict karte waqt input feature mein actual price se calculated value,
# jaise price_per_sqft = price / area, daal di, toh leakage ho sakti hai.

# Categorical Feature Encoding: Aisa data jo categories/labels represent karta hai.
# Categorical Data
#        ↓
# Is there an order?
#        ↓
#    ┌───┴────┐
#    NO       YES
#    ↓         ↓
# One-Hot    Ordinal
# Encoding   Encoding

import pandas as pd

df = pd.DataFrame({
    "city": ["Surat", "Mumbai", "Delhi", "Surat", "Mumbai"],
    "property_type": ["Flat", "Villa", "Flat", "Plot", "Villa"]
})

print(df)

# One-Hot Encoding: Categorical feature ko binary columns mein convert karna,
# jahan har unique category ke liye ek column hota hai.
encoded = pd.get_dummies(
    df,
    columns=["city", "property_type"]
)

print(encoded)

####### Feature Interaction: Do ya zyada features ko combine karke naye features banana. ######
# Example: Area aur bedrooms ko combine karke area_per_bedroom feature banana.

# df["area_x_bedrooms"] = df["area"] * df["bedrooms"]


######### Polynomial Features: nonlinear relationships ko linear model ke through represent karne ka technique.
#  x^2, x^3, x1*x2, etc.

from sklearn.preprocessing import PolynomialFeatures

df = pd.DataFrame({
    "area": [500, 800, 1200, 1500],
    "bedrooms": [1, 2, 2, 3]
})

poly = PolynomialFeatures(degree=2, include_bias=False)

result = poly.fit_transform(df)

feature_names = poly.get_feature_names_out(df.columns)

result_df = pd.DataFrame(result, columns=feature_names)

print(result_df)