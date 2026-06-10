#numpy
#find column-wise maximum
import numpy as np
a=np.array([[1,5,2],[8,3,4],[7,9,6]])
print(np.max(a,axis=0))