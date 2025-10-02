#Circle Area and Perimeter
#circle= pi*r*r
#perimeter= 2*pi*r

import math
from datetime import datetime, timedelta

r=5
c=math.pi*r*r
p=2*math.pi*r
print(f"c={c}\np={p}")
print(f"c={round(c)}\np={round(p)}")
print(f"c={math.ceil(c)}\np={math.ceil(p)}")
print(f"c={math.floor(c)}\np={math.floor(p)}")

#Printing a text by placeholders
print('c={}\np={}'.format(c,p))

#Triangle are
a=1.2345
h=4.5678
area=a*h/2
print(f"area ={round(area,2)}")


# Calculate 1000 days after birth
date_birth_str=(input("Enter date in dd-mm-yyyy= "))
date_birth=datetime.strptime(date_birth_str,"%Y-%m-%d")
date_birth_after_1000days=date_birth+timedelta(days=1000)
print("",date_birth_after_1000days.strftime("%d-%m-%Y)"))

now = datetime.now()
formatted_string = now.strftime("%A, %B %d, %Y %H:%M:%S")
print(formatted_string)

