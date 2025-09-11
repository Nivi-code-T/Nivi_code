#Pandas Series head() Attribute
import pandas as pd
data=[1,2,3,4,5,6,7,8]

s=pd.Series(data,index=['Row1','Row2','Row3','Row4','Row5','Row6','Row7','Row8'])
print("My Data=\n",s)
#head() will display First 5 rows values
print("First 5 Rows of a Series \n",s.head())

