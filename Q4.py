#Q4. Define two-dimensional array with values {(5,4),(6,3)}. Output eigen values and
#eigenvectors of the matrix.


import scipy.linalg as la
import numpy as np


x = np.array([[5,4], 
              [6,3]])

eigvals, eigvecs = la.eig(x) #eigen function for a square matrix. Return eigen values and eigen vector.
print(eigvals) #eigen values
print("\n")
print(eigvecs) #eigen vector
