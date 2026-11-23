import pandas as pd

data = {
    "name": ["Rahul", "Amit", "Priya", "Neha", "Raj", "Karan"],
    "city": ["Surat", "Delhi", "Mumbai", "Surat", "Delhi", "Surat"],
    "salary": [40000, 55000, 60000, 70000, 45000, 50000]
}

df = pd.DataFrame(data)

print(df)


# Group by 'city'
print("\nGroup by City:")
group_city = df.groupby("city")
print(group_city)


# Group by 'city' and calculate the mean salary
print("\nMean Salary by City:")
mean_salary_by_city = df.groupby("city")["salary"].mean()
print(mean_salary_by_city)

# Group by 'city' and calculate the total salary
print("\nTotal Salary by City:")
total_salary_by_city = df.groupby("city")["salary"].sum()
print(total_salary_by_city)

# Group by 'city' and calulcate total count of employees
print("\nTotal Employees Count by City:")
total_employee_count_by_city = df.groupby("city")["name"].count()
print(total_employee_count_by_city)

# Group by 'city' and caluclate the maximum salary
print("\nMaximum Salary by City:")
maximum_salary_by_city = df.groupby('city')["salary"].max()
print(maximum_salary_by_city)

# Group by 'city' and caluclate the minimum salary
print("\nMinimum Salary by City:")
minimum_salary_by_city = df.groupby('city')["salary"].min()
print(minimum_salary_by_city)

# Multiple Calculations
print("\nMultiple Calculations by aggregation")
aggregate_results = df.groupby("city")["salary"].agg(
    ["mean", "min", "max"]
)
print(aggregate_results)

# Different column, different aggregation
print("\nMultiple aggregation on multiple columns")
aggregate_multiple_columns = df.groupby("city").agg(
    average_salary=("salary", "mean"),
    employee_count=("name", "count")
)
print(aggregate_multiple_columns)
