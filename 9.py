#numpy
#sort the matrix column-wise
import numpy as np
a=np.array([[1,8,3],[7,2,9],[4,5,6]])
sorted=np.sort(a,axis=0)
print(sorted)