#2 unsorted arrays in to Sorted numpy intersetcion arrays
import numpy as np
n1=np.array([1,9,10,25])
n2=np.array([11,9,10,28])
Intern=np.intersect1d(n1,n2)
print("Sorted Array",Intern)