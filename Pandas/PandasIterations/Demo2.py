#Pandas itertuples() to iterate over rows
import pandas as pd
data={
    'Student':['A','B','C','D','E'],
    'Marks':[80,85,90,95,98],
    'Ranks':[1,2,3,4,5]
}

df=pd.DataFrame(data)
print("Student Records\n",df)

#Iterate over rows
for rows in df.itertuples():
    print("\n",rows)

