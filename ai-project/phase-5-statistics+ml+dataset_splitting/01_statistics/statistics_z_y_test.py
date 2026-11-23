import numpy as np

#     Feature                             Criteria Z-Test                                                      T-Test
# Sample Size (n)              Bada hona chahiye (n > 30)                                               Chhota ho toh chalta hai (n ≤ 30)
# Population Std Dev (σ)       Known (Pata hota hai)                                                    Unknown (Nahi pata hota)
# Distribution Shape           Perfectly Normal Distribution (Bell Curve)                               Student's T-Distribution (Flatter tails hote hain)
# Real World Use               Bohot kam use hota hai (Kyunki σ milna mushkil hai)                      Har jagah use hota hai (A/B Testing, Clinical Trials)

# Y-test ke liye hum scipy use karte hain
from scipy import stats
# Company ka claim hai ki target mean range 150 km hai
claimed_mean = 150

# Humne sirf 12 gadiyon ka sample data collect kiya (Small Data, n=12)
sample_ev_range = [148, 152, 145, 149, 151, 147, 146, 153, 144, 150, 148, 147]

# T-Test lagaya kyunki data chhota hai aur population std dev nahi pata
t_stat, p_value = stats.ttest_1samp(sample_ev_range, claimed_mean)

print(f"Sample Size: {len(sample_ev_range)}")
print(f"Calculated T-Statistic: {t_stat:.4f}")
print(f"Calculated P-Value: {p_value:.4f}")

# Decision Layer
alpha = 0.05
if p_value < alpha:
    print("Decision: Reject H0 -> Company ka 150km ka claim galat hai!")
else:
    print("Decision: Fail to reject H0 -> Company ka 150km ka claim sahi lag raha hai.")


# Z-test ke liye hum statsmodels use karte hain
from statsmodels.stats.weightstats import ztest

# Seed fix kiya taaki har baar exact same large data generate ho
np.random.seed(42)

# Company ka background claim hai ki target mean range 150 km hai
claimed_mean = 150

# SCENARIO: Humne 50 gadiyon ka data test kiya (Large Data, n=50)
# Data generate kiya jiska actual mean ~149.2 hai aur std dev 2.5 hai
sample_ev_range = np.random.normal(loc=149.2, scale=2.5, size=50)

# --- Z-TEST KA KHEL ---
# ztest() ko do main inputs chahiye: hamara sample data aur target value (value)
z_stat, p_value = ztest(sample_ev_range, value=claimed_mean)

print(f"Sample Size: {len(sample_ev_range)}")
print(f"Calculated Z-Statistic: {z_stat:.4f}")
print(f"Calculated P-Value: {p_value:.4f}")

# Decision Layer
alpha = 0.05
if p_value < alpha:
    print("Decision: Reject H0 -> Company ka 150km ka claim galat hai! (Data ne jhoot pakad liya)")
else:
    print("Decision: Fail to reject H0 -> Company ka 150km ka claim sahi lag raha hai.")