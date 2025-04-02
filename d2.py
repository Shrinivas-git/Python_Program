import numpy as np
matrix=np.array([[4,3],[7,3]])
eigenvalues,eigenvectors=np.linalg.eig(matrix)
print("eigenvalues",eigenvalues)
