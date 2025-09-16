#Get the Size of each Group
import numpy as np
import pandas as pd
data={
    'Player':['A','B','C','D','E','A','B','F'],
    'Rank':[1,2,3,4,5,6,8,8],
    'Marks':[88,89,90,91,92,93,94,95]
}

df=pd.DataFrame(data)
print("Records=\n",df)

#Group ny player
newdf=df.groupby('Player')

#The Agg() to perform Aggregation
#Use np.size to get the size of each group
print(newdf.agg(np.size))

