#Pandas Series info method
import pandas as pd
data=[1,2,3,4,5,6,7,8]
s=pd.Series(data,name='mydata')
print(s)
print("Info of a Series",s.info())