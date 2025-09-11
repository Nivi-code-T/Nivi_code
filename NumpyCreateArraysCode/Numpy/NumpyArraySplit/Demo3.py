#Split 2D array
import numpy as np
n=np.array([[[1,2,3,4],[5,6,7,8]],[[1,2,3,4],[5,6,7,8]]])
splitn=np.array_split(n,2)
print(splitn)
