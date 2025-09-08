#Iterate 3D array
import numpy as np
n=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
for i in n:
    print(i)
print("Type",type(n))
print("Type",n.dtype)
print("Type",n.ndim)
