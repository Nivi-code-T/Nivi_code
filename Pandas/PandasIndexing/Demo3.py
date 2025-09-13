#Pandas Indexing from csv File
import pandas as pd

#Specify the path and Index Column
df = pd.read_csv("D:\\Nivi_Prac\\NT\\Nivi_code\\Pandas\\PandasReadCSV\\StudentsNew.csv")

#Display the CSV file records
print("Display CSV Data\n",df)

#Specify the index using loc
Indexdf=df.iloc[0]
print("Indexing=\n",Indexdf)