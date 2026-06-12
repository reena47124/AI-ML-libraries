#numpy
#find the rank of the array
import numpy as np
A = np.array([[1,2,3],
              [2,4,6],
              [1,1,1]])
print(np.linalg.matrix_rank(A))