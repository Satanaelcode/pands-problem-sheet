# grade.py
# this program reads in a student's percentage mark
# output prints out corresponding the grade
# <40% =fail; 40% to 49% = Pass; 50% to 59% = Merit 2; 
# 60% to 69%= Merit 1; Over 70%= Distinction
# Author: Andrea Cignoni

percentage = float(input("Enter the percentage: "))
# number output in percentage

if percentage < 0 or percentage > 100:
    # if statement necessary to restrict number range
    print ("Please enter a number between 0 and 100")
elif percentage < 40: # lower possible grade already established
    print("Fail")
elif percentage < 50: # between 40 and 49
    print("Pass")
elif percentage < 60: # between 50 and 59
    print("Merit1")
elif percentage < 70: # between 60 and 69
    print("Merit2")
else: # the only option remained up to 100
    print ("Distinction")

# answer to question .3 : variable "number" should be defined as a float instead of int
# or alternatively use the "round" function when printing the outpu
# answer to questio .4   