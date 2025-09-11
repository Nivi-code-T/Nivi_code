#Pandas Series Indexes
import pandas as pd

data=[1,2,3,4,5]
s=pd.Series(data,index=['Row1','Row2','Row3','Row4','Row5'],name='MyData')
print("Series Data = \n",s)
print("Indexes of Series = \n",s.index)