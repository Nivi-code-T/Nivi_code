#Contains in Pandas : Search for a value in a column using contains()

import numpy as np
import pandas as pd

#Data to be sorted in the Pandas Series
data=[np.nan,'Apple','Kiwi','Orange','Banana']

#Create Series using Series() method
s=pd.Series(data)
print("Results=\n",s)

#Search for Specific Value and it will write it as True
print("Saerch for Specific Value =",s.str.contains('Apple'))

