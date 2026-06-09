#numpy
#replace values
import numpy as np
a = np.array([1,4,7,2,8,5])
a[a > 5] = 0
print(a)