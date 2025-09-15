#Pnadas item() to iterate over columns
import pandas as pd
data={
    'Student':['A','B','C','D','E'],
    'Marks':[80,85,90,95,98],
    'Ranks':[1,2,3,4,5]
}

df=pd.DataFrame(data)
print("Student Records\n",df)

#Iterate over columns
for col_name,col_data in df.items():
    print("\n",col_name)
    print("\n",col_data)

