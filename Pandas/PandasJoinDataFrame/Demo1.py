#Join Pandas DataFrame
import pandas as pd
data1={
    'Student':['A','B','C','D','E'],
    'Rank':[1,2,3,4,5],
    'Marks':[90,80,82,88,90]
}
data2={
    'Id':[6,7,8,9,10],
    'Roll':[91,90,98,88,90]
}
df1=pd.DataFrame(data1)
print("Student Records=\n",df1)
df2=pd.DataFrame(data2)
print("Student Records=\n",df2)

#Join DataFrame
dfjoin=df1.join(df2)
print(dfjoin)

