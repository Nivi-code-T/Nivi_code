#Pandas Clean Data
#Pandas dropna() method
import pandas as pd

#Input CSV File
#Load the CSV in the DataFrame

df = pd.read_csv("D:\\Nivi_Prac\\NT\\Nivi_code\\Pandas\\PandasCleanData\\Demo.csv")
print("Records =\n",df)

#drop and remove null values
dfnew=df.dropna()
print("New Records= \n",dfnew.to_string())

