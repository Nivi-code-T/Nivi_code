#1D Add only column values of numpy arrays using the axis parameter
import numpy as np
n1=np.array([1,2,3,4,5])
n2=np.array([6,7,8,9,10])
print("Sum of Column values",np.sum([n1,n2],axis=0))



#2D Add the elements of numpy array
import numpy as np

n1=np.array([[1,2,3,4,5],[1,2,3,4,5]])
n2=np.array([[3,4,5,6,7],[2,3,4,5,8]])
print("Sum of Column values",np.sum([n1,n2],axis=0))