import numpy as np

# mean() — Average
marks = np.array([40, 50, 60, 70, 80])

print(np.mean(marks)) # 60.0

# median() — Middle value
marks = np.array([40, 50, 60, 70, 80])

print(np.median(marks)) # 60.0

# min() and max()
marks = np.array([40, 50, 60, 70, 80])

print(marks.min()) # 40
print(marks.max()) # 80

# std() — Standard Deviation
marks = np.array([40, 50, 60, 70, 80])

print(np.std(marks)) # 14.142135623730951

# small std → values relatively close
# large std  → values more spread out

# Axis Statistics
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(np.mean(data, axis=0))  # Mean of each column [40. 50. 60.]
print(np.mean(data, axis=1))  # Mean of each row [20. 50. 80.]


### Normalization and Standardization
# Normalization (Min-Max Scaling)

data = np.array([10, 20, 30, 40, 50])
normalized_data = (data - np.min(data)) / (np.max(data) - np.min(data))
print(normalized_data)  # [0.   0.25 0.5  0.75 1.  ]


# Standardization (Z-score Normalization)
data = np.array([10, 20, 30, 40, 50])
standardized_data = (data - np.mean(data)) / np.std(data)
print(standardized_data)  # [-1.41421356 -0.70710678  0.          0.70710678  1.41421356]


# Practical Example: Analyzing Student Scores

marks = np.array([40, 50, 60, 70, 80])

print("Mean:", marks.mean())
print("Median:", np.median(marks))
print("Min:", marks.min())
print("Max:", marks.max())
print("Std:", marks.std())

x = np.array([10, 20, 30, 40, 50])

normalized = (x - x.min()) / (x.max() - x.min())

print("Original:", x)
print("Normalized:", normalized)