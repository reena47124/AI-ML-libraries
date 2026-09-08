#numpy
#changing datatype
import numpy as np
a1=np.arange(12).reshape(3,4)
a2=np.arange(12,24).reshape(3,4)
print(a1.dtype)
b1=a1.astype(np.int32)
print(b1.dtype)