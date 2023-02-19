# randomNumber.py
# Program to generate a random number between 0 and 30
# importing the random module
# asking a user to guess this number until he gets it right
# Author: Andrea Cignoni

import random
numberToGuess= random.randint(0,30)

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("too low")
    else:
        print("too high")
    guess = int(input("Please guess again:"))


print("Well done! Yes the number was ", numberToGuess)