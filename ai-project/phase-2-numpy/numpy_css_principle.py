# CSS -> concatenate, stack aur split.

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Concatenate:")
print(np.concatenate([a, b]))
# Output:-
# Concatenate:
# [1 2 3 4 5 6]


print("\nStack:")
print(np.stack([a, b]))

# Output:-
# Stack:
# [[1 2 3]
#  [4 5 6]]

print("\nSplit:")
numbers = np.array([1, 2, 3, 4, 5, 6])
parts = np.split(numbers, 3)

# Output:-
# Split:
# [array([1, 2]), array([3, 4]), array([5, 6])]

print(parts)

# concatenate → existing axis par join
# stack       → new axis create karke join


# 2D arrays ke liye concatenate aur stack ka example:
a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

print(np.concatenate([a, b], axis=0))
# Output:- 
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

print(np.concatenate([a, b], axis=1))
# Output:-
# [[1 2 5 6]
#  [3 4 7 8]]


