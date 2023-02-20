# collatz.py
# This program asks the user to input any positive integer,
# then it outputs the successive values resulting from the below calculation.
# If the result is even the amount is devided by two 
# but if it is odd, it is multiplied by three and increased by one.
# The program ends when the current value is one.
# Author: Andrea Cignoni


number = int (input("Please enter a positive integer: "))
while number != 1:
    if number %2 == 0:
        number = number/2
        print(number)
    else:
        number = 3 * number + 1
        print(number)
