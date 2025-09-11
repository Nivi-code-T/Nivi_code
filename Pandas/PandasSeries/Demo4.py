#Access Value from a Pandas Series from labels

import pandas as pd
data=[10,20,30,40,50]

#Name your Indexes

s=pd.Series(data,index=['Row1','Row2','Row3','Row4','Row5'])
print("Created Own Index=\n",s)

#Access Value from labels
print("Value from a lable = ",s['Row1'])

