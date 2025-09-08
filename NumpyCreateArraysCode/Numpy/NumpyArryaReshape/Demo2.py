#Reshape dimension from 3D to 1D
import numpy as np
n=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("Print 2D array ",n)
reshapen=n.reshape(-1)
print("Reshape from 3D to 1D array",reshapen)
