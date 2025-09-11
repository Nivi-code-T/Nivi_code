#Pandas Categorical Data use dtype='category' to create categorises
import pandas as pd
#Create Categorical Series
s=pd.Series(['a','b','c','d','e'], dtype= "category" )
print("Series =\n",s)