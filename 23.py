#numpy
#find eigenvalues and eigenvectors
import numpy as np
a=np.array([[1,5,2],[8,3,4],[7,9,6]])
eigenvalues,eigenvectors=np.linalg.eig(a)
print(eigenvalues)
print(eigenvectors)
