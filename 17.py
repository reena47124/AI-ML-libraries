#numpy
#stack two arrays
import numpy as np
x = np.array([1,2,3])
y = np.array([4,5,6])
print(np.stack((x,y), axis=1))