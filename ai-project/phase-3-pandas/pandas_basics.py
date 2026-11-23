import pandas as pd

print(pd.__version__)


# Creating a Series (Series = one-dimensional labeled data)
ages = pd.Series([25, 30, 28, 35])

print(ages)

# Series indexing

print(ages[0])  # Accessing the first element
print(ages[1:3])  # Slicing the Series


# Creating a DataFrame (DataFrame = two-dimensional labeled data[rows + columns ka table])
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 28, 35],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)

print(df)

# DataFrame indexing
print(df['Name'])  # Accessing a single column
print(df[['Name', 'Age']])  # Accessing multiple columns


# Practical Example: Analyzing Student Scores with Pandas
data = {
    "name": ["Rahul", "Amit", "Priya", "Neha"],
    "age": [25, 30, 28, 32],
    "city": ["Surat", "Delhi", "Mumbai", "Pune"],
    "salary": [40000, 55000, 60000, 70000]
}

df = pd.DataFrame(data)

print(df)
# Output:- 
#     name  age    city  salary
# 0   Rahul   25   Surat   40000
# 1   Amit   30   Delhi   55000
# 2   Priya   28   Mumbai   60000
# 3   Neha   32   Pune   70000

print("\n--- Age ---")
print(df["age"])
# Output:-
# 0    25
# 1    30
# 2    28
# 3    32

print("\n--- Name + Salary ---")
print(df[["name", "salary"]])
# Output:-
#     name  salary
# 0   Rahul   40000
# 1   Amit   55000
# 2   Priya   60000
# 3   Neha   70000


print(df.shape)
print(df.columns)
print(df["salary"].mean())

# 

# First 5 rows
print(df.head())

# Last 5 rows
print(df.tail())

print("HEAD:")
print(df.head(2))

print("\nTAIL:")
print(df.tail(2))

print("\nINFO:")
df.info()

print("\nDESCRIBE:")
print(df.describe())