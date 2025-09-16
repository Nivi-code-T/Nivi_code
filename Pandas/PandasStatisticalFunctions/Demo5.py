#Get the mean values using mean() in Pandas
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

#get the mean() marks for each Subject
print("Result\n",df.mean())

#get the mean() marks for only one Subject
print("Result\n",df['Maths'].mean())

