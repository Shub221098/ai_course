import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)
print(type(numbers)) # <class 'numpy.ndarray'> ==> ndarray = NumPy ka main array object.
print(numbers.dtype) # Ye batata hai array ke elements kis numerical data type ke hain.
print(numbers.shape) # 5 elements 1 dimension (Abhi ye 1-dimensional array hai.)


# List me hum +, *, /, ** operators ka use nahi kar sakte. Lekin NumPy arrays me hum ye operations directly kar sakte hain.

# Python List me ye operations kaise kaam karte hain:
# numbers_list = [10, 20, 30, 40, 50]
# print([x + 10 for x in numbers_list]) # [20, 30, 40, 50, 60]
# print([x * 2 for x in numbers_list]) # [20, 40, 60, 80, 100]
# print([x / 10 for x in numbers_list]) # [1.0, 2.0, 3.0, 4.0, 5.0]
# print([x ** 2 for x in numbers_list]) # [100, 400, 900, 1600, 2500]

# numbers = [10, 20, 30]

# print(numbers * 2)  => [10, 20, 30, 10, 20, 30] (Ye list ko repeat kar deta hai)

# NumPy arrays me ye operations kaise kaam karte hain:
numbers = np.array([10, 20, 30, 40, 50])

print(numbers + 10) # [20 30 40 50 60]
print(numbers * 2) # [ 20  40  60  80 100]
print(numbers / 10) # [1. 2. 3. 4. 5.]
print(numbers ** 2) # [ 100  400  900 1600 2500]


print(numbers * 1.10)# 10% increase
print(numbers * 2) # double price
print(numbers ** 2) # square
print(numbers.shape) # shape
print(numbers.dtype) # dtype


# 1 diensional and 2 dimensional arrays

# 1D
a = np.array([10, 20, 30, 40])

# 2D
b = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(a)
print(a.shape)

print(b)
print(b.shape)


data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(data[0, 2]) # 30
print(data[2, 1]) # 80
print(data[1]) # [40 50 60]
print(data[:, 0]) # [10 40 70] => Ye batata hai ki humne saare rows ke liye column 0 select kiya hai.
print(data[:, 2]) # [30 60 90] => Ye batata hai ki humne saare rows ke liye column 2 select kiya hai.


# Vectorization => Ye ek technique hai jisme hum loops ke bina hi operations perform kar sakte hain. 
# Ye NumPy ka main feature hai. 

# Broadcasting => Ye ek technique hai jisme hum different shapes ke arrays ke saath operations perform
# kar sakte hain.
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b) # [11 22 33] => Ye element wise addition hai.
print(a * b) # [10 40 90] => Ye element wise multiplication hai

# Matrix multiplication hum baad mein @ aur np.matmul() se dekhenge.