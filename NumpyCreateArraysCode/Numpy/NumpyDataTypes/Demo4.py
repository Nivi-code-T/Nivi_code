#Conver one Type to another
import numpy as np
n=np.array(['10','20','30','40'])
print(n)
print(n.dtype)

n1 = n.astype('i')
print(n1)
print(n1.dtype)
