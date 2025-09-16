#Aggregation Operation - Get the mean of the grouped data
import numpy as np
import pandas as pd
data={
    'Player':['A','B','C','D','E','A','B','F'],
    'Rank':[1,2,3,4,5,6,8,8],
    'Marks':[88,89,90,91,92,93,94,95],
    'Year':[2023,2029,2025,2028,2027,2028,2029,2030]
}

df=pd.DataFrame(data)
print("Records=\n",df)

#Group by Year
newdf=df.groupby('Year')

#Use agg() to perform aggregation
print("Result\n",newdf['Rank'].agg(np.mean))