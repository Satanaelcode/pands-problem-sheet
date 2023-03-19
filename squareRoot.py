# $ python squareroot.py
# This programe takes a ploating-point number
# and returns an approximation of its square root
# This operations is to be performed by my own sqrt function
# Author: Andrea Cignoni

# Create a function to calculate a function of a number
def square_root(number):
    # applying Newton square root method
    # where x is x**2 - 24 is within epsilon of 0

    # set the level of accuracy we want achieve (0.01)
    epsilon = 0.01
    # assigned input number to the variable k
    k = number
    # set the initial guess for the square root to the half of the input number
    guess = k / 2.0
    # absolute function used to make output number positive regardless the result
    while abs(guess*guess - k) >= epsilon:
        guess = guess - (guess ** 2 -k)/ (2*guess)
    return guess
# Asking the user to enter a positive number
n = float(input("Please enter a positive number: "))
# Call the square_root function with the user input as the argument and assign the result to a variable
sqroot_number = square_root (n)
# Print the input number and its approximate quare root with one decimal point precision
print ("The square root of ", n,"is approx.", "%.1f" %sqroot_number)