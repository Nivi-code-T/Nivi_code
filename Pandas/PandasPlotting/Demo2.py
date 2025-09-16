#Plot Histogram in Pandas
import matplotlib.pyplot as plt
import pandas as pd

#Craete DataSet
data={
    'Temperature':[27,19,20,21,22,23,24,25,26,18],
    'Humidity':[30,35,32,38,34,17,36,37,33,39],
    'Wind':[17,9,11,10,12,13,14,15,16,8],
    'Precipitation':[17,18,28,30,32,45,38,32,20,22]
}

#Create DataFrame
df=pd.DataFrame(data)
print("Records=\n",df)

#Plot Histogram
df['Humidity'].plot(kind='hist')

#Disply Plot
plt.show()