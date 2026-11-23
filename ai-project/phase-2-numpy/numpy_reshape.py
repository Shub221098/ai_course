import numpy as np

numbers = np.array([1, 2, 3, 4, 5, 6])

print(numbers.shape)

matrix = numbers.reshape(2, 3)

print(matrix)
print(matrix.shape)


# Original:

# [1 2 3 4 5 6]
#        ↓
#     reshape
#        ↓
# [[1 2 3]
#  [4 5 6]]

# 2 × 3 = 6 -> Total elements must remain the same after reshaping.


# Can also use -1 to automatically calculate the other dimension:
# reshape(2, -1) → 2 rows, columns automatically
# reshape(-1, 2) → 2 columns, rows automatically
num1 = numbers.reshape(2, -1)

print(num1)

num2 = numbers.reshape(-1, 2)

print(num2)

# ====================================================================================================

numbers = np.array([1, 2, 3, 4, 5, 6])

print("Original:", numbers)
print("Original shape:", numbers.shape)

matrix = numbers.reshape(2, 3)

print("2D:")
print(matrix)
print("2D shape:", matrix.shape)

print("Reshape with -1:")
print(numbers.reshape(3, -1))

print("Flatten:")
print(matrix.flatten())

print("Ravel:")
print(matrix.ravel())