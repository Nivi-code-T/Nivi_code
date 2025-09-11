#Pandas Categorical Data use dtype='category' to create categorises
import pandas as pd

#Create 3 categories
s=pd.DataFrame({'s1':list('abcd'),'s2':list('efgh'),'s3':list('ijkl')},dtype='category')
print("categories=\n",s)
print("dtype=\n",s.dtypes)
