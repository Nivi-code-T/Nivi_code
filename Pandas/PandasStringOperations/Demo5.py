#pandas nonempty cell for each column or rows using count()
import numpy as np
import pandas as pd

#Data to be sorted in the Pandas Series
data=[np.nan,'aPPle','KIwi','OraNge','baNAna']

#Create Series using Series() method
s=pd.Series(data)
print("Results=\n",s)

#Count nonempty cell values
print("Count =",s.count())
