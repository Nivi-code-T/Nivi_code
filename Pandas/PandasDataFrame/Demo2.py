#Access group of rows or columns in a pandas DataFrame
import pandas as pd
#Create DataSet

data={ 'Student':["A","B","C","D","E"],
        'Rank':[1,2,3,4,5],
        'Marks':[80,90,85,88,98]
}

df=pd.DataFrame(data,index=['RowA','RowB','RowC','RowD','RowE'])
print("Student Records\n",df)

#Access the value in the student column corresponding to the RowA label

print("RowA Value =",df.loc['RowA','Student'])