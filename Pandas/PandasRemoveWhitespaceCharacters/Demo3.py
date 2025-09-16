# PANDAS rstrip() METHOD
#To strip whitespace (including newlines) or specific characters from both the right of
# values in a Series or DataFrame, use the rstrip() method in Pandas.

import pandas as pd
data=['\tA!','!B\n\n','\nC','D\t','E']

#Create Data Set
s=pd.Series(data)
print("Records=\n",s)

#remove whitespace or specific character from right side in series
print("Remove whitespace or specific character=\n",s.str.rstrip('\t!\n'))