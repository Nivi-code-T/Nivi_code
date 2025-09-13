#Select Multiple Columns in a range with Pandas
import pandas as pd
from pandas import DataFrame

#Create Dataset
data={
    'Address':['East','West','South','North','NorthEast'],
    'Student':['A','B','C','D','E'],
    'Ranks':[1,2,3,4,5],
    'Marks':[80,85,90,95,98],
    'Code':[11,12,14,15,16]
}
df=pd.DataFrame(data)
print("Student Records=\n",df)

Columndf=df[df.columns[:1]]

#Display multiple column in range
print("Student and Marks Records=\n",Columndf)

