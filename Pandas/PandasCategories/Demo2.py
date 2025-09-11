#Remove New categories in pandas
import pandas as pd

#Create Category Series
s=pd.Series(['a','b','c','d','e'],dtype='category')
print(s)

#remove Category using remove_categories
s=s.cat.remove_categories('e')
print(s)