from collections import Counter
import statistics
import numpy as np

marks = [45, 55, 60, 60, 65, 70, 75, 80, 95]

# --- 1. Pure Python & NumPy ---
mean_val = np.mean(marks)  # or sum(marks) / len(marks)
median_val = np.median(marks)
mode_val = Counter(marks).most_common(1)[0][0]
marks = [45, 55, 60, 60, 65, 70, 75, 80, 95]

# 1. Counter(marks)                 ->  {60: 2, 45: 1, ...}
# 2. .most_common(1)                ->  [(60, 2)]          (list of top 1)
# 3. [0]                            ->  (60, 2)            (extract tuple)
# 4. [0]                            ->  60                 (extract value)

print("--- Method 1 (NumPy + Collections) ---")
print(f"Mean:   {mean_val:.2f}")
print(f"Median: {median_val}")
print(f"Mode:   {mode_val}")

# --- 2. Using Python's built-in statistics module ---
print("\n--- Method 2 (Built-in statistics module) ---")
print(f"Mean:   {statistics.mean(marks):.2f}")
print(f"Median: {statistics.median(marks)}")
print(f"Mode:   {statistics.mode(marks)}")