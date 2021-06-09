#Q1. Import the essential library scipy with i/o package and Numpy. Create a 4 x 4 dimensional
#one's array. Store array in test.text file. Get data from test.text file and print the output.

import scipy.io as sio
import numpy as np

x = np.array([[1, 2, 3,4], 
              [5, 6,7,8],
              [9,10,11,12],
              [13,14,15,16]])

sio.savemat('test.txt', {"f":x})
data = sio.loadmat('test.txt')
print(data)
