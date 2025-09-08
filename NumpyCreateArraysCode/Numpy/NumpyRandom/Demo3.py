#Generate one of the Random values based on an array values
from numpy import random
n=random.choice([1,2,3,4,5,6,7,8,9,10])
print("Random value",n)

#Generate one of the Random values based on an array values with size
from numpy import random
n=random.choice([1,2,3,4,5,6,7,8,9,10],size=(4))
print("Random value",n)