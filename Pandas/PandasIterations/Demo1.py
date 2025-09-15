#Pandas iterrows() to iterate over rows
import pandas as pd
data={
    'Student':['A','B','C','D','E'],
    'Marks':[80,85,90,95,98],
    'Ranks':[1,2,3,4,5]
}

df=pd.DataFrame(data)
print("Student Records\n",df)

#Iterate over rows
for rows in df.iterrows():
    print("\n",rows)

#Pandas columns() to iterate over rows
#Iterate over columns
for col in df.columns:
    print("\n",col)