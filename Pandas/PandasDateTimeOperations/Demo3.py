#Get the day of year
#dayofyear() is used in Python Pandas to get the day of the week
import pandas as pd
from pandas import Timestamp

timestamp=pd.Timestamp(year=2023,month=12,day=29,hour=11)

#Display The Date
print("Print Day and Time",timestamp)

#Day of year
print("Day of Year",timestamp.dayofyear)
