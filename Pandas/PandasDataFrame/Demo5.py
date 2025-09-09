# ITERATE A PANDAS DATAFRAME to display the column and rows names
# To iterate a DataFrame and display the column names, use the for loop

import pandas as pd
data={ 'Student':["A","B","C","D","E"],
        'Rank':[1,2,3,4,5],
        'Marks':[80,90,85,88,98]
}

#us the index argument to name indexes
df=pd.DataFrame(data,index=['S1','S2','S3','S4','S5'])
print("Student Records:\n",df)

#Iterating
print("\nDisplaying the columns:")
for col in df.columns:
    print(col)

print("\nDisplaying the rows:\n")
for index,row in df.iterrows():
    print("\n",row)

