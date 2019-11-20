"""
A1_3_2 #Replace With Your Last Name.py
Programmer: Ethan S
"""

import random
guess = 23
def hiLo_game(guess):
    rand_num = random.randint(1,100)
    if guess == rand_num:
        print ("Yes! You got it right!")
    elif guess < rand_num:
            print ('Your guess was too low. Try again!')
    else:
            print ("Your guess was too high! Try again!")

hiLo_game(guess)
