#Addition operation on Numpy Array
import numpy as np
n1=np.array([1,2,3,4,5])
n2=np.array([2,3,4,5,6])
n1=n1+10
n2=n2+20
print("Addition of updated array 1",n1)
print("Addition of updated array 2",n2)

#Extra Practice
print("Sum of two arrays",np.sum([n1,n2]))
print("Sum of two arrays",np.sum([n1,n2],axis=0))
print("Sum of two arrays",np.sum([n1,n2],axis=1))