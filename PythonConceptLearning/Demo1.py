# #write a program that reads a fractional number in inches and converts it to centimeters:
# inch=float(input("Enter inch = "))
# centemeter = inch * 2.54
# print(centemeter)
#
# first_name = input()
# last_name = input()
# age = int(input())
# town = input()
#
# print('You are {0} {1}, a {2}-year-old person from {3}.')
import math

#Test1
width=5
height=10.5
area=width*height
print('width=',width,'; height=',height,'; area=',area)

#Rounding of number
roundoff=round(area)
print("roundoff=",roundoff)

#Rounding of number
roundoff=math.ceil(area)  #will round of to bigger number
print("roundoff=",roundoff)

#Rounding of number
roundoff=math.floor(area)  #will round of to smaller number
print("roundoff=",roundoff)



