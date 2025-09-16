#View the group

import pandas as pd
data={
    'Player':['A','B','C','D','E','A','B','F'],
    'Rank':[1,2,3,4,5,6,8,8],
    'Marks':[88,89,90,91,92,93,94,95]
}

df=pd.DataFrame(data)
print("Records=\n",df)

#Group by player view the groups
newdf=df.groupby('Player')
print(newdf.groups)


