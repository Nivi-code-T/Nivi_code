#Get the std values using std() in Pandas
#count() in Pandas
import numpy as np
import pandas as pd
Marks = {
    'Maths':[1,2,3,4,5],
    'Science':[6,7,8,9,10],
    'English':[12,17,18,19,20],
}

df=pd.DataFrame(Marks)

#Displat the Records
print("Records",df)

#get the std()
print("Result\n",df.std())



