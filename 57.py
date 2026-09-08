#numpy
#no of dimensions
import numpy as np
a1=np.arange(10)
a2=np.arange(12,dtype=float).reshape(3,4)
a3=np.arange(8).reshape(2,2,2)
b1=a1.ndim
print(b1)
print(a2.ndim)
print(a3.ndim)

