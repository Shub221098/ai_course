import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Column sum:", data.sum(axis=0)) # [120 150 180]
print("Row sum:", data.sum(axis=1)) # [ 60 150 240]

print("Column average:", data.mean(axis=0)) # [40. 50. 60.]
print("Row average:", data.mean(axis=1)) # [20. 50. 80.]

print("Column max:", data.max(axis=0)) # [70 80 90]
print("Row max:", data.max(axis=1)) # [30 60 90]