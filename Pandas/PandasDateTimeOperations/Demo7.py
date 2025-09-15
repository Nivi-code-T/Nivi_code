#Check if the date is the first day of the month
#use is_month_start()
import pandas as pd
from pandas import Timestamp

timestamp=pd.Timestamp(year=2024,month=12,day=30,hour=11)

#Display The Date
print("Print Day and Time",timestamp)

#Check first day of the month
print("Is It First day of the month?",timestamp.is_month_start)


#Test2
timestamp1=pd.Timestamp(year=2024,month=12,day=1,hour=11)

#Display The Date
print("Print Day and Time",timestamp1)

#Check first day of the month
print("Is It First day of the month?",timestamp1.is_month_start)