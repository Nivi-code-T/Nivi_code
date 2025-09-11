#Access Values from Series using []
import pandas as pd
data=[10,20,30,40,50]
#Create Series as  Out it will display as indexes and columns
s=pd.Series(data)
print("Pandas Series=\n",s)

#Access Value from Pandas Series
print("Access value from Pandas Series =",s[0])