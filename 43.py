#numpy
#find prime numbers in numpy array
import numpy as np
arr = np.array([2,3,4,5,6,7,8,11])
for num in arr:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)