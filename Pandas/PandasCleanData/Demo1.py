#Pandas Clean Data
#Pandas isnull() method
import pandas as pd

#Input CSV File
#Load the CSV in the DataFrame

df = pd.read_csv("D:\\Nivi_Prac\\NT\\Nivi_code\\Pandas\\PandasCleanData\\Demo.csv")
print("Records =\n",df)

#Find null and replace with True
dfnew=df.isnull()
print("New Records= \n",dfnew.to_string())



