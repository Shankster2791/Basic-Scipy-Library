#Q2. Find cubic root of 27, 64, 891 using sciPy special package.

from scipy.special import cbrt

res = cbrt([27, 64, 891]) #Element-wise cube root of array.
print(res)
