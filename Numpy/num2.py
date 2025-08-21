import numpy as np

# arr = np.array([10, 20, 30, 40, 50])
# print(arr[0])   # first element → 10    It will print 0 index value
# print(arr[-1])  # last element → 50   It will print last element from the list

# matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(matrix[0, 0])  # element at row 0, col 0 → 1
# print(matrix[1, 2])  # element at row 1, col 2 → 6

# arr = np.array([10, 20, 30, 40, 50])
# print(arr[1:4])     # elements from index 1 to 3 → [20 30 40]
# print(arr[:3])      # first 3 elements → [10 20 30]
# print(arr[::2])     # every 2nd element → [10 30 50]

# matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(matrix[0:2, 1:3])   # rows 0–1, cols 1–2 → [[2 3],[5 6]]
# print(matrix[:, 1])       # all rows, column 1 → [2 5 8]
# print(matrix[1, :])       # row 1, all columns → [4 5 6]

# arr = np.array([10, 20, 30, 40, 50])
# print(arr[arr > 25])   # → [30 40 50]
# print(arr[arr % 20 == 0]) # → [20 40]

# arr = np.arange(1, 13)   # numbers 1 to 12
# matrix = arr.reshape(3, 4)   # reshape into 3x4 matrix
# print(matrix)

# print(matrix.ravel())  # flatten to 1D
# print(matrix.flatten())  # same as ravel, but makes a copy

# print(matrix.T)  # transpose rows ↔ columns




# Task 1 - Create a 1D array of numbers from 1 to 16.

arr = np.arange(1,17)
print(arr)

# Task 2 - Reshape it into a 4x4 matrix.
matrix = arr.reshape(4,4)
print(matrix)


# Task 3 - Print the 2nd row and 3rd column separately.

print(matrix[:,1])
print(matrix[2,:])

# Task 4 - Extract all even numbers using boolean indexing.
print(matrix[matrix%2==0])

# Task 5 :- Flatten the matrix into 1D.

print(matrix.ravel())