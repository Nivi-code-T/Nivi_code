#Join arrays using stack
import numpy as np
n1=np.array([1,2,3,4,5])
n2=np.array([1,2,3,4,5])
n3=np.stack((n1 ,n2),axis=1)
print(n3)

