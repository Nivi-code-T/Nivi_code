#Pandas DataFrame tail() will return last 5 Rows
import pandas as pd
data={
    'Student':['A','B','C','D','E','F','G'],
    'Rank':[1,2,3,4,5,6,7],
    'Marks': [80,90,92,94,98,92,94]
}
df=pd.DataFrame(data,index=['RowA','RowB','RowC','RowD','RowE','RowF','RowG'])
print("Student Records\n",df)

#Displayed Last 5 Rows
print("First 5 Rows=\n",(df.tail()))

#Displayed Last 2 Rows
print("First 2 Rows=\n",(df.tail(2)))