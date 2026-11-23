# Hypothesis Testing
# │
# ├── T-Test              → Numerical / Mean
# ├── Z-Test              → Numerical / Mean
# ├── One/Tail Tests      → Direction
# ├── Type I / Type II    → Errors
# ├── Statistical Power
# └── Chi-Square          → Categorical / Counts

# Chi Sqaure Test: Observed categorical data aur expected categorical data ke beech difference statistically
# significant hai ya nahi, ye check karta hai.

# Types:

# 1. Goodness of Fit :- One Categorial variable => Category → A, B, C, D
# 2. Test of Independence -> Two Categorial variable => Gender + Product Preference

from scipy import stats


# 1. Goodness of Fit :- One Categorial variable => Category → A, B, C, D

def find_p_value_and_chi_stat(observed, expected):
    print(f"Caluclation of Chi Square")
    chi_stat, p_value = stats.chisquare(
        observed,
        f_exp=expected
    )
    print("Chi-Square Statistic:", chi_stat)
    print("P-value:", p_value)

    alpha = 0.05

    if p_value < alpha:
        print("Reject H0")
    else:
        print("Fail to reject H0")

observed = [18, 22, 27, 33]
expected = [25, 25, 25, 25]

find_p_value_and_chi_stat(observed, expected)

# Practical Assignment
from scipy import stats

observed = [20, 30, 25, 25]
expected = [25, 25, 25, 25]

find_p_value_and_chi_stat(observed, expected)
# Output:
# Caluclation of Chi Square
# Chi-Square Statistic: 2.0
# P-value: 0.5724067044708798
# Fail to reject 

# Observed aur expected mein difference hai, but statistical evidence sufficient nahi
# hai ki distribution genuinely expected distribution se different hai.


# 🔥 Chi-Square statistic manually

# Formula:

# χ2= ∑((O−E)2/E)

# Categories:

# A: (20 - 25)² / 25 = 1
# B: (30 - 25)² / 25 = 1
# C: (25 - 25)² / 25 = 0
# D: (25 - 25)² / 25 = 0

# Total:

# χ² = 1 + 1 + 0 + 0 = 2.0


# 2. Test of Independence -> Two Categorial variable => Gender + Product Preference
import numpy as np

def find_p_value_and_chi_stat_contingency(observed):
    print(f"Caluclation of Chi Square Contingency")
    chi_stat, p_value, dof, expected = stats.chi2_contingency(observed)

    print("Chi-Square Statistic:", chi_stat)
    print("P-value:", p_value)
    print("Degrees of Freedom:", dof)
    print("Expected Frequencies:")
    print(expected)

    alpha = 0.05

    if p_value < alpha:
        print("Reject H0")
    else:
        print("Fail to reject H0")

observed = np.array([
    [40, 20],
    [25, 35]
])

find_p_value_and_chi_stat_contingency(observed)

# Practical Assignment - Test of Independence

observed = np.array([
    [30, 20],
    [20, 30]
])

find_p_value_and_chi_stat_contingency(observed)

# Degree of Freedom manually
# df=(rows−1)(columns−1) = (2-1)(2-1)= 1*1 = 1