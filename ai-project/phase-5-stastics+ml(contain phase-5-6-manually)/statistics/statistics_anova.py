# ANOVA(Analysis of Variance) : Jab hume 3 ya usse zyada groups ke average (mean) compare karne hote hain,
# tab hum ANOVA use kar sakte hain.

# Example: Maan lo tum ek ML model ki performance compare kar rahe ho, jahan 3 different algorithms use
# kiye gaye hain.

# Algorithm                  Accuracy (%)
# Model A                 78, 80, 79, 81, 82
# Model B                 85, 87, 86, 84, 88
# Model C                 75, 77, 76, 74, 78

# Question: Kya in models ki average accuracy mein statistically significant difference hai?

# T-test vs ANOVA

#                 T-test                                                 ANOVA
# Generally 2 groups ke means compare karta hai       3 ya usse zyada groups ke means compare kar sakta hai
# Example: Model A vs Model B                         Example: Model A vs B vs C
# t-statistic                                         F-statistic


import numpy as np
from scipy import stats

def find_anova(model_a, model_b, model_c):
    # --- ANOVA TEST KA KHEL ---
    f_stat, p_value = stats.f_oneway(
        model_a,
        model_b,
        model_c
    )
    print("=== ONE-WAY ANOVA RESULT ===")
    print(f"Calculated F-Statistic: {f_stat:.4f}")
    print(f"Calculated P-Value: {p_value:.4e}")  # Scientific notation mein print hoga kyunki value bohot choti hai


    # Decision Layer
    alpha = 0.05
    if p_value < alpha:
        print("\nDecision: Reject H0")
        print("Asli Matlab: Kam se kam ek company ki car ka average range baakiyon se alag hai! (Significant Difference)")
    else:
        print("\nDecision: Fail to reject H0")
        print("Asli Matlab: Saari companies lagbhag same range de rahi hain. Koi farak nahi hai.")


model_a = [78, 80, 79, 81, 82]
model_b = [85, 87, 86, 84, 88]
model_c = [75, 77, 76, 74, 78]

find_anova(model_a, model_b, model_c)


# Seed fix kiya taaki data change na ho
np.random.seed(42)

# 3 alag-alag companies ki cars ka sample data (n=5 each)
tata_ev = [145, 148, 150, 147, 149]
mahindra_ev = [155, 158, 160, 156, 159]
mg_ev = [135, 138, 140, 137, 139]

find_anova(tata_ev, mahindra_ev, mg_ev)

# H₀: Mean A = Mean B = Mean C
# F = Between-group variation
#     -------------------------
#      Within-group variation
# Teeno population means equal hain, is claim ke against statistically significant evidence mila.


################# Post-Hoc Testing → Tukey HSD ###################################
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd

model_a = [78, 80, 79, 81, 82]
model_b = [85, 87, 86, 84, 88]
model_c = [75, 77, 76, 74, 78]

scores = model_a + model_b + model_c

groups = (
    ["A"] * len(model_a)
    + ["B"] * len(model_b)
    + ["C"] * len(model_c)
)

result = pairwise_tukeyhsd(
    endog=scores,
    groups=groups,
    alpha=0.05
)

print(result)

# Output:
#  Multiple Comparison of Means - Tukey HSD, FWER=0.05 
# =====================================================
# group1 group2 meandiff p-adj   lower    upper  reject
# -----------------------------------------------------
#      A      B      6.0 0.0002   3.3321  8.6679   True
#      A      C     -4.0 0.0046  -6.6679 -1.3321   True
#      B      C    -10.0    0.0 -12.6679 -7.3321   True

# A ≠ B
# A ≠ C
# B ≠ C