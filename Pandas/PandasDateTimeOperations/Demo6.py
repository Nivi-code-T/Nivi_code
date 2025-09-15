#Check the last day of month end using is_month_end
#is_month_end is used in Python Pandas to check the last day of a month
import pandas as pd
from pandas import Timestamp

timestamp=pd.Timestamp(year=2024,month=12,day=30,hour=11)

#Display The Date
print("Print Day and Time",timestamp)

#Check is month end or not
print("Is This Month End ?",timestamp.is_month_end)

