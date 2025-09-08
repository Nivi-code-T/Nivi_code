#1D Substract numpy array
import numpy as np
n1=np.array([1,2,3,4,5])
n2=np.array([2,5,8,4,5])
print("Subtraction result",np.subtract(n1,n2))


#2D Substract numpy array
import numpy as np
n1=np.array([[1,2,3,4,5],[6,7,8,9,10]])
n2=np.array([[2,5,8,4,5],[11,12,13,14,15]])
print("Subtraction Result",np.subtract(n1,n2))

#2D Sub the elements of numpy array
import numpy as np

n1=np.array([[1,2,3,4,5],[1,2,3,4,5]])
n2=np.array([[3,4,5,6,7],[2,3,4,5,8]])
n=n1-n2
print(n)