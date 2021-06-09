import scipy.io as sio
import numpy as np

x = np.array([[1, 2, 3,4], 
              [5, 6,7,8],
              [9,10,11,12],
              [13,14,15,16]])

sio.savemat('test.mat', {"f":x})
data = sio.loadmat('test.mat')
print(data)