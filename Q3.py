from scipy import linalg
import numpy as np

x = np.array([[4,5], 
              [3,2]])
y = linalg.det(x)

z = linalg.inv(x)

print(y)

print("\n")

print(z)