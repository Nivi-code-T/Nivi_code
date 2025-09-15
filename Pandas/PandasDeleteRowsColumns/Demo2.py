#Pandas Delete Rows using drop() in DataFrame
import pandas as pd

data={
    'Student':['A','B','C','D','E'],
    'Marks':[80,85,90,95,98],
    'Ranks':[1,2,3,4,5]
}

df=pd.DataFrame(data,index=['Row1','Row2','Row3','Row4','Row5'])
print("Student Records\n",df)

#Delete rows
deleteRows=df.drop('Row2',axis="index")

#Or
#deleteRows=df.drop('Student',axis=1)
print("Student Records After dropping rows= \n",deleteRows)

#Example 2
data={
    'Student':['A','B','C','D','E'],
    'Marks':[80,85,90,95,98],
    'Ranks':[1,2,3,4,5]
}

df=pd.DataFrame(data)
print("Student Records\n",df)

#Delete rows
deleteRows=df.drop(4,axis=0)

#Or
#deleteRows=df.drop('Student',axis=1)

print("Student Records After dropping rows= \n",deleteRows)
