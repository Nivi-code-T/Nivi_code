#Read Last Rows Value from Data
import pandas as pd

#Display Last 5 Rows Value
df = pd.read_csv("D:\\Nivi_Prac\\NT\\Nivi_code\\Pandas\\PandasReadCSV\\StudentsNew.csv")
print("Last 5 Rows=\n",df.tail())

#Display Last 2 Rows
print("Last 2 Rows=\n",df.tail(2))