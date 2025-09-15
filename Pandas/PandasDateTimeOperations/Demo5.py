#Check the Pandas_leap_year
#is_leap_year() is used in Python Pandas to check the leap year
import pandas as pd
from pandas import Timestamp

timestamp=pd.Timestamp(year=2024,month=12,day=29,hour=11)

#Display The Date
print("Print Day and Time",timestamp)

#Display the number of days in a month
print("is Leap Year ?",timestamp.is_leap_year)