# guess2.py
# this program prompts the user to guess a number
# and, in case of a wrong answer, it indicates 
# whether their guess is too high or too low
# Author: Andrea Cignoni

numberToGuess = 30

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    if guess > numberToGuess:
        print ("too high")
    else:
        print ("too low")
    guess = int(input("Please guess again:"))

print("Well done! Yes the number was ", numberToGuess)



