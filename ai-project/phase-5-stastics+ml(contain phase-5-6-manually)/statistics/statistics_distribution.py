import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Seed set kiya hai taaki har baar exact same values generate hon
np.random.seed(42)

# ==========================================
# TASK 1: Generate 1000 normal values (Mean=50, Std=10)
# ==========================================
data1 = np.random.normal(loc=50, scale=10, size=1000)

# ==========================================
# TASK 2: Calculate Mean, Median, and Std Dev for Dataset 1
# ==========================================
mean1 = np.mean(data1)
median1 = np.median(data1)
std1 = np.std(data1)

print("=== DATASET 1 STATS (Expected: Mean=50, Std=10) ===")
print(f"Calculated Mean   : {mean1:.4f}")
print(f"Calculated Median : {median1:.4f}")
print(f"Calculated Std Dev: {std1:.4f}\n")

# ==========================================
# TASK 4 (Part 1): Generate Dataset 2 (Mean=50, Std=20)
# ==========================================
data2 = np.random.normal(loc=50, scale=20, size=1000)

mean2 = np.mean(data2)
median2 = np.median(data2)
std2 = np.std(data2)

print("=== DATASET 2 STATS (Expected: Mean=50, Std=20) ===")
print(f"Calculated Mean   : {mean2:.4f}")
print(f"Calculated Median : {median2:.4f}")
print(f"Calculated Std Dev: {std2:.4f}\n")

# ==========================================
# TASK 3 & 4 (Part 2): Plotting and Comparing Histograms
# ==========================================
plt.figure(figsize=(12, 6))

# Dataset 1 Histogram: Alpha 0.6 rakha h taaki peeche ka data dikhe
plt.hist(data1, bins=30, alpha=0.6, color='royalblue', label='Dataset 1 (Std = 10)', edgecolor='black')

# Dataset 2 Histogram
plt.hist(data2, bins=30, alpha=0.4, color='darkorange', label='Dataset 2 (Std = 20)', edgecolor='black')

# Styling and Details
plt.axvline(50, color='red', linestyle='--', linewidth=2, label='Target Mean (50)')
plt.title("Practical Analysis: How Standard Deviation Controls the Spread", fontsize=14, fontweight='bold')
plt.xlabel("Values", fontsize=12)
plt.ylabel("Frequency (Count)", fontsize=12)
plt.legend(fontsize=11)
plt.grid(axis='y', linestyle=':', alpha=0.6)

plt.tight_layout()
plt.show()