import numpy as np

# From a Python list
# arr1 = np.array([1, 2, 3, 4, 5])
# print(arr1)

# Multi-dimensional array
# arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr2)

# print(np.zeros((2, 3)))   # 2x3 array of zeros
# print(np.ones((3, 3)))    # 3x3 array of ones
# print(np.arange(0, 10, 2)) # numbers from 0 to 9 step 2
# print(np.linspace(0, 1, 5)) # 5 values evenly spaced between 0 and 1

# arr = np.array([[1,2,3],[4,5,6]])
# print(arr.shape)   # (2, 3) → rows x columns
# print(arr.ndim)    # 2 → dimensions
# print(arr.dtype)   # int64 (depends on system)
# print(arr.size)    # 6 elements

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# print(a + b)   # [5 7 9]
# print(a * b)   # [ 4 10 18]
# print(a ** b)  # [1 4 9]
# # print(b ** b)
# print(np.dot(a, b))  # dot product = 32



#Task :- Create a 1D NumPy array with numbers from 10 to 50 (inclusive).


arr = np.arange(10,51,1)
print(arr)


# Task - Create a 3x3 matrix filled with random integers between 1 and 100.

arr1 = np.random.randint(1,100,size=(3,3))
print(arr1)


# Task 3 - Find the sum, mean, and standard deviation of the matrix.

print(np.sum(arr1))


print(np.mean(arr1))

print(np.std(arr1))