#The groupby() method is used in Pandas to split the object.
# We can define groupby() as grouping the rows/columns into specific groups.
import pandas as pd
data={
    'Player':['A','B','C','D','E','A','B','F'],
    'Rank':[1,2,3,4,5,6,8,8],
    'Marks':[88,89,90,91,92,93,94,95]
}

df=pd.DataFrame(data)
print("Records=\n",df)

#Group the data on Player Value
newdf=df.groupby('Player')

#Dsiplay the First Entry
print("\n",newdf.first())

for Rank,group in newdf:
    print(Rank)
    print(group)
