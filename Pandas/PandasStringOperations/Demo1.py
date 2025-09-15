#Pandas lower() method
import pandas as pd

#Data to be sorted in the Pandas Series
data=['Apple','Kiwi','Orange','Banana']

#Create Series using Series() method
s=pd.Series(data)
print("Results=\n",s)

#Conver Data to lowercase using lower()
S=s.str.lower()
print("Display Updated Results=\n",S)