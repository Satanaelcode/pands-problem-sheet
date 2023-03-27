# Accounts.py
# This program requests to input an account number
# and returns a string displaying the last 4 digits only
# Author: Andrea Cignoni

# Use of input function to ask a user to input his account number
account_number = input('Please enter a 10 digit account number: ')
# Concatenation and slising technique to mask the output and show just the last 4 digits
print ("XXXXXX"+ account_number[6:])

# EXTRA:
# This function will check the length of the input the user provided.
def check_len(account_number):
    if len(account_number) < 10:
        if len(account_number) != 10:
        # If the length of account_number is < 10, inform user that the account number must be at least 10 digits long.
            print("Account number must be atleast 10 digits, Please try again")
    else:
        # Concatenation and slicing technique to mask the output and show just the last 4 digits
        output_number = "X" * 6 + account_number[6:10]
        print("Account Number:", output_number)
# Call the check_len function to verify the length of the input
check_len(account_number)