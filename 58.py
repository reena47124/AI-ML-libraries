#numpy
#shape of an array
import numpy as np
a1=np.arange(10)
a2=np.arange(12,dtype=float).reshape(3,4)
a3=np.arange(8).reshape(2,2,2)
print(a1.shape)
print(a2.shape)
print(a3.shape)