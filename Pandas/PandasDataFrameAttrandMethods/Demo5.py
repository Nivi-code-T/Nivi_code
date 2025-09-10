#Pandas DataFrame index
import pandas as pd
data={
    'Student':['A','B','C','D','E'],
    'Rank':[1,2,3,4,5],
    'Marks': [80,90,92,94,98]
}
df=pd.DataFrame(data,index=['RowA','RowB','RowC','RowD','RowE'])
print("Student Records\n",df)
print("index Attribute =",(df.index))