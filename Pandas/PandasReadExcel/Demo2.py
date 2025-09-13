#Read Top N Rows
import pandas as pd

#input CSV and Loading xlsx in DataFrame
df = pd.read_excel("D:\\Nivi_Prac\\NT\\Nivi_code\\Pandas\\PandasReadExcel\\Students.xlsx")
print("Our DataFrame =\n",df)

#Read Top n Rows
print("Top N Rows=\n",df.head())

#Read Top 2 Rows
print("Top N Rows=\n",df.head(2))
