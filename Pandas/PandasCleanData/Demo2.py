#Pandas Clean Data
#Pandas notnull() method
import pandas as pd

#Input CSV File
#Load the CSV in the DataFrame

df = pd.read_csv("D:\\Nivi_Prac\\NT\\Nivi_code\\Pandas\\PandasCleanData\\Demo.csv")
print("Records =\n",df)

#Find notnull and replace with True
dfnew=df.notnull()
print("New Records= \n",dfnew.to_string())

