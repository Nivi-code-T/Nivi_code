#Name Attribute in Pandas Series
import pandas as pd
data=[1,2,3,4,5]
#use name to display Series name
s=pd.Series(data,name="MyData")
print("My Records",s)
print("Result=",s.name)