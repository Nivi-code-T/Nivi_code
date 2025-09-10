#Pandas DataFrame Size
import pandas as pd
data={
    'Student':['A','B','C','D','E'],
    'Rank':[1,2,3,4,5],
    'Marks': [80,90,92,94,98]
}
df=pd.DataFrame(data)
print("Student Records\n",df)
print("Size of Records =",(df.size))
