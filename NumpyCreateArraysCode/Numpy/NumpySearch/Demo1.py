#Search a numpy array for value
import numpy as np
n=np.array([1,2,3,4,5])
for i in n:
    print(i)
Searchn=np.where(n==2)
print(Searchn)

n1=np.array([[1,2],[3,4]])
searchn1=np.where(n==1)
print(searchn1)