#Pandas dtype Attribute for Interger
import pandas as pd
data=[10,20,30,40,50]

#Create Series
s=pd.Series(data)
print("Series = \n",s)

#data dtype of a series
print("dtype of Series",s.dtype)

#Pandas dtype Attribute for String
data=['A','B','C','D','E']

#Create Series
s=pd.Series(data)
print("Series = \n",s)

#data dtype of a series
print("dtype of Series",s.dtype)
