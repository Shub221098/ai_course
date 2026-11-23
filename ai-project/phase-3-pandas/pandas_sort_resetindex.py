import pandas as pd

data = {
    "name": ["Rahul", "Amit", "Priya", "Neha", "Raj", "Karan"],
    "city": ["Surat", "Delhi", "Mumbai", "Surat", "Delhi", "Surat"],
    "salary": [40000, 55000, 60000, 70000, 45000, 50000]
}

df = pd.DataFrame(data)

print(df)

# Sort Salary in ascending
print("\nSort Salary in ascending")
salary_sort_asc = df.sort_values("salary")
print(salary_sort_asc)

# Sort Salary in descending
print("\nSort Salary in descending")
salary_sort_desc = df.sort_values("salary", ascending=False)
print(salary_sort_desc)

# Sort Multiple columns in different order
print("\nSort Multiple Columns on asc or desc order")
sort_multiple_columns = df.sort_values(["city", "salary"], ascending=[True, False])
print(sort_multiple_columns)

# Sort Group by result
print("\nSort GroupBy Result")
average_mean = df.groupby("city")["salary"].mean()
print(average_mean)
sort_avg_mean = average_mean.sort_values(ascending=False)
print(sort_avg_mean)

# Reset Index
avg_salary = df.groupby("city")["salary"].mean()
# After doing this above operation, city becomes index, it is no more a column
print("\nType of avg salary:")
print(type(avg_salary)) # Pandas.Series
print("\nIndexed city average salary:")
print(avg_salary)
print("\nReset Index city to make it column again:")
avg_salary = df.groupby("city")["salary"].mean().reset_index()
print(avg_salary)

# Groupby, Reset Index, Sort
print("\nGroupby with reset_index, and sorting")
results = df.groupby("city")["salary"].mean().reset_index().sort_values("salary")
print(results)

# groupby, aggregation on avg_salary, sorting on avg_salary
print("\nGroupby with aggregation result on avg_salary and sort on avg salary")
result = (
    df.groupby("city")
    .agg(average_salary=("salary", "mean"))
    .reset_index()
    .sort_values("average_salary", ascending=False)
)
print(result)