import numpy as np
matrix = np.array([[11, 22], [33, 44]])
vector = np.array([1, 0])
vector2 = np.array([55, 66])

dot_product = np.dot(vector, vector2)
print("Dot product of vectors:", dot_product)


inner_product = np.inner(vector, vector2)
print("Inner product of vectors:", inner_product)


outer_product = np.outer(vector, vector2)
print("Outer product of vectors:\n", outer_product)
matrix2 = np.array([[2, 0], [1, 2]])
matrix_product = np.dot(matrix, matrix2)
print("Matrix product:\n", matrix_product)
matrix_power = np.linalg.matrix_power(matrix2, 2)  
print("Matrix power (squared):\n", matrix_power)
