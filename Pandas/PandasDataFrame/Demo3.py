#Access group of rows or columns integer positions in a pandas DataFrame
import pandas as pd

#DataSet
data={ 'Student':["A","B","C","D","E"],
        'Rank':[1,2,3,4,5],
        'Marks':[80,90,85,88,98]
}

df=pd.DataFrame(data,index=['RowA','RowB','RowC','RowD','RowE'])
print("Student Records\n",df)

#Access using rows or columns by integer positions
print("Value = \n",df.iloc[[0,1]])
print("Value = \n",df.iloc[[2,3]])
print("Value = \n",df.iloc[[3,4,2]])
print("Value = \n",df.iloc[[0,1,2,3,4]])
