#numpy
#swap 2 rows
import numpy as np
arr = np.array([[1,2],
                [3,4],
                [5,6]])
arr[[0,2]] = arr[[2,0]]
print(arr)