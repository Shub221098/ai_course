import numpy as np

# Confidence Interval (CI) : Agar mere paas poori population ka data nahi hai, toh sample ke basis par population mean ka reasonable range kaise estimate karun?


sample_mean = 500
population_std = 100
sample_size = 100

standard_error = population_std / np.sqrt(sample_size)

margin_of_error = 1.96 * standard_error

lower = sample_mean - margin_of_error
upper = sample_mean + margin_of_error

print("Standard Error:", standard_error)
print("Margin of Error:", margin_of_error)
print("Lower Bound:", lower)
print("Upper Bound:", upper)

# Practice Assignment

# Given:

# sample_mean = 750
# population_std = 120

# Calculate 95% confidence interval for:

# Task 1
# sample_size = 25
# Task 2
# sample_size = 100
# Task 3
# sample_size = 400

# For each calculate:

# 1. Standard Error
# 2. Margin of Error
# 3. Lower Bound
# 4. Upper Bound
# 🎯 Final observation

# Compare the three intervals and answer:

# Sample size increase hone par Confidence Interval ke width mein kya change hua?

sample_mean = 750
population_std = 120

def calculate_confidence_interval(sample_size):
    print(f"Calculating Confidence Interval for sample size: {sample_size}")
    standard_error = population_std / np.sqrt(sample_size)
    print(f"Standard Error for sample size: {sample_size}: {standard_error}")
    margin_of_error = 1.96 * standard_error
    print(f"Margin of Error for sample size: {sample_size}: {margin_of_error}")
    lower_bound = sample_mean - margin_of_error
    print(f"Lower Bound for sample size: {sample_size}: {lower_bound}")
    upper_bound = sample_mean + margin_of_error
    print(f"Upper Bound for sample size: {sample_size}: {upper_bound}")

    print(f"Final Confidence Interval for sample size: {sample_size} is between {lower_bound} and {upper_bound}")

calculate_confidence_interval(25)
calculate_confidence_interval(100)
calculate_confidence_interval(400)

# Sample size ↑ → Standard Error ↓ → Margin of Error ↓ → Confidence Interval narrower