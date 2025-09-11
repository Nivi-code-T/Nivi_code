#Get Maximun value in array numpy
import numpy as np
n=np.array([[1,2,3,4],[5,6,7,8]])
print("Dimension",n.ndim)
print("Maximun",n.max())
print("Maximun Value Vertical (Axes is Zero)",n.max(axis = 0))
print("Maximun Value Horizontal (Axes is One)",n.max(axis = 1))