#Get the day of the week
#dayofweek() is used in Python Pandas to get the day of the week
import pandas as pd
from pandas import Timestamp

timestamp=pd.Timestamp(year=2023,month=12,day=29,hour=11)

#Display The Date
print("Print Day and Time",timestamp)

#Display The day of a week
print("Day of the week",timestamp.dayofweek)

#Day Name
print("Day name",timestamp.day_name())




