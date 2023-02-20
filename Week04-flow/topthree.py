# topthree.py
# this program generates 10 random numbers,
# prints them out then prints out the top three
# It includes a list to store and manipulate numbers
# Author: Andrea Cignoni

import random
# I programming the general case
howMany     = 10
topHowMany  = 3
rangeFrom   = 0
rangeto     = 100

numbers = []

for i in range (0,howMany):
    numbers.append(random.randint(rangeFrom,rangeto))
print(f"{howMany} random numbers\t {numbers}")

# original listn kept
topOnes = numbers.copy()

topOnes.sort (reverse = True)
print ("The top {topHowMany} are \t\t{topOnes[0:topHowMany]}")

# This program does not run correctly