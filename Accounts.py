# Accounts.py
# This program requests to input an account number
# and returns a string displaying the last 4 digits only
# Author: Andrea Cignoni

account_number = input('Please enter a 10 digit account number: ')
print("XXXXXX"+ account_number[6:])