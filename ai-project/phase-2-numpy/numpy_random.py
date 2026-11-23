import numpy as np

# Random numbers between 0 and 1
numbers = np.random.rand(5)

print(numbers)

# Random integers between 1 and 100
random_integers = np.random.randint(1, 101, size=5)

print(random_integers)

# 2D random dataset of shape (3, 4)
random_2d = np.random.rand(3, 4)

print(random_2d)

data = np.random.randint(1, 101, (5, 3))

print(data)
print(data.shape)


# Random but reproducible
np.random.seed(42)

data = np.random.randint(1, 101, (5, 4))

print(data)
print("Shape:", data.shape)

print("Column average:", data.mean(axis=0))
print("Row average:", data.mean(axis=1))

print("Maximum:", data.max())
print("Minimum:", data.min())