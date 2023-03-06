# $ python squareroot.py
# This programe takes a ploating-point number
# and returns an approximation of its square root
# This operations is to be performed by my own sqrt function
# Author: Andrea Cignoni

def square_root(number):
    # applying Newton square root method
    # where x is x**2 - 24 is within epsilon of 0

    epsilon = 0.01
    k = number
    guess = k / 2.0
    while abs(guess*guess - k) >= epsilon:
        guess = guess - (guess ** 2 -k)/ (2*guess)
    return guess

n = float(input("Please enter a positive number: "))
sqroot_number = square_root (n)
print ("The square root of ", n,"is approx.", sqroot_number)