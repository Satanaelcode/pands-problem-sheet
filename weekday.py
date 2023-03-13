# weekday.py
# This program outputs whether today is a weekday or not
# Author: Andrea Cignoni

# Importing the datime module to work with dates and times
import datetime

# Getting the current weekday as an integer (0  for Monday, 1 for Tuesday, ..., 6 for Sunday)
weekno = datetime.datetime.today().weekday()
# If the weekday integer is less than 5 (i.e., it's a weekday from Monday to Friday) 
if weekno < 5:
    print("Yes, unfortunately today is a weekday") # Print a message indicating that it's a weekday
else:  
    # Otherwise, print a message indicating that it's the weekend
    print("It is the weekend, yay!")

