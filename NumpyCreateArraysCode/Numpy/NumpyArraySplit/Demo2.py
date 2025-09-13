#Access a split 1D array
import numpy as np
n=np.array([1,2,3,4,5,6,7,8])
splitn=np.array_split(n,2)
print("Arrya1 =",splitn[0])
print("Array2 =",splitn[1])
