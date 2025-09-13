#Add new Column using Assign() in Pandas DataFrame
import pandas as pd
from pandas import DataFrame

#Create Dataset
data={
    'Student':['A','B','C','D','E'],
    'Ranks':[1,2,3,4,5],
    'Marks':[80,85,90,95,98],
    'Code':[11,12,14,15,16]
}
df=pd.DataFrame(data)
print(df)

#Insert New Column using assign
newdf=df.assign(Address=['East','West','South','North','NorthEast'])
print("Updated Record=\n",newdf)