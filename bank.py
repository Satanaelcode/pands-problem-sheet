# bank.py
# author : Andrea Cignoni
# weekly task2

# Prompting user to input two integers
number1 = int(input ('Enter amount1(in cent): '))
number2 = int(input ('Enter amount2(in cent): '))
# sum of the amounts divided by 100 
# outputs a flotaing number showing two decimals
sum = float (number1 + number2)/100
# the output is concatenates two strings
print (f"The sum of this is €" + str(sum))