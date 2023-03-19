# Accounts.py
# This program requests to input an account number
# and returns a string displaying the last 4 digits only
# Author: Andrea Cignoni

# Use of input function to ask a user to input his account number
account_number = input('Please enter a 10 digit account number: ')
# Concatenation and slising technique to mask the output and show just the last 4 digits
print("XXXXXX"+ account_number[6:])