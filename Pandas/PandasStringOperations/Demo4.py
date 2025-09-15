#Get the length of each elements in Series
#len() method in pandas
import pandas as pd

#Data to be sorted in the Pandas Series
data=['aPPle','KIwi','OraNge','baNAna']

#Create Series using Series() method
s=pd.Series(data)
print("Results=\n",s)

#Get the length of each element
print("Length of Each element =\n",s.str.len())

