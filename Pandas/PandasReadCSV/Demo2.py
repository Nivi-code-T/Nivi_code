#Read Top Rows Value from Data
import pandas as pd

#Display Top 5 Rows Value
df = pd.read_csv("D:\\Nivi_Prac\\NT\\Nivi_code\\Pandas\\PandasReadCSV\\StudentsNew.csv")
print("Top 5 Rows=\n",df.head())

#Display Top 2 Rows
print("Top 2 Rows=\n",df.head(2))

