import scipy.linalg as la
import numpy as np


x = np.array([[5,4], 
              [6,3]])

eigvals, eigvecs = la.eig(x)
print(eigvals)
print("\n")
print(eigvecs)