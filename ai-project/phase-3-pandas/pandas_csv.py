import pandas as pd

# CSV
#  ↓
# read_csv()
#  ↓
# head()
# shape
# info()
# isna()
#  ↓
# fillna()
# drop_duplicates()
# str cleaning
#  ↓
# filter
# groupby
# sort
#  ↓
# to_csv()

# Read CSV → DataFrame.
df = pd.read_csv("employees.csv")
# Write DataFrame → CSV
df.to_csv("clean_employees.csv", index=False)
# index=False kyun? Agar False nahi lagao, Pandas apna index bhi file mein save kar dega:

print(df)

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

# # Read Excel → DataFrame
# df = pd.read_excel("employees.xlsx")
# # Write DataFrame → Excel
# df.to_excel("clean_employees.xlsx", index=False)
# print(df)

# # Read Json → DataFrame
# df = pd.read_json("employees.json")

# # Write DataFrame → Json
# df.to_json("employees_output.json", orient="records", indent=2)



