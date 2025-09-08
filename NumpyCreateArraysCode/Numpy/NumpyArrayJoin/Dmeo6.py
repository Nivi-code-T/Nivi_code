#Join arrays using dstack
import numpy as np
n1=np.array([1,2,3,4,5])
n2=np.array([1,2,3,4,5])
n3=np.column_stack((n1, n2))
print(n3)