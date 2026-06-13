#numpy
#find second largest
import numpy as np
arr = np.array([10, 25, 8, 40, 15])
second_largest = np.sort(arr)[-2]
print(second_largest)