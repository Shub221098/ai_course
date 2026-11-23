import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Seed set kiya taaki tumhara aur mera output exact match kare
np.random.seed(42)

# --- TASK 1: Synthetic Data Setup ---
# 10 students ka studying hours (1 se 10 ghante)
studying_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Marks hum hours ke directly proportional banayenge par thoda random noise (disturbance) add karenge
# marks = (hours * 8) + 15 + random noise
exam_marks = (studying_hours * 8) + 15 + np.random.randint(-5, 6, size=10)

# DataFrame create kiya
df = pd.DataFrame({
    'studying_hours': studying_hours,
    'exam_marks': exam_marks
})

print("--- Dataset ---")
print(df)

# --- TASK 2: Covariance Matrix ---
# df.cov() hume poori matrix deta hai
cov_matrix = df.cov()
# studying_hours aur exam_marks ka actual covariance nikalne ke liye:
actual_cov = cov_matrix.loc['studying_hours', 'exam_marks']

print("\n--- Covariance Matrix ---")
print(cov_matrix)
print(f"Covariance between Hours and Marks: {actual_cov:.2f}")

# --- TASK 3: Correlation Matrix ---
corr_matrix = df.corr()
actual_corr = corr_matrix.loc['studying_hours', 'exam_marks']

print("\n--- Correlation Matrix ---")
print(corr_matrix)
print(f"Pearson Correlation (r): {actual_corr:.4f}")


plt.scatter(df["studying_hours"], df["exam_marks"])
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.title("Studying Hours Vs Exam Marks")

plt.tight_layout()
plt.show()