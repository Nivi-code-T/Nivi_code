#sum() method in Pandas

import pandas as pd
Marks = {
    'Maths':[1,2,3,4,5],
    'Science':[6,7,8,9,10],
    'English':[12,17,18,19,20],
}

df=pd.DataFrame(Marks)

#Displat the Records
print("Records",df)

#Sum of marks in each column
print("Sum of Marks\n",df.sum())


