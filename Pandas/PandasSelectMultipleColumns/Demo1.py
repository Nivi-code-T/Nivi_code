#Pandas Select multiple columns
import pandas as pd

df = pd.read_csv("D:\\Nivi_Prac\\NT\\Nivi_code\\Pandas\\PandasReadCSV\\StudentsNew.csv")
#Display Two Column Results

print("Display Result\n",df[['Student','Marks']])

#Practice1
#Create Dataset
data={
    'Student':['A','B','C','D','E'],
    'Ranks':[1,2,3,4,5],
    'Marks':[80,85,90,95,98]
}
df=pd.DataFrame(data)
print("Student Records=\n",df)

#Display only Student and Marks Records
print("Student and Marks Records=\n",df[['Student','Marks']])