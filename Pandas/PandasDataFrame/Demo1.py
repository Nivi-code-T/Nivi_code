# WHAT IS A PANDAS DATAFRAME? HOW TO CREATE?
# The Pandas DataFrame is a two-dimensional, tabular data, table with rows and columns.
# The DataFrame() method is used to create a DataFrame and has the following parameters:

# data: The data to be stored in the Pandas DataFrame
# index: The index values to be provided for the resultant frame.
# columns: Set the column labels for the resultant frame if data does not mention before
# dtype: It is the datatype and only a single type is allowed.
# copy: To copy the input data

#Create a Pandas DataFrame
import pandas as pd

#Create DataSet
data={ 'Student':["A","B","C","D","E"],
        'Rank':[1,2,3,4,5],
        'Marks':[80,90,85,88,98]
}

df=pd.DataFrame(data)
print("Student Records\n",df)

