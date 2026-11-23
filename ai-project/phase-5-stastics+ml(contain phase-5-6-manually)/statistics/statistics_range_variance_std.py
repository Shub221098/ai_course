import statistics
import numpy as np

marks = [45, 55, 60, 60, 65, 70, 75, 80, 95]

# ==========================================
# 1. Using NumPy
# ==========================================
np_min = np.min(marks)
np_max = np.max(marks)
np_range = np.ptp(marks)  # ptp = "peak to peak" (max - min)
np_mean = np.mean(marks)

# Population (N) vs Sample (N - 1)
np_var_pop = np.var(marks)  # default: ddof=0 (population)
np_var_sample = np.var(marks, ddof=1)  # sample

np_std_pop = np.std(marks)  # default: ddof=0 (population)
np_std_sample = np.std(marks, ddof=1)  # sample

# ==========================================
# 2. Using Built-in statistics module
# ==========================================
stat_min = min(marks)
stat_max = max(marks)
stat_range = stat_max - stat_min
stat_mean = statistics.mean(marks)

# Built-in methods: 'p' prefix stands for Population
stat_var_pop = statistics.pvariance(marks)  # population
stat_var_sample = statistics.variance(marks)  # sample

stat_std_pop = statistics.pstdev(marks)  # population
stat_std_sample = statistics.stdev(marks)  # sample

# ==========================================
# Side-by-Side Output Table
# ==========================================
print(f"{'Metric':<25} | {'NumPy':<15} | {'statistics module':<15}")
print("-" * 60)
print(f"{'1. Minimum':<25} | {np_min:<15} | {stat_min:<15}")
print(f"{'2. Maximum':<25} | {np_max:<15} | {stat_max:<15}")
print(f"{'3. Range':<25} | {np_range:<15} | {stat_range:<15}")
print(f"{'4. Mean':<25} | {np_mean:<15.2f} | {stat_mean:<15.2f}")
print(f"{'5. Variance (Pop / N)':<25} | {np_var_pop:<15.2f} | {stat_var_pop:<15.2f}")
print(
    f"{'   Variance (Sample / N-1)':<25} | {np_var_sample:<15.2f} |"
    f" {stat_var_sample:<15.2f}"
)
print(f"{'6. Std Dev (Pop / N)':<25} | {np_std_pop:<15.2f} | {stat_std_pop:<15.2f}")
print(
    f"{'   Std Dev (Sample / N-1)':<25} | {np_std_sample:<15.2f} |"
    f" {stat_std_sample:<15.2f}"
)