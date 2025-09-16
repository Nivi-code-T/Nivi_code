#I. PANDAS strip() METHOD
#To strip whitespace (including newlines) or specific characters from both the left and right side of
# values in a Series or DataFrame, use the strip() method in Pandas.

import pandas as pd
data=['A','B\n\n','C','D\t','E']

#Create Data Set
s=pd.Series(data)
print("Records=\n",s)

#remove whitespace or specific character in series
print("Remove whitespace or specific character=\n",s.str.strip('\n\t'))