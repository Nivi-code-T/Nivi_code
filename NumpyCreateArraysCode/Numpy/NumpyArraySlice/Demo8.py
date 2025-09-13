#Slicing for both dimensions in Numpy
import numpy as np
n=np.array([[[1,2,3,4],[5,6,7,8]],[[3,5,6,7],[7,8,9,6]]])
print(n)
print(n[0:2:3,2:5:5])