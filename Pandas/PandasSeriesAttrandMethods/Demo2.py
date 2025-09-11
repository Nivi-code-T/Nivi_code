#Dimensions in Padas Series
import pandas as pd
data=[1,2,3,4,5]

#1D Array
print("Dimensions = ",pd.Series(data).ndim)

#2D Array
import pandas as pd
data1={
    'student1':['Alice', 25, 'New York'],
    'student2':['Bob', 30, 'London'],
    'student3':['Charlie', 22, 'Paris']
}
print("Dimensions = ",pd.Series(data1).ndim)
