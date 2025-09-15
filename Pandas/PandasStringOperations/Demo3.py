#Pandas title() method in pandas
import pandas as pd

#Data to be sorted in the Pandas Series
data=['aPPle','KIwi','OraNge','baNAna']

#Create Series using Series() method
s=pd.Series(data)
print("Results=\n",s)

#Convert Text data to camel case (Converts First letter in Capital)
S=s.str.title()
print("Results=\n",S)
