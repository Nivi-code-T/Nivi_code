#Pandas Combine Series
import pandas as pd

data1=[1,2,3,4,5]
s1=pd.Series(data1)
print("Data1= \n",data1)

data2=[6,7,8,9,10]
s2=pd.Series(data2)
print("Data2= \n",data2)

def demo(x1,x2):
    if (x1 > x2):
        return x1
    else:
        return x2

combines=s1.combine(s2,demo)
print("After Combine: \n",combines)


