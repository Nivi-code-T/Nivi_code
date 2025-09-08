#Intersection between 2 arrays
import numpy as np
n1=np.array([1,2,10,4,5])
n2=np.array([8,2,3,4,9])
print("Interate Array")
for i in n1:
    print(i)
print("Iterating Array2")
for i in n2:
    print(i)

Intern=np.intersect1d(n1,n2)
print("Intersection Arrays",Intern)