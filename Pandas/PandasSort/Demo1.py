#Pandas Sorting in DataFrame (Default sort will be in ascending)
import pandas as pd

#Create DataSet
data={
    'Student':['A','B','C','D','E'],
    'Marks':[1,2,3,4,5],
    'Rank':[98,85,92,99,99],
    'ID':[11,12,13,14,15]
}

df=pd.DataFrame(data)
print("Student Records=\n",df)

#Sort the DataFrame
sortdf=df.sort_values(by=['Rank'])
print("Sort in Ascending Order=\n",sortdf)

