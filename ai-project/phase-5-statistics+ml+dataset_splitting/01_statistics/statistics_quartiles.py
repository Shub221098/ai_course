import statistics
import numpy as np

marks = [45, 55, 60, 60, 65, 70, 75, 80, 95,150]

# ==========================================
# 1. NumPy Method (np.percentile / np.quantile)
# ==========================================
# Percentile 0 se 100 leta hai
q1_np = np.percentile(marks, 25)
q2_np = np.percentile(marks, 50)  # Median
q3_np = np.percentile(marks, 75)
iqr_np = q3_np - q1_np

# ==========================================
# 2. Python Built-in statistics Method
# ==========================================
# statistics.quantiles(data, n=4) seedha [Q1, Q2, Q3] deta hai
q1_stat, q2_stat, q3_stat = statistics.quantiles(marks, n=4)
iqr_stat = q3_stat - q1_stat

print("--- Using NumPy ---")
print(f"Q1 (25th Percentile): {q1_np}")
print(f"Q2 (50th Percentile): {q2_np}")
print(f"Q3 (75th Percentile): {q3_np}")
print(f"IQR (Q3 - Q1):        {iqr_np}")

print("\n--- Using statistics module ---")
print(f"Q1:  {q1_stat}")
print(f"Q2:  {q2_stat}")
print(f"Q3:  {q3_stat}")
print(f"IQR: {iqr_stat}")


lower_bound = q1_stat - 1.5 * iqr_stat
upper_bound = q3_stat + 1.5 * iqr_stat

print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

outliers = [
    x for x in marks
    if x < lower_bound or x > upper_bound
]

print("Outliers:", outliers)