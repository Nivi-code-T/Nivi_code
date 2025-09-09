#NAME YOUR INDEXES IN A PANDAS DATAFRAME
#The index argument is used to set and name your own indexes in a DataFrame.

import pandas as pd
data={ 'Student':["A","B","C","D","E"],
        'Rank':[1,2,3,4,5],
        'Marks':[80,90,85,88,98]
}

#us the index argument to name indexes
df=pd.DataFrame(data,index=['S1','S2','S3','S4','S5'])
print("Student Records:\n",df)

