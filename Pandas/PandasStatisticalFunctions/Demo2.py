#count() in Pandas
import pandas as pd
Marks = {
    'Maths':[1,2,None,4,5],
    'Science':[None,7,8,9,10],
    'English':[12,17,18,19,20],
}

df=pd.DataFrame(Marks)

#Displat the Records
print("Records",df)

#Count the non empty values
print("Result\n",df.count())
