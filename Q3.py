#Q3. Create two matrices with 2x2 dimensions. Initialize them with values [4,5], [3,2]. Calculate
#determinant of a two-dimensional matrix using scipy.linalg. Calculate the inverse of a matrix
#in 3.

from scipy import linalg
import numpy as np

x = np.array([[4,5], 
              [3,2]])

y = linalg.det(x) #Compute the determinant of a matrix

z = linalg.inv(x) #Compute the inverse of a matrix.

print(y)

print("\n")

print(z)
