import numpy as np

# Create two random 3x3 integer matrices
A = np.random.randint(1, 11, size=(3, 3))
B = np.random.randint(1, 11, size=(3, 3))

print("Matrix A:\n", A)
print("\nMatrix B:\n", B)

# Matrix addition
add = A + B
print("\nA + B:\n", add)

# Matrix multiplication
multiply = A @ B   # or np.dot(A, B)
print("\nA @ B (Matrix Multiplication):\n", multiply)
