import numpy as np

# arr = np.array([1, 2, 3, 4, 5])

# print(np.sum(arr))    # 15
# print(np.mean(arr))   # 3.0
# print(np.min(arr))    # 1
# print(np.max(arr))    # 5
# print(np.std(arr))    # standard deviation
# print(np.var(arr))    # variance

# matrix = np.array([[1,2,3],
#                    [4,5,6],
#                    [7,8,9]])

# print(np.sum(matrix, axis=0))  # column-wise sum → [12 15 18] 
# print(np.sum(matrix, axis=1))  # row-wise sum → [ 6 15 24]


# arr = np.array([1, 2, 3, 4, 5])

# print(np.sqrt(arr))   # square root
# print(np.exp(arr))    # exponential
# print(np.log(arr))    # natural log
# print(np.sin(arr))    # sine
# print(np.cos(arr))    # cosine

# print(np.random.rand(3))       # 3 random floats between 0 and 1
# print(np.random.randint(1, 10, 5))  # 5 random integers [1,10)


# print(np.random.rand(2, 3))      # 2x3 matrix of random floats
# print(np.random.randint(0, 100, (3, 3)))  # 3x3 random integers

# np.random.seed(42)
# print(np.random.rand(3))   # same result every time


# Task 1 - Create a 5x5 matrix of random integers between 10 and 50.
# matrix = np.random.randint(10,51,(5,5))
# print(matrix)

# # Task 2 - Find the row-wise maximum and column-wise mean.
# print(np.sum(matrix, axis = 0))
# print(np.mean(matrix, axis = 1))


# Task 3 - Create an array of 100 random numbers between 0 and 1 → find its mean

# matrix1 = np.array(np.random.rand(1,100))

# print(matrix1)
# print(np.mean(matrix1))


# Task 4 - Generate a random 3x3 matrix → then transpose it.

matrix = np.random.rand(3,3)
print(matrix)
print(matrix.T)