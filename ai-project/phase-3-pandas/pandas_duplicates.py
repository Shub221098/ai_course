import pandas as pd

data = {
    "name": ["Rahul", "Amit", "Rahul", "Priya", "Amit"],
    "city": ["Surat", "Delhi", "Mumbai", "Surat", "Delhi"],
    "salary": [40000, 55000, 40000, 60000, 55000]
}

df = pd.DataFrame(data)

print(df)

# Check for duplicate rows
print("\nCheck for Duplicate Rows:")
check_duplicate = df.duplicated()
print(check_duplicate)

# Check for duplicate rows based on specific columns

print("\nCheck for Duplicate Rows based on 'name' and 'city':")
check_duplicate_subset = df.duplicated(subset=["name", "city"])
print(check_duplicate_subset)

# See duplicate rows
print("\nDuplicate Rows:")
get_duplicate_rows = df[df.duplicated()]
print(get_duplicate_rows)

# See duplicate rows based on specific columns
print("\nDuplicate Rows based on 'name' and 'city':")
get_duplicate_rows_subset = df[df.duplicated(subset=["name", "city"])]
print(get_duplicate_rows_subset)

# Drop duplicate rows
print("\nDataFrame after dropping duplicate rows:")
df_dropped_duplicates = df.drop_duplicates()
print(df_dropped_duplicates)

# Drop duplicate rows based on specific columns
print("\nDataFrame after dropping duplicate rows based on 'name' and 'city':")
df_dropped_duplicates_subset = df.drop_duplicates(subset=["name", "salary"])
print(df_dropped_duplicates_subset)

# Drop duplicate rows and keep the last occurrence
print("\nDataFrame after dropping duplicate rows and keeping the last occurrence:")
df_dropped_duplicates_last = df.drop_duplicates(keep="last")
print(df_dropped_duplicates_last)

# Drop duplicate rows based on specific columns and keep the last occurrence
print("\nDataFrame after dropping duplicate rows based on 'name' and 'city' and keeping the last occurrence:")
df_dropped_duplicates_subset_last = df.drop_duplicates(subset=["name", "city"], keep="last")
print(df_dropped_duplicates_subset_last)

# Drop duplicate rows and keep the first occurrence
print("\nDataFrame after dropping duplicate rows and keeping the first occurrence:")
df_dropped_duplicates_first = df.drop_duplicates(keep="first")
print(df_dropped_duplicates_first)

# Drop duplicate rows based on specific columns and keep the first occurrence
print("\nDataFrame after dropping duplicate rows based on 'name' and 'city' and keeping the first occurrence:")
df_dropped_duplicates_subset_first = df.drop_duplicates(subset=["name", "city"], keep="first")
print(df_dropped_duplicates_subset_first)

# Drop duplicate rows and keep none
print("\nDataFrame after dropping duplicate rows and keeping none:")
df_dropped_duplicates_none = df.drop_duplicates(keep=False)
print(df_dropped_duplicates_none)

# Drop duplicate rows based on specific columns and keep none
print("\nDataFrame after dropping duplicate rows based on 'name' and 'city' and keeping none:")
df_dropped_duplicates_subset_none = df.drop_duplicates(subset=["name"], keep=False)
print(df_dropped_duplicates_subset_none)