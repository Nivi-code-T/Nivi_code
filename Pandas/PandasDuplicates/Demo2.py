#Remove Duplicates using the drop_duplicates()
import pandas as pd

data={
    'Student':['A','A','C','D','E'],
    'Marks':[1,1,3,4,5],
    'Rank':[98,98,92,99,99],
    'ID':[11,11,13,14,15]
}

df=pd.DataFrame(data)
print("Student Records = \n",df)

#drop Duplicates
duplicatedf=df.drop_duplicates()
print("Removed Duplicates =\n",duplicatedf)
