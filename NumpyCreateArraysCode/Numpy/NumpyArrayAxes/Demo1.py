#Get minimum value in array numpy
import numpy as np
n=np.array([[1,2,3,4],[5,6,7,8]])
print("Dimension",n.ndim)
print("Minimun",n.min())
print("Minimun Value Vertical (Axes is Zero)",n.min(axis = 0))
print("Minimun Value Horizontal (Axes is One)",n.min(axis = 1))