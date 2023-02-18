# isEven.py
# program asks user to enter an int
# output confirms wheather number is even or odd
# Author: Andrea Cignoni

number = int(input ("enter an integer: "))

if (number % 2) == 0:
    print (f"{number} is an even number")
else:
    print(f"{number} is an odd number")