# What is a Series in Pandas? How to Create?
#
# Series in Pandas is a one-dimensional array, like a column in a table.
# It is a labeled array that can hold data of any type.
# The Series() method is used for this and has the following parameters:
# data: The data to be stored in the Pandas Series
# index: The index values should have the same length as the data
# dtype: It is the datatype for the output Series
# name: Set the series name with the name parameter
# copy: To copy the input data

#Pandas Series : To create Series in pandas we use Series()
import pandas as pd
data=[10,20,30,40,50]
#Create Series as a Out it will display as indexes and columns
s=pd.Series(data)
print("Pandas Series=\n",s)
