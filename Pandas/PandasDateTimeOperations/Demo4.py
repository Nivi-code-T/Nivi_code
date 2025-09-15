#Get the days in a month
#dayofmonth() is used in Python Pandas to get the day of the week
import pandas as pd
from pandas import Timestamp

timestamp=pd.Timestamp(year=2023,month=12,day=29,hour=11)

#Display The Date
print("Print Day and Time",timestamp)

#Display the number of days in a month
print("Days in a month",timestamp.daysinmonth)

