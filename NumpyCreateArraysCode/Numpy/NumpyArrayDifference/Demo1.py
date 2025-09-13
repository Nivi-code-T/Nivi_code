#Find the difference between two arrays n1-n2
import numpy as np
n1=np.array([1,6,8,2,4,6,17,43,1,4,5,7,5,44,2,3,45,6,7,8])
n2=np.array([1,4,6,3,1,18,12,15,8,2,3,4,5,66,7,78,8,7])
print("Difference",np.setdiff1d(n1,n2))