#Pandas upper() method
import pandas as pd

#Data to be sorted in the Pandas Series
data=['apple','kiwi','orange','banana']

#Create Series using Series() method
s=pd.Series(data)
print("Results=\n",s)

#Conver Data to lowercase using upper()
S=s.str.upper()
print("Display Updated Results=\n",S)