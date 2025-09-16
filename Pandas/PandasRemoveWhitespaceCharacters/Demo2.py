# PANDAS Lstrip() METHOD
#To strip whitespace (including newlines) or specific characters from both the left of
# values in a Series or DataFrame, use the Lstrip() method in Pandas.

import pandas as pd
data=['\tA','!B\n\n','\nC','D\t','E']

#Create Data Set
s=pd.Series(data)
print("Records=\n",s)

#remove whitespace or specific character from left side in series
print("Remove whitespace or specific character=\n",s.str.lstrip('\t!\n'))