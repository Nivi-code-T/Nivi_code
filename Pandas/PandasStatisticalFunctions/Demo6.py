#Get the median values using median() in Pandas
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

#get the median() marks for each Subject
print("Result\n",df.median())

#get the median() marks for only one Subject
print("Result\n",df['Maths'].median())

