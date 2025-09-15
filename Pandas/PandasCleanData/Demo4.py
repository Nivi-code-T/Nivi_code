#Pandas Clean Data
#Pandas df.fillna(x) method
import pandas as pd

#Input CSV File
#Load the CSV in the DataFrame

df = pd.read_csv("D:\\Nivi_Prac\\NT\\Nivi_code\\Pandas\\PandasCleanData\\Demo.csv")
print("Records =\n",df)

#Fill Null values using fillna()
dfnew=df.fillna(12.12)
print("New Records= \n",dfnew.to_string())

