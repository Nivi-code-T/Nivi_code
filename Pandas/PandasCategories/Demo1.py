#Append New categories in pandas
import pandas as pd

#Create Category Series
s=pd.Series(['a','b','c','d'],dtype='category')
print(s)

#add Category using add_categories
s=s.cat.add_categories('t')
print(s)