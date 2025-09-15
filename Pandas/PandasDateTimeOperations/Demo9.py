#Check if the date is the first day of the year
#use is_year_end()
import pandas as pd
from pandas import Timestamp

timestamp=pd.Timestamp(year=2024,month=1,day=1,hour=11)

#Display The Date
print("Print Day and Time",timestamp)

#Check if the date is the last day of the year
print("Is year start day?",timestamp.is_year_start)


#Test2
timestamp1=pd.Timestamp(year=2024,month=12,day=31,hour=11)

#Display The Date
print("Print Day and Time",timestamp1)

#Check if the date is the last day of the year
print("Is year start day?",timestamp1.is_year_start)
