#Pandas Delete Columns using drop() in DataFrame
import numpy as np
import pandas as pd

data={
    'Student':['A','B','C','D','E'],
    'Marks':[80,85,90,95,98],
    'Ranks':[1,2,3,4,5]
}

df=pd.DataFrame(data)
print("Student Records\n",df)

#Delete Columns
deleteRColumns=df.drop('Student',axis="columns")

#Or
deleteRColumns=df.drop('Student',axis=1)

print("Student Records After dropping columns= \n",deleteRColumns)

