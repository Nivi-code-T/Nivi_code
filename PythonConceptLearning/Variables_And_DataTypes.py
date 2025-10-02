#Create variable
age=30
name="Python"

#Print DataType of the variable
print(type(age))
print(type(name))

#Convert Variable to different data type
age_float=float(age)
print(age_float)

#Integer to String
int1=15
str=str(int1)
print(str)

#string to bool
str_bool_true=bool('hello')
str_bool_false=bool('')
print(f"{str_bool_true}")
print(f"{str_bool_false}")

#float to integer
float=15.55
float_int=int(float)
print(float_int)

#print()
print("apple","banana",sep=' ')
print("apple","banana",sep='-')
print("apple is super",end=' ')
print("apple is sweet")