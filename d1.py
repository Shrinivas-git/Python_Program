import numpy as np

# Define the matrix correctly using a list of lists
matrix = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])

# Function to calculate matrix properties
def matrix_properties(matrix):
    rank = np.linalg.matrix_rank(matrix)  # Calculate rank of the matrix
    determinant = np.linalg.det(matrix)   # Calculate determinant of the matrix
    trace = np.trace(matrix)              # Calculate trace of the matrix
    return rank, determinant, trace        # Return the results

# Call the function and unpack the returned values
rank, determinant, trace = matrix_properties(matrix)

# Print the matrix and its properties
print("Matrix:\n", matrix)
print("\nRank of the matrix:", rank)
print("\nDeterminant of the matrix:", determinant)
print("\nTrace of the matrix:", trace)
